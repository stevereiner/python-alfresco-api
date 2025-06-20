# alfresco_core_client.DownloadsApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_download**](DownloadsApi.md#cancel_download) | **DELETE** /downloads/{downloadId} | Cancel a download
[**create_download**](DownloadsApi.md#create_download) | **POST** /downloads | Create a new download
[**get_download**](DownloadsApi.md#get_download) | **GET** /downloads/{downloadId} | Get a download


# **cancel_download**
> cancel_download(download_id)

Cancel a download

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

Cancels the creation of a download request.

**Note:** The download node can be deleted using the **DELETE /nodes/{downloadId}** endpoint

By default, if the download node is not deleted it will be picked up by a cleaner job which removes download nodes older than a configurable amount of time (default is 1 hour)

Information about the existing progress at the time of cancelling can be retrieved by calling the **GET /downloads/{downloadId}** endpoint

The cancel operation is done asynchronously.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
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
    api_instance = alfresco_core_client.DownloadsApi(api_client)
    download_id = 'download_id_example' # str | The identifier of a download node.

    try:
        # Cancel a download
        api_instance.cancel_download(download_id)
    except Exception as e:
        print("Exception when calling DownloadsApi->cancel_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| The identifier of a download node. | 

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
**202** | The request to cancel a download was accepted |  -  |
**400** | Invalid parameter: **downloadId** is invalid, or **downloadId** does not point to a node of download type  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission cancel the **downloadId** node |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_download**
> DownloadEntry create_download(download_body_create, fields=fields)

Create a new download

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

Creates a new download node asynchronously, the content of which will be the zipped content of the **nodeIds** specified in the JSON body like this:

```JSON
{
    "nodeIds":
     [
       "c8bb482a-ff3c-4704-a3a3-de1c83ccd84c",
       "cffa62db-aa01-493d-9594-058bc058eeb1"
     ]
}
```

**Note:** The content of the download node can be obtained using the **GET /nodes/{downloadId}/content** endpoint


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.download_body_create import DownloadBodyCreate
from alfresco_core_client.models.download_entry import DownloadEntry
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
    api_instance = alfresco_core_client.DownloadsApi(api_client)
    download_body_create = alfresco_core_client.DownloadBodyCreate() # DownloadBodyCreate | The nodeIds the content of which will be zipped, which zip will be set as the content of our download node.
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Create a new download
        api_response = api_instance.create_download(download_body_create, fields=fields)
        print("The response of DownloadsApi->create_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadsApi->create_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_body_create** | [**DownloadBodyCreate**](DownloadBodyCreate.md)| The nodeIds the content of which will be zipped, which zip will be set as the content of our download node. | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**DownloadEntry**](DownloadEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The request to create a download node was accepted |  -  |
**400** | Invalid parameter: **DownloadBodyCreate** is invalid due to incorrect syntax, or **nodeIds** is empty, or **nodeIds** contains a duplicate **nodeId**  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission to add a certain **nodeId** to the zip |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download**
> DownloadEntry get_download(download_id, fields=fields)

Get a download

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

Retrieve status information for download node **downloadId**


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.download_entry import DownloadEntry
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
    api_instance = alfresco_core_client.DownloadsApi(api_client)
    download_id = 'download_id_example' # str | The identifier of a download node.
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Get a download
        api_response = api_instance.get_download(download_id, fields=fields)
        print("The response of DownloadsApi->get_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadsApi->get_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| The identifier of a download node. | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**DownloadEntry**](DownloadEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Download node information |  -  |
**400** | Invalid parameter: **downloadId** is invalid, or **downloadId** does not point to a node of download type  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission to get information about **downloadId** node |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

