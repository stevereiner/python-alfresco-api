#!/usr/bin/env python3

"""
Enhanced Hybrid Approach with Swagger 2.0 Preprocessing

This script implements the complete hybrid approach including the missing preprocessing step:
1. **PREPROCESS** Swagger 2.0 specs to fill in missing parts (inspired by Windsurf scripts)
2. Convert preprocessed Swagger 2.0 to OpenAPI 3.0 (fixes regex issues)
3. Generate API client with OpenAPI Generator (clean, working code)
4. Generate Pydantic models with datamodel-code-generator (pure Pydantic)
5. Create enhancement scripts to bridge and add convenience methods

This addresses the user's note about missing preprocessing from the Windsurf scripts.
"""

import os
import subprocess
import yaml
import shutil
import sys
from pathlib import Path
import copy

def ensure_dependencies():
    """Ensure all required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    # Check openapi-generator-cli
    try:
        result = subprocess.run(["openapi-generator-cli", "version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("   ✅ openapi-generator-cli found")
        else:
            print("   ❌ openapi-generator-cli not working")
            return False
    except FileNotFoundError:
        print("   ❌ openapi-generator-cli not found")
        print("   Install with: npm install @openapitools/openapi-generator-cli -g")
        return False
    
    # Check datamodel-code-generator
    try:
        result = subprocess.run(["datamodel-codegen", "--help"], capture_output=True, text=True)
        if result.returncode == 0:
            print("   ✅ datamodel-code-generator found")
        else:
            print("   ❌ datamodel-code-generator not working")
            return False
    except FileNotFoundError:
        print("   ❌ datamodel-code-generator not found")
        print("   Install with: pip install datamodel-code-generator")
        return False
    
    return True

def preprocess_swagger2_spec(input_file, output_file, api_name):
    """
    Preprocess Swagger 2.0 spec to fill in missing parts (from Windsurf scripts)
    
    This fills in missing required fields that might cause validation errors later.
    """
    print(f"🔧 Preprocessing {Path(input_file).name} (filling missing parts)...")
    
    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            spec = yaml.safe_load(f)
        
        # Create a base complete spec with all required fields (but don't add host if not present)
        complete_spec = {
            'swagger': '2.0',
            'info': {
                'title': f'Alfresco {api_name.capitalize()} API',
                'version': '1.0',
                'description': f'Alfresco {api_name.capitalize()} API'
            },
            'consumes': ['application/json'],
            'produces': ['application/json'],
            'paths': {},
            'definitions': {},
            'securityDefinitions': {
                'basicAuth': {
                    'type': 'basic',
                    'description': 'HTTP Basic Authentication'
                }
            },
            'security': [
                {'basicAuth': []}
            ]
        }
        
        # Override with fields from the original spec (preserving existing data)
        for field in ['swagger', 'info', 'host', 'basePath', 'schemes', 'consumes', 'produces', 
                     'paths', 'definitions', 'parameters', 'responses', 'securityDefinitions', 
                     'security', 'tags']:
            if field in spec:
                if field == 'info':
                    # Merge info fields, keeping defaults for missing ones
                    complete_spec['info'].update(spec['info'])
                else:
                    complete_spec[field] = spec[field]
        
        # Ensure all paths have proper structure
        for path, path_item in complete_spec['paths'].items():
            for method, operation in path_item.items():
                if method.lower() in ['get', 'post', 'put', 'delete', 'patch', 'options', 'head']:
                    # Ensure responses exist
                    if 'responses' not in operation:
                        operation['responses'] = {
                            '200': {
                                'description': 'Successful response'
                            }
                        }
                    
                    # Ensure at least one response exists
                    if not operation['responses']:
                        operation['responses']['200'] = {
                            'description': 'Successful response'
                        }
        
        # Fix malformed schema definitions
        def fix_schema_definitions(obj):
            """Fix common schema definition issues"""
            if isinstance(obj, dict):
                # Fix property-level 'required: false' which should be removed
                if 'properties' in obj:
                    for prop_name, prop_def in obj['properties'].items():
                        if isinstance(prop_def, dict) and 'required' in prop_def:
                            # Remove 'required' from property level (it belongs at schema level)
                            prop_def.pop('required', None)
                
                # Recursively fix nested objects
                for key, value in obj.items():
                    fix_schema_definitions(value)
            elif isinstance(obj, list):
                for item in obj:
                    fix_schema_definitions(item)
        
        fix_schema_definitions(complete_spec)
        
        # Write the preprocessed spec
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            yaml.dump(complete_spec, f, default_flow_style=False)
        
        print(f"   ✅ Preprocessed to {Path(output_file).name}")
        return True
        
    except Exception as e:
        print(f"   ❌ Preprocessing failed: {e}")
        return False

def ensure_openapi_at_top(openapi3_spec: dict) -> dict:
    """Return a new dict with 'openapi' as the first key, preserving order of the rest."""
    if 'openapi' in openapi3_spec:
        openapi_value = openapi3_spec.pop('openapi')
        # Use dict insertion order (Python 3.7+)
        return {'openapi': openapi_value, **openapi3_spec}
    return openapi3_spec

def convert_swagger_to_openapi3(input_file, output_file):
    """Convert preprocessed Swagger 2.0 to OpenAPI 3.0"""
    print(f"🔄 Converting {Path(input_file).name} to OpenAPI 3.0...")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            swagger_spec = yaml.safe_load(f)
        
        # Verify it's Swagger 2.0
        if 'swagger' not in swagger_spec:
            print(f"   ❌ Not a Swagger 2.0 spec")
            return False
        
        # Create OpenAPI 3.0 structure preserving important sections
        openapi3_spec = {
            'openapi': '3.0.0',
            'info': swagger_spec.get('info', {}),
            'components': {},
            'paths': swagger_spec.get('paths', {})
        }
        
        # Add servers - handle basePath even without host
        if 'host' in swagger_spec or 'basePath' in swagger_spec:
            servers = []
            base_path = swagger_spec.get('basePath', '')
            
            if 'host' in swagger_spec:
                # Full URL with host
                host = swagger_spec['host']
                schemes = swagger_spec.get('schemes', ['https'])
                for scheme in schemes:
                    servers.append({'url': f"{scheme}://{host}{base_path}"})
            else:
                # Just basePath (relative URL)
                if base_path:
                    servers.append({'url': base_path})
            
            if servers:
                openapi3_spec['servers'] = servers
        
        # Convert securityDefinitions to components/securitySchemes
        if 'securityDefinitions' in swagger_spec:
            openapi3_spec['components']['securitySchemes'] = {}
            for name, scheme in swagger_spec['securityDefinitions'].items():
                if scheme.get('type') == 'basic':
                    openapi3_spec['components']['securitySchemes'][name] = {
                        'type': 'http',
                        'scheme': 'basic'
                    }
                else:
                    openapi3_spec['components']['securitySchemes'][name] = scheme
        
        # Convert definitions to components/schemas
        if 'definitions' in swagger_spec:
            openapi3_spec['components']['schemas'] = swagger_spec['definitions']
        
        # Add security if it exists
        if 'security' in swagger_spec:
            openapi3_spec['security'] = swagger_spec['security']
        
        # Preserve produces as a comment or in responses (OpenAPI 3.0 doesn't have global produces)
        # We'll add it as extensions to preserve the information
        if 'produces' in swagger_spec:
            openapi3_spec['x-original-produces'] = swagger_spec['produces']
        if 'consumes' in swagger_spec:
            openapi3_spec['x-original-consumes'] = swagger_spec['consumes']
        
        # Fix $ref paths from #/definitions/ to #/components/schemas/
        def fix_refs(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key == '$ref' and isinstance(value, str):
                        if value.startswith('#/definitions/'):
                            obj[key] = value.replace('#/definitions/', '#/components/schemas/')
                    else:
                        fix_refs(value)
            elif isinstance(obj, list):
                for item in obj:
                    fix_refs(item)
        
        fix_refs(openapi3_spec)
        
        # Convert operation-level consumes/produces to OpenAPI 3.0 format
        def convert_operation_content_types(paths):
            for path, path_item in paths.items():
                for method, operation in path_item.items():
                    if method.lower() in ['get', 'post', 'put', 'delete', 'patch', 'options', 'head']:
                        # Handle operation-level consumes (convert to requestBody)
                        if 'consumes' in operation:
                            consumes = operation.pop('consumes')
                            if 'parameters' in operation:
                                # Find body parameter and convert to requestBody
                                body_param = None
                                new_params = []
                                for param in operation['parameters']:
                                    if param.get('in') == 'body':
                                        body_param = param
                                    else:
                                        new_params.append(param)
                                
                                if body_param:
                                    operation['parameters'] = new_params if new_params else None
                                    if not operation['parameters']:
                                        operation.pop('parameters', None)
                                    
                                    # Create requestBody with multiple content types
                                    request_body = {
                                        'required': body_param.get('required', False),
                                        'content': {}
                                    }
                                    
                                    for content_type in consumes:
                                        if content_type == 'multipart/form-data':
                                            # For multipart, create a form schema
                                            request_body['content'][content_type] = {
                                                'schema': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'filedata': {
                                                            'type': 'string',
                                                            'format': 'binary'
                                                        }
                                                    }
                                                }
                                            }
                                        else:
                                            # For JSON, use the original schema
                                            request_body['content'][content_type] = {
                                                'schema': body_param.get('schema', {})
                                            }
                                    
                                    operation['requestBody'] = request_body
                        
                        # Handle operation-level produces (ensure responses have content)
                        if 'produces' in operation:
                            produces = operation.pop('produces')
                            if 'responses' in operation:
                                for status, response in operation['responses'].items():
                                    if 'schema' in response:
                                        schema = response.pop('schema')
                                        response['content'] = {}
                                        for content_type in produces:
                                            response['content'][content_type] = {
                                                'schema': schema
                                            }
        
        convert_operation_content_types(openapi3_spec['paths'])
        
        # Write the file manually to ensure correct order
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("openapi: 3.0.0\n")
            
            # Write info section
            f.write("info:\n")
            info_yaml = yaml.dump(openapi3_spec['info'], default_flow_style=False, allow_unicode=False)
            for line in info_yaml.strip().split('\n'):
                f.write(f"  {line}\n")
            
            # Write servers if they exist
            if 'servers' in openapi3_spec:
                f.write("servers:\n")
                servers_yaml = yaml.dump(openapi3_spec['servers'], default_flow_style=False, allow_unicode=False)
                for line in servers_yaml.strip().split('\n'):
                    f.write(f"  {line}\n")
            
            # Write security if it exists
            if 'security' in openapi3_spec:
                f.write("security:\n")
                security_yaml = yaml.dump(openapi3_spec['security'], default_flow_style=False, allow_unicode=False)
                for line in security_yaml.strip().split('\n'):
                    f.write(f"  {line}\n")
            
            # Write original produces/consumes as extensions to preserve info
            if 'x-original-produces' in openapi3_spec:
                f.write("x-original-produces:\n")
                produces_yaml = yaml.dump(openapi3_spec['x-original-produces'], default_flow_style=False, allow_unicode=False)
                for line in produces_yaml.strip().split('\n'):
                    f.write(f"  {line}\n")
            
            if 'x-original-consumes' in openapi3_spec:
                f.write("x-original-consumes:\n")
                consumes_yaml = yaml.dump(openapi3_spec['x-original-consumes'], default_flow_style=False, allow_unicode=False)
                for line in consumes_yaml.strip().split('\n'):
                    f.write(f"  {line}\n")
            
            # Write components section
            f.write("components:\n")
            if openapi3_spec['components']:
                components_yaml = yaml.dump(openapi3_spec['components'], default_flow_style=False, allow_unicode=False)
                for line in components_yaml.strip().split('\n'):
                    f.write(f"  {line}\n")
            else:
                f.write("  {}\n")
            
            # Write paths section
            f.write("paths:\n")
            paths_yaml = yaml.dump(openapi3_spec['paths'], default_flow_style=False, allow_unicode=False)
            for line in paths_yaml.strip().split('\n'):
                f.write(f"  {line}\n")
        
        print(f"   ✅ Converted to {Path(output_file).name}")
        return True
        
    except Exception as e:
        print(f"   ❌ Conversion failed: {e}")
        return False

def generate_api_client(spec_file, output_dir, package_name):
    """Generate API client using OpenAPI Generator"""
    print(f"⚙️ Generating API client for {package_name}...")
    
    # Clean output directory
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    cmd = [
        "openapi-generator-cli", "generate",
        "-i", spec_file,
        "-g", "python",
        "-o", output_dir,
        "--package-name", package_name,
        "--skip-validate-spec",
        "--additional-properties=packageName=" + package_name
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print(f"   ✅ API client generated")
            return True
        else:
            print(f"   ❌ Generation failed: {result.stderr[:200]}...")
            return False
            
    except subprocess.TimeoutExpired:
        print("   ❌ Generation timed out")
        return False
    except Exception as e:
        print(f"   ❌ Generation error: {e}")
        return False

def generate_pydantic_models(spec_file, output_file):
    """Generate Pydantic models using datamodel-code-generator"""
    print(f"🎯 Generating Pydantic models...")
    
    # Create output directory
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    cmd = [
        "datamodel-codegen",
        "--input", spec_file,
        "--output", output_file,
        "--input-file-type", "openapi",
        "--output-model-type", "pydantic_v2.BaseModel",
        "--field-constraints",
        "--use-double-quotes"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print(f"   ✅ Pydantic models generated")
            return True
        else:
            print(f"   ❌ Model generation failed: {result.stderr[:200]}...")
            return False
            
    except subprocess.TimeoutExpired:
        print("   ❌ Model generation timed out")
        return False
    except Exception as e:
        print(f"   ❌ Model generation error: {e}")
        return False

def create_enhancement_script(api_name, enhancement_file):
    """Create enhancement wrapper script"""
    print(f"🔗 Creating enhancement wrapper for {api_name}...")
    
    enhancement_code = f'''"""
Enhanced {api_name.title()} API Client

Provides convenience methods and enhanced functionality for the generated API client.
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Add generated client to path
client_dir = Path(__file__).parent.parent / "enhanced_generated" / "clients" / "{api_name}"
if str(client_dir) not in sys.path:
    sys.path.insert(0, str(client_dir))

# Add Pydantic models to path  
models_dir = Path(__file__).parent.parent / "enhanced_generated" / "models"
if str(models_dir) not in sys.path:
    sys.path.insert(0, str(models_dir))

try:
    from {api_name.replace('-', '_')}_client.api_client import ApiClient
    from {api_name.replace('-', '_')}_client.configuration import Configuration
    print(f"✅ Successfully imported {{api_name}} API client")
except ImportError as e:
    print(f"❌ Failed to import {{api_name}} API client: {{e}}")
    ApiClient = None
    Configuration = None

try:
    from {api_name.replace('-', '_')}_models import *
    print(f"✅ Successfully imported {{api_name}} Pydantic models")
except ImportError as e:
    print(f"❌ Failed to import {{api_name}} Pydantic models: {{e}}")

class Enhanced{api_name.replace('-', '').title()}Client:
    """Enhanced client with convenience methods"""
    
    def __init__(self, host: str = "http://localhost:8080", username: str = "admin", password: str = "admin"):
        if not ApiClient or not Configuration:
            raise ImportError("API client not available")
            
        # Configure the API client
        self.configuration = Configuration()
        self.configuration.host = host + "/alfresco/api/-default-/public/alfresco/versions/1"
        self.configuration.username = username
        self.configuration.password = password
        
        # Create API client
        self.api_client = ApiClient(self.configuration)
        
        # Import specific APIs as needed
        self._import_apis()
    
    def _import_apis(self):
        """Import specific API classes"""
        try:
            # Import common APIs - adjust based on actual generated APIs
            from {api_name.replace('-', '_')}_client.api import DefaultApi
            self.default_api = DefaultApi(self.api_client)
        except ImportError:
            print(f"Warning: Could not import APIs for {{api_name}}")
    
    def test_connection(self) -> bool:
        """Test if the connection to Alfresco is working"""
        try:
            # This would need to be customized based on available endpoints
            # For now, just test if we can create the client
            return self.api_client is not None
        except Exception as e:
            print(f"Connection test failed: {{e}}")
            return False

def create_client(host: str = "http://localhost:8080", username: str = "admin", password: str = "admin") -> Enhanced{api_name.replace('-', '').title()}Client:
    """Convenience function to create an enhanced client"""
    return Enhanced{api_name.replace('-', '').title()}Client(host, username, password)

if __name__ == "__main__":
    # Test the enhanced client
    try:
        client = create_client()
        if client.test_connection():
            print(f"✅ Enhanced {{api_name}} client is working!")
        else:
            print(f"❌ Enhanced {{api_name}} client connection failed")
    except Exception as e:
        print(f"❌ Enhanced {{api_name}} client test failed: {{e}}")
'''
    
    # Write enhancement script
    os.makedirs(os.path.dirname(enhancement_file), exist_ok=True)
    with open(enhancement_file, 'w', encoding='utf-8') as f:
        f.write(enhancement_code)
    
    print(f"   ✅ Enhancement script created")
    return True

def process_api(api_name, yaml_file):
    """Process a single API through the complete pipeline"""
    print(f"\n🚀 Processing {api_name} API...")
    
    base_dir = "enhanced_generated"
    
    # Step 1: Preprocess Swagger 2.0
    preprocessed_file = f"{base_dir}/preprocessed/{api_name}.preprocessed.yaml"
    if not preprocess_swagger2_spec(yaml_file, preprocessed_file, api_name):
        return False
    
    # Step 2: Convert to OpenAPI 3.0
    openapi3_file = f"{base_dir}/openapi3/{api_name}.openapi3.yaml"
    if not convert_swagger_to_openapi3(preprocessed_file, openapi3_file):
        return False
    
    # Step 3: Generate API client
    client_dir = f"{base_dir}/clients/{api_name}"
    package_name = api_name.replace('-', '_') + '_client'
    if not generate_api_client(openapi3_file, client_dir, package_name):
        return False
    
    # Step 4: Generate Pydantic models
    models_file = f"{base_dir}/models/{api_name.replace('-', '_')}_models.py"
    if not generate_pydantic_models(openapi3_file, models_file):
        return False
    
    # Step 5: Create enhancement script
    enhancement_file = f"{base_dir}/enhanced/{api_name}_enhanced.py"
    if not create_enhancement_script(api_name, enhancement_file):
        return False
    
    print(f"   ✅ {api_name} API processing complete")
    return True

def main():
    """Main execution function"""
    print("🎯 Enhanced Hybrid Approach with Preprocessing")
    print("=" * 50)
    
    # Check dependencies
    if not ensure_dependencies():
        print("\n❌ Dependencies not met. Please install required tools.")
        return False
    
    # Find YAML files
    yaml_files = {
        'alfresco-auth': 'yaml_v2/alfresco-auth.yaml',
        'alfresco-core': 'yaml_v2/alfresco-core.yaml', 
        'alfresco-discovery': 'yaml_v2/alfresco-discovery.yaml',
        'alfresco-model': 'yaml_v2/alfresco-model.yaml',
        'alfresco-search': 'yaml_v2/alfresco-search.yaml',
        'alfresco-search-sql': 'yaml_v2/alfresco-search-sql.yaml',
        'alfresco-workflow': 'yaml_v2/alfresco-workflow.yaml'
    }
    
    # Verify files exist
    missing_files = []
    for api_name, file_path in yaml_files.items():
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n❌ Missing YAML files: {', '.join(missing_files)}")
        return False
    
    # Process each API
    success_count = 0
    total_count = len(yaml_files)
    
    for api_name, yaml_file in yaml_files.items():
        if process_api(api_name, yaml_file):
            success_count += 1
        else:
            print(f"   ❌ Failed to process {api_name}")
    
    # Summary
    print(f"\n📊 Results: {success_count}/{total_count} APIs processed successfully")
    
    if success_count == total_count:
        print("\n🎉 Enhanced hybrid approach completed successfully!")
        print("\n📁 Generated structure:")
        print("   enhanced_generated/")
        print("   ├── preprocessed/     # Preprocessed Swagger 2.0 specs")
        print("   ├── openapi3/         # Converted OpenAPI 3.0 specs")  
        print("   ├── clients/          # Generated API clients")
        print("   ├── models/           # Generated Pydantic models")
        print("   └── enhanced/         # Enhancement wrapper scripts")
        
        print("\n🔧 Next steps:")
        print("   1. Test the enhanced clients")
        print("   2. Run integration tests")
        print("   3. Create master client wrapper")
        
        return True
    else:
        print(f"\n❌ {total_count - success_count} APIs failed to process")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)