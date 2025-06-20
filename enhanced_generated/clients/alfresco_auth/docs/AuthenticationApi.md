# alfresco_auth.AuthenticationApi

All URIs are relative to */alfresco/api/-default-/public/authentication/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ticket**](AuthenticationApi.md#create_ticket) | **POST** /tickets | Create ticket (login)
[**delete_ticket**](AuthenticationApi.md#delete_ticket) | **DELETE** /tickets/-me- | Delete ticket (logout)
[**validate_ticket**](AuthenticationApi.md#validate_ticket) | **GET** /tickets/-me- | Validate ticket

# **create_ticket**
> TicketEntry create_ticket(body)

Create ticket (login)

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Logs in and returns the new authentication ticket.  The userId and password properties are mandatory in the request body. For example: ```JSON {     \"userId\": \"jbloggs\",     \"password\": \"password\" } ``` To use the ticket in future requests you should pass it in the request header. For example using Javascript:   ```Javascript     request.setRequestHeader (\"Authorization\", \"Basic \" + btoa(ticket));   ``` 

### Example
```python
from __future__ import print_function
import time
import alfresco_auth
from alfresco_auth.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_auth.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_auth.AuthenticationApi(alfresco_auth.ApiClient(configuration))
body = alfresco_auth.TicketBody() # TicketBody | The user credential.

try:
    # Create ticket (login)
    api_response = api_instance.create_ticket(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->create_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TicketBody**](TicketBody.md)| The user credential. | 

### Return type

[**TicketEntry**](TicketEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ticket**
> delete_ticket()

Delete ticket (logout)

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Deletes logged in ticket (logout). 

### Example
```python
from __future__ import print_function
import time
import alfresco_auth
from alfresco_auth.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_auth.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_auth.AuthenticationApi(alfresco_auth.ApiClient(configuration))

try:
    # Delete ticket (logout)
    api_instance.delete_ticket()
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_ticket**
> ValidTicketEntry validate_ticket()

Validate ticket

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Validates the specified ticket (derived from Authorization header) is still valid.  For example, you can pass the Authorization request header using Javascript:   ```Javascript     request.setRequestHeader (\"Authorization\", \"Basic \" + btoa(ticket));   ``` 

### Example
```python
from __future__ import print_function
import time
import alfresco_auth
from alfresco_auth.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_auth.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_auth.AuthenticationApi(alfresco_auth.ApiClient(configuration))

try:
    # Validate ticket
    api_response = api_instance.validate_ticket()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

