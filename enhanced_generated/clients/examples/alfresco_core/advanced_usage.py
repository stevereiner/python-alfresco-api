from alfresco_core import CoreClient
import json

def main():
    # Initialize the client with custom configuration
    client = CoreClient(
        base_url="http://your-alfresco-instance/alfresco",
        username="your-username",
        password="your-password",
        verify_ssl=False  # For development only
    )

    # Example of error handling
    try:
        # Your API calls here
        pass
    except Exception as e:
        print(f"Error: {e}")

    # Example of working with responses
    try:
        response = client.some_api_call()
        data = response.json()
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error processing response: {e}")

if __name__ == "__main__":
    main()
