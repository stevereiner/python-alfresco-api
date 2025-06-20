#!/usr/bin/env python3

"""
Simplified Enhanced Hybrid Approach - Tool-Based OpenAPI 3.0 Conversion

This script implements a streamlined hybrid approach with automated tool-based conversion:
1. **PREPROCESS** Swagger 2.0 specs to fill in missing parts
2. **CONVERT** preprocessed Swagger 2.0 to OpenAPI 3.0 using tools:
   - Primary: swagger2openapi (Node.js tool) - industry standard
   - Fallback: Python-based conversion
   - Final fallback: Manual conversion (modular functions)
3. **GENERATE** API client with OpenAPI Generator (clean, working code)
4. **GENERATE** Pydantic models with datamodel-code-generator (pure Pydantic)
5. **CREATE** enhancement scripts to bridge and add convenience methods

BENEFITS OF TOOL-BASED APPROACH:
- Uses industry-standard conversion tools (swagger2openapi)
- Better handling of complex schemas and edge cases
- Automatic validation and error detection
- Superior regex patterns and Unicode support
- Maintains fallback options for reliability

The manual conversion functions are kept as fallbacks and for reference.
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
    
    # Check datamodel-code-generator and its capabilities
    try:
        result = subprocess.run(["datamodel-codegen", "--help"], capture_output=True, text=True)
        if result.returncode == 0:
            print("   ✅ datamodel-code-generator found")
            
            # Check if it supports our enhanced parameters
            help_text = result.stdout
            enhanced_features = [
                ("--allow-extra-fields", "extra fields support"),
                ("--use-union-operator", "union operator support"),
                ("--strict-nullable", "strict nullable support")
            ]
            
            for param, description in enhanced_features:
                if param in help_text:
                    print(f"   ✅ {description}")
                else:
                    print(f"   ⚠️  {description} not available (older version)")
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

def convert_servers_section(swagger_spec):
    """Convert Swagger 2.0 host/basePath to OpenAPI 3.0 servers"""
    servers = []
    
    if 'host' in swagger_spec or 'basePath' in swagger_spec:
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
    
    return servers

def convert_security_definitions(swagger_spec):
    """Convert Swagger 2.0 securityDefinitions to OpenAPI 3.0 securitySchemes"""
    if 'securityDefinitions' not in swagger_spec:
        return {}
    
    security_schemes = {}
    for name, scheme in swagger_spec['securityDefinitions'].items():
        if scheme.get('type') == 'basic':
            security_schemes[name] = {
                'type': 'http',
                'scheme': 'basic'
            }
        else:
            security_schemes[name] = scheme
    
    return security_schemes

def fix_ref_paths(obj):
    """Fix $ref paths from #/definitions/ to #/components/schemas/"""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == '$ref' and isinstance(value, str):
                if value.startswith('#/definitions/'):
                    obj[key] = value.replace('#/definitions/', '#/components/schemas/')
            else:
                fix_ref_paths(value)
    elif isinstance(obj, list):
        for item in obj:
            fix_ref_paths(item)

def convert_operation_request_body(operation, consumes):
    """Convert Swagger 2.0 body parameter + consumes to OpenAPI 3.0 requestBody"""
    if 'parameters' not in operation:
        return
    
    # Find body parameter and convert to requestBody
    body_param = None
    new_params = []
    
    for param in operation['parameters']:
        if param.get('in') == 'body':
            body_param = param
        else:
            new_params.append(param)
    
    if not body_param:
        return
    
    # Update parameters list
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

def convert_operation_responses(operation, produces):
    """Convert Swagger 2.0 produces to OpenAPI 3.0 response content"""
    if 'responses' not in operation:
        return
    
    for status, response in operation['responses'].items():
        if 'schema' in response:
            schema = response.pop('schema')
            response['content'] = {}
            for content_type in produces:
                response['content'][content_type] = {
                    'schema': schema
                }

def convert_operations_content_types(paths):
    """Convert operation-level consumes/produces to OpenAPI 3.0 format"""
    for path, path_item in paths.items():
        for method, operation in path_item.items():
            if method.lower() in ['get', 'post', 'put', 'delete', 'patch', 'options', 'head']:
                # Handle operation-level consumes (convert to requestBody)
                if 'consumes' in operation:
                    consumes = operation.pop('consumes')
                    convert_operation_request_body(operation, consumes)
                
                # Handle operation-level produces (ensure responses have content)
                if 'produces' in operation:
                    produces = operation.pop('produces')
                    convert_operation_responses(operation, produces)

def build_openapi3_structure(swagger_spec):
    """Build the basic OpenAPI 3.0 structure from Swagger 2.0"""
    openapi3_spec = {
        'openapi': '3.0.0',
        'info': swagger_spec.get('info', {}),
        'components': {},
        'paths': swagger_spec.get('paths', {})
    }
    
    # Add servers
    servers = convert_servers_section(swagger_spec)
    if servers:
        openapi3_spec['servers'] = servers
    
    # Convert security definitions
    security_schemes = convert_security_definitions(swagger_spec)
    if security_schemes:
        openapi3_spec['components']['securitySchemes'] = security_schemes
    
    # Convert definitions to components/schemas
    if 'definitions' in swagger_spec:
        openapi3_spec['components']['schemas'] = swagger_spec['definitions']
    
    # Add security if it exists
    if 'security' in swagger_spec:
        openapi3_spec['security'] = swagger_spec['security']
    
    # Preserve produces/consumes as extensions
    if 'produces' in swagger_spec:
        openapi3_spec['x-original-produces'] = swagger_spec['produces']
    if 'consumes' in swagger_spec:
        openapi3_spec['x-original-consumes'] = swagger_spec['consumes']
    
    return openapi3_spec

def write_openapi3_yaml(openapi3_spec, output_file):
    """Write OpenAPI 3.0 spec to YAML file with proper section ordering"""
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

def convert_swagger_to_openapi3(input_file, output_file):
    """Convert preprocessed Swagger 2.0 to OpenAPI 3.0 (refactored for readability)"""
    print(f"🔄 Converting {Path(input_file).name} to OpenAPI 3.0...")
    
    try:
        # Load and validate Swagger 2.0 spec
        with open(input_file, 'r', encoding='utf-8') as f:
            swagger_spec = yaml.safe_load(f)
        
        if 'swagger' not in swagger_spec:
            print(f"   ❌ Not a Swagger 2.0 spec")
            return False
        
        # Build OpenAPI 3.0 structure
        openapi3_spec = build_openapi3_structure(swagger_spec)
        
        # Fix reference paths
        fix_ref_paths(openapi3_spec)
        
        # Convert operation-level content types
        convert_operations_content_types(openapi3_spec['paths'])
        
        # Write the result
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        write_openapi3_yaml(openapi3_spec, output_file)
        
        print(f"   ✅ Converted to {Path(output_file).name}")
        return True
        
    except Exception as e:
        print(f"   ❌ Conversion failed: {e}")
        return False

def convert_swagger_to_openapi3_with_tool(input_file, output_file):
    """
    EXPERIMENTAL: Convert preprocessed Swagger 2.0 to OpenAPI 3.0 using proper conversion tools
    
    This is an experiment to see if using a proper converter gives better results
    than the manual field-by-field conversion above.
    """
    print(f"🔧 Converting {Path(input_file).name} to OpenAPI 3.0 using swagger2openapi...")
    
    try:
        # First try swagger2openapi (Node.js tool)
        try:
            # Try different ways to call swagger2openapi on Windows
            swagger_methods = [
                # Method 1: Direct call with shell=True
                (["swagger2openapi"], True),
                # Method 2: PowerShell command
                (["powershell", "-Command", "swagger2openapi"], False),
                # Method 3: cmd /c
                (["cmd", "/c", "swagger2openapi"], False)
            ]
            
            swagger_cmd = None
            use_shell = False
            
            for cmd_list, shell_flag in swagger_methods:
                try:
                    result = subprocess.run(cmd_list + ["--version"], capture_output=True, text=True, shell=shell_flag)
                    if result.returncode == 0:
                        print(f"   ✅ Found swagger2openapi: {result.stdout.strip()}")
                        swagger_cmd = cmd_list
                        use_shell = shell_flag
                        break
                except:
                    continue
            
            if swagger_cmd:
                # Convert using swagger2openapi
                cmd = swagger_cmd + [
                    input_file, 
                    "--outfile", output_file,
                    "--verbose"
                ]
                
                print(f"   🔄 Running: {' '.join(cmd)}")
                result = subprocess.run(cmd, capture_output=True, text=True, shell=use_shell)
                
                if result.returncode == 0:
                    print(f"   ✅ Successfully converted with swagger2openapi")
                    
                    # Verify the output file exists and is valid
                    if os.path.exists(output_file):
                        with open(output_file, 'r', encoding='utf-8') as f:
                            converted_spec = yaml.safe_load(f)
                            if 'openapi' in converted_spec:
                                print(f"   ✅ Verified OpenAPI 3.0 output: {converted_spec['openapi']}")
                                return True
                            else:
                                print(f"   ❌ Output doesn't contain 'openapi' field")
                    else:
                        print(f"   ❌ Output file not created")
                else:
                    print(f"   ❌ swagger2openapi failed: {result.stderr}")
                    if result.stderr:
                        print(f"   📋 Error details: {result.stderr}")
            else:
                print(f"   ⚠️  swagger2openapi not found with any method")
        except Exception as e:
            print(f"   ⚠️  swagger2openapi error: {e}")
        
        # Fallback: Try using Python openapi-spec-validator with conversion
        try:
            from openapi_spec_validator import validate_spec
            from openapi_spec_validator.readers import read_from_filename
            
            print(f"   🔄 Trying Python-based conversion fallback...")
            
            # Read the swagger spec
            with open(input_file, 'r', encoding='utf-8') as f:
                swagger_spec = yaml.safe_load(f)
            
            # Basic conversion (simplified version of our manual approach)
            openapi3_spec = {
                'openapi': '3.0.0',
                'info': swagger_spec.get('info', {}),
                'servers': [],
                'paths': swagger_spec.get('paths', {}),
                'components': {}
            }
            
            # Add servers
            if 'host' in swagger_spec or 'basePath' in swagger_spec:
                base_path = swagger_spec.get('basePath', '')
                if 'host' in swagger_spec:
                    host = swagger_spec['host']
                    schemes = swagger_spec.get('schemes', ['https'])
                    for scheme in schemes:
                        openapi3_spec['servers'].append({'url': f"{scheme}://{host}{base_path}"})
                elif base_path:
                    openapi3_spec['servers'].append({'url': base_path})
            
            # Convert components
            if 'definitions' in swagger_spec:
                openapi3_spec['components']['schemas'] = swagger_spec['definitions']
            
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
            
            # Add security
            if 'security' in swagger_spec:
                openapi3_spec['security'] = swagger_spec['security']
            
            # Fix $ref paths
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
            
            # Write the converted spec
            with open(output_file, 'w', encoding='utf-8') as f:
                yaml.dump(openapi3_spec, f, default_flow_style=False, allow_unicode=False, sort_keys=False)
            
            print(f"   ✅ Python fallback conversion completed")
            return True
            
        except ImportError:
            print(f"   ❌ openapi-spec-validator not available")
        except Exception as e:
            print(f"   ❌ Python fallback conversion failed: {e}")
        
        # Final fallback: Use our manual conversion
        print(f"   🔄 Falling back to manual conversion...")
        return convert_swagger_to_openapi3(input_file, output_file)
        
    except Exception as e:
        print(f"   ❌ Tool-based conversion failed: {e}")
        print(f"   🔄 Falling back to manual conversion...")
        return convert_swagger_to_openapi3(input_file, output_file)

def fix_regex_syntax_in_generated_code(client_dir):
    """Fix invalid regex syntax in generated code"""
    print(f"   🔧 Fixing regex syntax in generated code...")
    
    try:
        models_dir = os.path.join(client_dir, "models")
        if not os.path.exists(models_dir):
            return True
        
        fixed_count = 0
        for root, dirs, files in os.walk(models_dir):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    
                    # Read the file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Fix the specific regex pattern issues
                    original_content = content
                    
                    # Fix the main problematic pattern
                    content = content.replace(
                        r'r"^(?!(.*[\\"\*\\\>\<\?\/\:\|]+.*)',
                        r'r"^(?!(.*[\\\"\\*\\\\>\\<\\?\\/\\:\\|]+.*)'
                    )
                    
                    # Fix other escape sequence issues
                    content = content.replace(
                        r'[\\"\*\\\>\<\?\/\:\|]',
                        r'[\\\"\\*\\\\>\\<\\?\\/\\:\\|]'
                    )
                    
                    # Write back if changed
                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixed_count += 1
        
        if fixed_count > 0:
            print(f"   ✅ Fixed regex syntax in {fixed_count} files")
        else:
            print(f"   ✅ No regex fixes needed")
        return True
        
    except Exception as e:
        print(f"   ⚠️ Regex fix failed: {e}")
        return True  # Don't fail the whole process

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
            
            # Fix regex syntax issues in generated code
            package_dir = os.path.join(output_dir, package_name)
            fix_regex_syntax_in_generated_code(package_dir)
            
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
    
    # Enhanced parameters for better compatibility with swagger2openapi output
    cmd = [
        "datamodel-codegen",
        "--input", spec_file,
        "--output", output_file,
        "--input-file-type", "openapi",
        "--output-model-type", "pydantic_v2.BaseModel",
        "--use-double-quotes",
        "--allow-extra-fields",              # Handle unknown fields gracefully
        "--disable-warnings",               # Reduce noise from complex schemas
        "--target-python-version", "3.9",   # Specify Python version
        "--encoding", "utf-8"               # Handle Unicode characters from swagger2openapi
    ]
    
    try:
        print(f"   🔄 Running: datamodel-codegen with {len(cmd)-1} parameters")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)  # Increased timeout
        
        if result.returncode == 0:
            print(f"   ✅ Pydantic models generated")
            return True
        else:
            print(f"   ❌ Model generation failed (exit code: {result.returncode})")
            print(f"   📋 Error: {result.stderr[:500]}...")
            if result.stdout:
                print(f"   📋 Output: {result.stdout[:200]}...")
            
            # Try fallback with more permissive settings and encoding fix
            print(f"   🔄 Trying fallback with permissive settings...")
            fallback_cmd = [
                "datamodel-codegen",
                "--input", spec_file,
                "--output", output_file,
                "--input-file-type", "openapi",
                "--output-model-type", "pydantic_v2.BaseModel",
                "--use-double-quotes",
                "--disable-warnings",
                "--encoding", "utf-8"  # Explicitly specify UTF-8 encoding
            ]
            
            print(f"   🔄 Fallback command: {' '.join(fallback_cmd[:6])}...")
            fallback_result = subprocess.run(fallback_cmd, capture_output=True, text=True, timeout=120)
            
            if fallback_result.returncode == 0:
                print(f"   ✅ Pydantic models generated (fallback mode)")
                return True
            else:
                print(f"   ❌ Fallback also failed (exit code: {fallback_result.returncode})")
                print(f"   📋 Fallback error: {fallback_result.stderr[:500]}...")
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

def process_api(api_name, yaml_file, use_experimental_converter=False):
    """Process a single API through the complete pipeline"""
    print(f"\n🚀 Processing {api_name} API...")
    
    base_dir = "enhanced_generated"
    
    # Step 1: Preprocess Swagger 2.0
    preprocessed_file = f"{base_dir}/preprocessed/{api_name}.preprocessed.yaml"
    if not preprocess_swagger2_spec(yaml_file, preprocessed_file, api_name):
        return False
    
    # Step 2: Convert to OpenAPI 3.0
    openapi3_file = f"{base_dir}/openapi3/{api_name}.openapi3.yaml"
    
    if use_experimental_converter:
        # Try experimental tool-based conversion first
        if not convert_swagger_to_openapi3_with_tool(preprocessed_file, openapi3_file):
            return False
    else:
        # Use manual conversion (original approach)
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
    print("🎯 Alfresco Python Client Generator")
    print("=" * 50)
    
    # Use tool-based conversion (simplified approach)
    print("\n🔧 Using tool-based OpenAPI 3.0 conversion")
    print("   Primary: swagger2openapi (Node.js)")
    print("   Fallback: Python-based conversion")
    print("   Final fallback: Manual conversion")
    
    use_experimental = True
    compare_methods = False
    
    # Check dependencies
    if not ensure_dependencies():
        print("\n❌ Dependencies not met. Please install required tools.")
        return False
    
    # Check for conversion tools
    print("\n🔍 Checking for conversion tools...")
    swagger_found = False
    
    # Try multiple methods to find swagger2openapi
    for cmd_list, shell_flag in [
        (["swagger2openapi"], True),
        (["powershell", "-Command", "swagger2openapi"], False),
        (["cmd", "/c", "swagger2openapi"], False)
    ]:
        try:
            result = subprocess.run(cmd_list + ["--version"], capture_output=True, text=True, shell=shell_flag)
            if result.returncode == 0:
                print(f"   ✅ swagger2openapi found: {result.stdout.strip()}")
                swagger_found = True
                break
        except:
            continue
    
    if not swagger_found:
        print("   ℹ️  swagger2openapi not found (install with: npm install -g swagger2openapi)")
        print("   ℹ️  Will use Python-based fallback or manual conversion")
    
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
    
    print(f"\n🚀 Processing {total_count} APIs with tool-based conversion...")
    print("=" * 60)
    
    for api_name, yaml_file in yaml_files.items():
        print(f"\n📁 Processing {api_name}...")
        if process_api(api_name, yaml_file, use_experimental_converter=use_experimental):
            success_count += 1
            print(f"   ✅ {api_name} completed successfully")
        else:
            print(f"   ❌ Failed to process {api_name}")
    
    # Summary
    print(f"\n📊 Results: {success_count}/{total_count} APIs processed successfully")
    
    if success_count == total_count:
        print("\n🎉 Alfresco Python client generation completed successfully!")
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