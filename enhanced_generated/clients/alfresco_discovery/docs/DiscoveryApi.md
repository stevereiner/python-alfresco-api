# alfresco_discovery.DiscoveryApi

All URIs are relative to */alfresco/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_repository_information**](DiscoveryApi.md#get_repository_information) | **GET** /discovery | Get repository information

# **get_repository_information**
> DiscoveryEntry get_repository_information()

Get repository information

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Retrieves the capabilities and detailed version information from the repository. 

### Example
```python
from __future__ import print_function
import time
import alfresco_discovery
from alfresco_discovery.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_discovery.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_discovery.DiscoveryApi(alfresco_discovery.ApiClient(configuration))

try:
    # Get repository information
    api_response = api_instance.get_repository_information()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

