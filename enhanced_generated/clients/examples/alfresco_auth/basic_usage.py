from alfresco_auth import AuthClient

def main():
    # Initialize the client
    client = AuthClient(
        base_url="http://your-alfresco-instance/alfresco",
        username="your-username",
        password="your-password"
    )

    # Example API calls
    # Create ticket (login)
    response = client.createTicket()
    print(f'Response: {response}')

    # Validate ticket
    response = client.validateTicket()
    print(f'Response: {response}')

    # Delete ticket (logout)
    response = client.deleteTicket()
    print(f'Response: {response}')


if __name__ == "__main__":
    main()
