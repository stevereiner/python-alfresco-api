# alfresco_core.ProbesApi

All URIs are relative to */alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_probe**](ProbesApi.md#get_probe) | **GET** /probes/{probeId} | Check readiness and liveness of the repository

# **get_probe**
> ProbeEntry get_probe(probe_id)

Check readiness and liveness of the repository

**Note:** this endpoint is available in Alfresco 6.0 and newer versions.  Returns a status of 200 to indicate success and 503 for failure.  The readiness probe is normally only used to check repository startup.  The liveness probe should then be used to check the repository is still responding to requests.  **Note:** No authentication is required to call this endpoint. 

### Example
```python
from __future__ import print_function
import time
import alfresco_core
from alfresco_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_core.ProbesApi(alfresco_core.ApiClient(configuration))
probe_id = 'probe_id_example' # str | The name of the probe: * -ready- * -live- 

try:
    # Check readiness and liveness of the repository
    api_response = api_instance.get_probe(probe_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProbesApi->get_probe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **probe_id** | **str**| The name of the probe: * -ready- * -live-  | 

### Return type

[**ProbeEntry**](ProbeEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

