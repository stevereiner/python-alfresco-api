# alfresco_core_client.ProbesApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_probe**](ProbesApi.md#get_probe) | **GET** /probes/{probeId} | Check readiness and liveness of the repository


# **get_probe**
> ProbeEntry get_probe(probe_id)

Check readiness and liveness of the repository

**Note:** this endpoint is available in Alfresco 6.0 and newer versions.

Returns a status of 200 to indicate success and 503 for failure.

The readiness probe is normally only used to check repository startup.

The liveness probe should then be used to check the repository is still responding to requests.

**Note:** No authentication is required to call this endpoint.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.probe_entry import ProbeEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.ProbesApi(api_client)
    probe_id = 'probe_id_example' # str | The name of the probe: * -ready- * -live- 

    try:
        # Check readiness and liveness of the repository
        api_response = api_instance.get_probe(probe_id)
        print("The response of ProbesApi->get_probe:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | **probeId** does not exist  |  -  |
**503** | Service Unavailable - Probe failure status. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

