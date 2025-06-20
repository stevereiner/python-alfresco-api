from alfresco_discovery import DiscoveryClient

def main():
    # Initialize the client
    client = DiscoveryClient(
        base_url="http://your-alfresco-instance/alfresco",
        username="your-username",
        password="your-password"
    )

    # Example API calls
    # Get repository information
    response = client.getRepositoryInformation()
    print(f'Response: {response}')


if __name__ == "__main__":
    main()
