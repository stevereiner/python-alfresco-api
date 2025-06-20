# alfresco_core.DownloadsApi

All URIs are relative to */alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_download**](DownloadsApi.md#cancel_download) | **DELETE** /downloads/{downloadId} | Cancel a download
[**create_download**](DownloadsApi.md#create_download) | **POST** /downloads | Create a new download
[**get_download**](DownloadsApi.md#get_download) | **GET** /downloads/{downloadId} | Get a download

# **cancel_download**
> cancel_download(download_id)

Cancel a download

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Cancels the creation of a download request.  **Note:** The download node can be deleted using the **DELETE /nodes/{downloadId}** endpoint  By default, if the download node is not deleted it will be picked up by a cleaner job which removes download nodes older than a configurable amount of time (default is 1 hour)  Information about the existing progress at the time of cancelling can be retrieved by calling the **GET /downloads/{downloadId}** endpoint  The cancel operation is done asynchronously. 

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
api_instance = alfresco_core.DownloadsApi(alfresco_core.ApiClient(configuration))
download_id = 'download_id_example' # str | The identifier of a download node.

try:
    # Cancel a download
    api_instance.cancel_download(download_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_download**
> DownloadEntry create_download(body, fields=fields)

Create a new download

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Creates a new download node asynchronously, the content of which will be the zipped content of the **nodeIds** specified in the JSON body like this:  ```JSON {     \"nodeIds\":      [        \"c8bb482a-ff3c-4704-a3a3-de1c83ccd84c\",        \"cffa62db-aa01-493d-9594-058bc058eeb1\"      ] } ```  **Note:** The content of the download node can be obtained using the **GET /nodes/{downloadId}/content** endpoint 

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
api_instance = alfresco_core.DownloadsApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.DownloadBodyCreate() # DownloadBodyCreate | The nodeIds the content of which will be zipped, which zip will be set as the content of our download node.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Create a new download
    api_response = api_instance.create_download(body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadsApi->create_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadBodyCreate**](DownloadBodyCreate.md)| The nodeIds the content of which will be zipped, which zip will be set as the content of our download node. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**DownloadEntry**](DownloadEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download**
> DownloadEntry get_download(download_id, fields=fields)

Get a download

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Retrieve status information for download node **downloadId** 

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
api_instance = alfresco_core.DownloadsApi(alfresco_core.ApiClient(configuration))
download_id = 'download_id_example' # str | The identifier of a download node.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Get a download
    api_response = api_instance.get_download(download_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadsApi->get_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_id** | **str**| The identifier of a download node. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**DownloadEntry**](DownloadEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

