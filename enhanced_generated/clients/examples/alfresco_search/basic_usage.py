from alfresco_search import SearchClient

def main():
    # Initialize the client
    client = SearchClient(
        base_url="http://your-alfresco-instance/alfresco",
        username="your-username",
        password="your-password"
    )

    # Example API calls
    # Searches Alfresco
    response = client.search()
    print(f'Response: {response}')


if __name__ == "__main__":
    main()
