# alfresco_auth_client.AuthenticationApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/authentication/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ticket**](AuthenticationApi.md#create_ticket) | **POST** /tickets | Create ticket (login)
[**delete_ticket**](AuthenticationApi.md#delete_ticket) | **DELETE** /tickets/-me- | Delete ticket (logout)
[**validate_ticket**](AuthenticationApi.md#validate_ticket) | **GET** /tickets/-me- | Validate ticket


# **create_ticket**
> TicketEntry create_ticket(ticket_body)

Create ticket (login)

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Logs in and returns the new authentication ticket.

The userId and password properties are mandatory in the request body. For example:
```JSON
{
    "userId": "jbloggs",
    "password": "password"
}
```
To use the ticket in future requests you should pass it in the request header.
For example using Javascript:
  ```Javascript
    request.setRequestHeader ("Authorization", "Basic " + btoa(ticket));
  ```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_auth_client
from alfresco_auth_client.models.ticket_body import TicketBody
from alfresco_auth_client.models.ticket_entry import TicketEntry
from alfresco_auth_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/authentication/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_auth_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/authentication/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_auth_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_auth_client.AuthenticationApi(api_client)
    ticket_body = alfresco_auth_client.TicketBody() # TicketBody | The user credential.

    try:
        # Create ticket (login)
        api_response = api_instance.create_ticket(ticket_body)
        print("The response of AuthenticationApi->create_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->create_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_body** | [**TicketBody**](TicketBody.md)| The user credential. | 

### Return type

[**TicketEntry**](TicketEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | **userId** or **password** is not provided  |  -  |
**403** | Login failed |  -  |
**501** | SAML is enabled and enforced |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ticket**
> delete_ticket()

Delete ticket (logout)

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Deletes logged in ticket (logout).


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_auth_client
from alfresco_auth_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/authentication/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_auth_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/authentication/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_auth_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_auth_client.AuthenticationApi(api_client)

    try:
        # Delete ticket (logout)
        api_instance.delete_ticket()
    except Exception as e:
        print("Exception when calling AuthenticationApi->delete_ticket: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |
**400** | URL path does not include **-me-** or the ticket is not provided by the Authorization header |  -  |
**404** | Status of the user has changed (for example, the user is locked or the account is disabled) or the ticket has expired |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_ticket**
> ValidTicketEntry validate_ticket()

Validate ticket

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Validates the specified ticket (derived from Authorization header) is still valid.

For example, you can pass the Authorization request header using Javascript:
  ```Javascript
    request.setRequestHeader ("Authorization", "Basic " + btoa(ticket));
  ```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_auth_client
from alfresco_auth_client.models.valid_ticket_entry import ValidTicketEntry
from alfresco_auth_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/authentication/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_auth_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/authentication/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_auth_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_auth_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_auth_client.AuthenticationApi(api_client)

    try:
        # Validate ticket
        api_response = api_instance.validate_ticket()
        print("The response of AuthenticationApi->validate_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->validate_ticket: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ValidTicketEntry**](ValidTicketEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | URL path does not include **-me-** or the ticket is not provided by the Authorization header |  -  |
**401** | Authentication failed |  -  |
**404** | The request is authorized correctly but the status of the user (of the supplied ticket) has changed (for example, the user is locked or the account is disabled) or the ticket has expired |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

