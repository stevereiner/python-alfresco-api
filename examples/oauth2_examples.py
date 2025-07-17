#!/usr/bin/env python3
"""
OAuth2 Examples - Python Alfresco API v1.0

This example demonstrates how to use OAuth2 authentication with the Python Alfresco API.
It covers multiple scenarios: local testing, real OAuth2 providers, and enterprise setups.

SETUP REQUIREMENTS:

1. Environment Variables (Create .env file):
   OAUTH2_CLIENT_ID=your-client-id
   OAUTH2_CLIENT_SECRET=your-client-secret
   OAUTH2_TOKEN_ENDPOINT=your-token-endpoint
   ALFRESCO_URL=http://localhost:8080

2. Or use sample-oauth2-test.env as template

SUPPORTED OAUTH2 PROVIDERS:
- Keycloak (Local & Enterprise)
- Azure AD
- AWS Cognito
- Google OAuth2
- Okta
- Alfresco Enterprise (with OAuth2 support)
"""

import os
import asyncio
from python_alfresco_api import OAuth2AuthUtil, ClientFactory


def example_1_basic_oauth2():
    """Example 1: Basic OAuth2 client credentials flow."""
    print("📋 Example 1: Basic OAuth2 Setup")
    print("-" * 40)
    
    # Direct configuration (for testing)
    oauth_util = OAuth2AuthUtil(
        base_url="http://localhost:8080",
        client_id="alfresco-client",
        client_secret="your-client-secret",
        token_endpoint="http://localhost:8180/auth/realms/alfresco/protocol/openid-connect/token",
        grant_type="client_credentials",
        scope="read write",
        load_env=False  # Don't load from environment
    )
    
    print(f"   🆔 Client ID: {oauth_util.client_id}")
    print(f"   🔗 Token Endpoint: {oauth_util.token_endpoint}")
    print(f"   📋 Grant Type: {oauth_util.grant_type}")
    
    return oauth_util


def example_2_environment_oauth2():
    """Example 2: OAuth2 with environment configuration."""
    print("\n📋 Example 2: Environment-Based OAuth2")
    print("-" * 40)
    
    # Load from environment variables
    oauth_util = OAuth2AuthUtil(
        base_url="http://localhost:8080",
        client_id="",  # Will be loaded from environment
        load_env=True
    )
    
    config = oauth_util.get_config_info()
    print(f"   🆔 Client ID: {config.get('client_id', 'Not set')}")
    print(f"   🔗 Token Endpoint: {config.get('token_endpoint', 'Not set')}")
    print(f"   📋 Grant Type: {config.get('grant_type')}")
    print(f"   🔑 Has Token: {config.get('has_access_token', False)}")
    
    return oauth_util


def example_3_oauth2_factory():
    """Example 3: Using OAuth2 with ClientFactory."""
    print("\n📋 Example 3: OAuth2 with ClientFactory")
    print("-" * 40)
    
    # Create OAuth2 auth utility
    oauth_util = OAuth2AuthUtil(
        base_url="http://localhost:8080",
        client_id="factory-example",
        client_secret="factory-secret",
        load_env=False
    )
    
    # Simulate successful authentication (in real usage, call authenticate())
    oauth_util.access_token = "example_access_token_12345"
    oauth_util._authenticated = True
    
    # Create factory with OAuth2 auth
    factory = ClientFactory(auth_util=oauth_util)
    
    # Create clients
    discovery_client = factory.create_discovery_client()
    core_client = factory.create_core_client()
    search_client = factory.create_search_client()
    
    print("   ✅ Factory created with OAuth2 authentication")
    print("   🔍 Discovery client ready")
    print("   📄 Core client ready")
    print("   🔎 Search client ready")
    
    return factory


async def example_4_real_authentication():
    """Example 4: Real OAuth2 authentication flow."""
    print("\n📋 Example 4: Real OAuth2 Authentication")
    print("-" * 40)
    
    # Check if we have real OAuth2 configuration
    required_env = ['OAUTH2_CLIENT_ID', 'OAUTH2_CLIENT_SECRET', 'OAUTH2_TOKEN_ENDPOINT']
    missing_env = [var for var in required_env if not os.getenv(var)]
    
    if missing_env:
        print(f"   ⚠️ Missing environment variables: {', '.join(missing_env)}")
        print("   💡 This example requires real OAuth2 configuration")
        print("   📝 Create .env file with your OAuth2 settings")
        return None
    
    # Create OAuth2 util with environment config
    oauth_util = OAuth2AuthUtil(
        base_url=os.getenv('ALFRESCO_URL', 'http://localhost:8080'),
        client_id="",  # Will be loaded from environment
        load_env=True
    )
    
    print("   🔄 Attempting OAuth2 authentication...")
    
    try:
        # Perform real authentication
        success = await oauth_util.authenticate()
        
        if success:
            print("   ✅ OAuth2 authentication successful!")
            print(f"   🔑 Access token obtained (length: {len(oauth_util.access_token)})")
            
            # Test with Alfresco API
            factory = ClientFactory(auth_util=oauth_util)
            discovery_client = factory.create_discovery_client()
            
            try:
                # This would make a real API call
                print("   🧪 Testing API call with OAuth2 token...")
                # repo_info = discovery_client.get_repository_info()
                print("   ℹ️ API call skipped in example (would require live server)")
            except Exception as e:
                print(f"   ⚠️ API call failed: {e}")
            
            return oauth_util
        else:
            print("   ❌ OAuth2 authentication failed")
            return None
            
    except Exception as e:
        print(f"   ❌ OAuth2 authentication error: {e}")
        return None


def example_5_oauth2_providers():
    """Example 5: Different OAuth2 provider configurations."""
    print("\n📋 Example 5: OAuth2 Provider Examples")
    print("-" * 40)
    
    providers = {
        "Keycloak (Local)": {
            "token_endpoint": "http://localhost:8180/auth/realms/alfresco/protocol/openid-connect/token",
            "setup": "docker run -p 8180:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:latest start-dev"
        },
        "Azure AD": {
            "token_endpoint": "https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/token",
            "setup": "Register app in Azure Portal, get client credentials"
        },
        "AWS Cognito": {
            "token_endpoint": "https://{domain}.auth.{region}.amazoncognito.com/oauth2/token",
            "setup": "Create Cognito User Pool, configure app client"
        },
        "Google OAuth2": {
            "token_endpoint": "https://oauth2.googleapis.com/token",
            "setup": "Create project in Google Cloud Console, enable APIs"
        },
        "Okta": {
            "token_endpoint": "https://{domain}.okta.com/oauth2/default/v1/token",
            "setup": "Create Okta developer account, register application"
        }
    }
    
    for provider, config in providers.items():
        print(f"\n   🔧 {provider}")
        print(f"      Token URL: {config['token_endpoint']}")
        print(f"      Setup: {config['setup']}")
    
    print("\n   💡 For any provider, set these environment variables:")
    print("      OAUTH2_CLIENT_ID=your-client-id")
    print("      OAUTH2_CLIENT_SECRET=your-client-secret")
    print("      OAUTH2_TOKEN_ENDPOINT=provider-token-url")


def example_6_oauth2_debugging():
    """Example 6: OAuth2 debugging and troubleshooting."""
    print("\n📋 Example 6: OAuth2 Debugging")
    print("-" * 40)
    
    oauth_util = OAuth2AuthUtil(
        base_url="http://localhost:8080",
        client_id="debug-client",
        client_secret="debug-secret",
        token_endpoint="http://debug-oauth2/token",
        scope="read write admin",
        load_env=False
    )
    
    # Get configuration info (safe for logging)
    config = oauth_util.get_config_info()
    
    print("   📊 OAuth2 Configuration:")
    for key, value in config.items():
        print(f"      {key}: {value}")
    
    # Check authentication status
    print(f"\n   🔒 Authentication Status:")
    print(f"      Is Authenticated: {oauth_util.is_authenticated()}")
    print(f"      Has Access Token: {bool(oauth_util.access_token)}")
    print(f"      Has Refresh Token: {bool(oauth_util.refresh_token)}")
    
    # Test headers generation
    headers = oauth_util.get_auth_headers()
    print(f"\n   📋 Auth Headers: {len(headers)} headers")
    if headers:
        for key, value in headers.items():
            # Mask sensitive data
            if "Authorization" in key:
                print(f"      {key}: {value[:20]}..." if len(value) > 20 else value)
            else:
                print(f"      {key}: {value}")


async def main():
    """Run all OAuth2 examples."""
    print("🚀 Python Alfresco API v1.0 - OAuth2 Examples")
    print("=" * 55)
    
    # Basic examples (always work)
    example_1_basic_oauth2()
    example_2_environment_oauth2()
    example_3_oauth2_factory()
    
    # Real authentication (requires configuration)
    await example_4_real_authentication()
    
    # Provider information
    example_5_oauth2_providers()
    
    # Debugging
    example_6_oauth2_debugging()
    
    print("\n🎉 OAuth2 Examples Complete!")
    print("\n📚 Next Steps:")
    print("   1. Choose your OAuth2 provider (Keycloak, Azure AD, etc.)")
    print("   2. Set up environment variables with your credentials")
    print("   3. Test authentication with: python tests/test_oauth2_simple.py")
    print("   4. Use OAuth2AuthUtil in your applications")
    print("\n📖 Documentation: Copy sample-oauth2-test.env to .env and configure")


if __name__ == "__main__":
    asyncio.run(main()) 