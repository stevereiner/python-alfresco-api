# alfresco_core_client.RenditionsApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rendition**](RenditionsApi.md#create_rendition) | **POST** /nodes/{nodeId}/renditions | Create rendition
[**get_rendition**](RenditionsApi.md#get_rendition) | **GET** /nodes/{nodeId}/renditions/{renditionId} | Get rendition information
[**get_rendition_content**](RenditionsApi.md#get_rendition_content) | **GET** /nodes/{nodeId}/renditions/{renditionId}/content | Get rendition content
[**list_renditions**](RenditionsApi.md#list_renditions) | **GET** /nodes/{nodeId}/renditions | List renditions


# **create_rendition**
> create_rendition(node_id, rendition_body_create)

Create rendition

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

An asynchronous request to create a rendition for file **nodeId**.

The rendition is specified by name **id** in the request body:
```JSON
{
  "id":"doclib"
}
```
 Multiple names may be specified as a comma separated list or using a list format:
```JSON
[
  {
     "id": "doclib"
  },
  {
     "id": "avatar"
  }
]
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.rendition_body_create import RenditionBodyCreate
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
    api_instance = alfresco_core_client.RenditionsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    rendition_body_create = alfresco_core_client.RenditionBodyCreate() # RenditionBodyCreate | The rendition \"id\".

    try:
        # Create rendition
        api_instance.create_rendition(node_id, rendition_body_create)
    except Exception as e:
        print("Exception when calling RenditionsApi->create_rendition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **rendition_body_create** | [**RenditionBodyCreate**](RenditionBodyCreate.md)| The rendition \&quot;id\&quot;. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |
**400** | Invalid parameter: **nodeId** is not a valid format or is not a file or **renditionBodyCreate** is invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission for **nodeId** |  -  |
**404** | **nodeId** or **renditionId** does not exist  |  -  |
**409** | All requested renditions already exist |  -  |
**501** | Renditions/thumbnails are disabled for the system |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rendition**
> RenditionEntry get_rendition(node_id, rendition_id)

Get rendition information

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Gets the rendition information for **renditionId** of file **nodeId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.rendition_entry import RenditionEntry
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
    api_instance = alfresco_core_client.RenditionsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    rendition_id = 'rendition_id_example' # str | The name of a thumbnail rendition, for example *doclib*, or *pdf*.

    try:
        # Get rendition information
        api_response = api_instance.get_rendition(node_id, rendition_id)
        print("The response of RenditionsApi->get_rendition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenditionsApi->get_rendition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **rendition_id** | **str**| The name of a thumbnail rendition, for example *doclib*, or *pdf*. | 

### Return type

[**RenditionEntry**](RenditionEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** is not a valid format, or is not a file, or **renditionId** is invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission for **nodeId** |  -  |
**404** | **nodeId** or **renditionId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rendition_content**
> bytearray get_rendition_content(node_id, rendition_id, attachment=attachment, if_modified_since=if_modified_since, range=range, placeholder=placeholder)

Get rendition content

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Gets the rendition content for **renditionId** of file **nodeId**.


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
    api_instance = alfresco_core_client.RenditionsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    rendition_id = 'rendition_id_example' # str | The name of a thumbnail rendition, for example *doclib*, or *pdf*.
    attachment = True # bool | **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  (optional) (default to True)
    if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`.  (optional)
    range = 'range_example' # str | The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes=1-10.  (optional)
    placeholder = False # bool | If **true** and there is no rendition for this **nodeId** and **renditionId**, then the placeholder image for the mime type of this rendition is returned, rather than a 404 response.  (optional) (default to False)

    try:
        # Get rendition content
        api_response = api_instance.get_rendition_content(node_id, rendition_id, attachment=attachment, if_modified_since=if_modified_since, range=range, placeholder=placeholder)
        print("The response of RenditionsApi->get_rendition_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenditionsApi->get_rendition_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **rendition_id** | **str**| The name of a thumbnail rendition, for example *doclib*, or *pdf*. | 
 **attachment** | **bool**| **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  | [optional] [default to True]
 **if_modified_since** | **datetime**| Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, &#x60;Wed, 09 Mar 2016 16:56:34 GMT&#x60;.  | [optional] 
 **range** | **str**| The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes&#x3D;1-10.  | [optional] 
 **placeholder** | **bool**| If **true** and there is no rendition for this **nodeId** and **renditionId**, then the placeholder image for the mime type of this rendition is returned, rather than a 404 response.  | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**206** | Partial Content |  -  |
**304** | Content has not been modified since the date provided in the If-Modified-Since header |  -  |
**400** | Invalid parameter: **nodeId** is not a valid format, or is not a file, or **renditionId** is invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission for **nodeId** |  -  |
**404** | **nodeId** or **renditionId** does not exist  |  -  |
**416** | Range Not Satisfiable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_renditions**
> RenditionPaging list_renditions(node_id, where=where)

List renditions

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Gets a list of the rendition information for each rendition of the the file **nodeId**, including the rendition id.

Each rendition returned has a **status**: CREATED means it is available to view or download, NOT_CREATED means the rendition can be requested.

You can use the **where** parameter to filter the returned renditions by **status**. For example, the following **where**
clause will return just the CREATED renditions:

```
(status='CREATED')
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.rendition_paging import RenditionPaging
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
    api_instance = alfresco_core_client.RenditionsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)

    try:
        # List renditions
        api_response = api_instance.list_renditions(node_id, where=where)
        print("The response of RenditionsApi->list_renditions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenditionsApi->list_renditions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 

### Return type

[**RenditionPaging**](RenditionPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** is not a valid format, is not a file, or **where** is invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission for **nodeId** |  -  |
**404** | **nodeId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

