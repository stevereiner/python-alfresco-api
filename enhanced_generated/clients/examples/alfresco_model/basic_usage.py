from alfresco_model import ModelClient

def main():
    # Initialize the client
    client = ModelClient(
        base_url="http://your-alfresco-instance/alfresco",
        username="your-username",
        password="your-password"
    )

    # Example API calls
    # List aspects
    response = client.listAspects()
    print(f'Response: {response}')

    # Get an aspect
    response = client.getAspect()
    print(f'Response: {response}')

    # List types
    response = client.listTypes()
    print(f'Response: {response}')

    # Get a type
    response = client.getType()
    print(f'Response: {response}')


if __name__ == "__main__":
    main()
