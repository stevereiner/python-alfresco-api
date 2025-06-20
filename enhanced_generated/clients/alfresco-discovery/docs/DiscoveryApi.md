# alfresco_discovery_client.DiscoveryApi

All URIs are relative to */alfresco/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_repository_information**](DiscoveryApi.md#get_repository_information) | **GET** /discovery | Get repository information


# **get_repository_information**
> DiscoveryEntry get_repository_information()

Get repository information

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Retrieves the capabilities and detailed version information from the repository.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_discovery_client
from alfresco_discovery_client.models.discovery_entry import DiscoveryEntry
from alfresco_discovery_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /alfresco/api
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_discovery_client.Configuration(
    host = "/alfresco/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_discovery_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_discovery_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_discovery_client.DiscoveryApi(api_client)

    try:
        # Get repository information
        api_response = api_instance.get_repository_information()
        print("The response of DiscoveryApi->get_repository_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->get_repository_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DiscoveryEntry**](DiscoveryEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**501** | Discovery is disabled for the system |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

