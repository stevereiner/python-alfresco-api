from alfresco_search-sql import Search-sqlClient

def main():
    # Initialize the client
    client = Search-sqlClient(
        base_url="http://your-alfresco-instance/alfresco",
        username="your-username",
        password="your-password"
    )

    # Example API calls
    # Alfresco Insight Engine SQL Passthrough
    response = client.search()
    print(f'Response: {response}')


if __name__ == "__main__":
    main()
