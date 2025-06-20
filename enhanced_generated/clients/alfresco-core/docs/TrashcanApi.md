# alfresco_core_client.TrashcanApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_deleted_node**](TrashcanApi.md#delete_deleted_node) | **DELETE** /deleted-nodes/{nodeId} | Permanently delete a deleted node
[**get_archived_node_rendition**](TrashcanApi.md#get_archived_node_rendition) | **GET** /deleted-nodes/{nodeId}/renditions/{renditionId} | Get rendition information for a deleted node
[**get_archived_node_rendition_content**](TrashcanApi.md#get_archived_node_rendition_content) | **GET** /deleted-nodes/{nodeId}/renditions/{renditionId}/content | Get rendition content of a deleted node
[**get_deleted_node**](TrashcanApi.md#get_deleted_node) | **GET** /deleted-nodes/{nodeId} | Get a deleted node
[**get_deleted_node_content**](TrashcanApi.md#get_deleted_node_content) | **GET** /deleted-nodes/{nodeId}/content | Get deleted node content
[**list_deleted_node_renditions**](TrashcanApi.md#list_deleted_node_renditions) | **GET** /deleted-nodes/{nodeId}/renditions | List renditions for a deleted node
[**list_deleted_nodes**](TrashcanApi.md#list_deleted_nodes) | **GET** /deleted-nodes | List deleted nodes
[**restore_deleted_node**](TrashcanApi.md#restore_deleted_node) | **POST** /deleted-nodes/{nodeId}/restore | Restore a deleted node


# **delete_deleted_node**
> delete_deleted_node(node_id)

Permanently delete a deleted node

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Permanently deletes the deleted node **nodeId**.


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
    api_instance = alfresco_core_client.TrashcanApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.

    try:
        # Permanently delete a deleted node
        api_instance.delete_deleted_node(node_id)
    except Exception as e:
        print("Exception when calling TrashcanApi->delete_deleted_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 

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
**400** | Invalid parameter: **nodeId** is not a valid format  |  -  |
**401** | Authentication failed |  -  |
**403** | User does not have permission to permanently delete the deleted node |  -  |
**404** | **nodeId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archived_node_rendition**
> RenditionEntry get_archived_node_rendition(node_id, rendition_id)

Get rendition information for a deleted node

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
    api_instance = alfresco_core_client.TrashcanApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    rendition_id = 'rendition_id_example' # str | The name of a thumbnail rendition, for example *doclib*, or *pdf*.

    try:
        # Get rendition information for a deleted node
        api_response = api_instance.get_archived_node_rendition(node_id, rendition_id)
        print("The response of TrashcanApi->get_archived_node_rendition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrashcanApi->get_archived_node_rendition: %s\n" % e)
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

# **get_archived_node_rendition_content**
> bytearray get_archived_node_rendition_content(node_id, rendition_id, attachment=attachment, if_modified_since=if_modified_since, range=range, placeholder=placeholder)

Get rendition content of a deleted node

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
    api_instance = alfresco_core_client.TrashcanApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    rendition_id = 'rendition_id_example' # str | The name of a thumbnail rendition, for example *doclib*, or *pdf*.
    attachment = True # bool | **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  (optional) (default to True)
    if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`.  (optional)
    range = 'range_example' # str | The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes=1-10.  (optional)
    placeholder = False # bool | If **true** and there is no rendition for this **nodeId** and **renditionId**, then the placeholder image for the mime type of this rendition is returned, rather than a 404 response.  (optional) (default to False)

    try:
        # Get rendition content of a deleted node
        api_response = api_instance.get_archived_node_rendition_content(node_id, rendition_id, attachment=attachment, if_modified_since=if_modified_since, range=range, placeholder=placeholder)
        print("The response of TrashcanApi->get_archived_node_rendition_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrashcanApi->get_archived_node_rendition_content: %s\n" % e)
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

# **get_deleted_node**
> DeletedNodeEntry get_deleted_node(node_id, include=include)

Get a deleted node

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Gets the specific deleted node **nodeId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.deleted_node_entry import DeletedNodeEntry
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
    api_instance = alfresco_core_client.TrashcanApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    include = ['include_example'] # List[str] | Returns additional information about the node. The following optional fields can be requested: * allowableOperations * association * isLink * isFavorite * isLocked * path * permissions * definition  (optional)

    try:
        # Get a deleted node
        api_response = api_instance.get_deleted_node(node_id, include=include)
        print("The response of TrashcanApi->get_deleted_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrashcanApi->get_deleted_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **include** | [**List[str]**](str.md)| Returns additional information about the node. The following optional fields can be requested: * allowableOperations * association * isLink * isFavorite * isLocked * path * permissions * definition  | [optional] 

### Return type

[**DeletedNodeEntry**](DeletedNodeEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** is not a valid format  |  -  |
**401** | Authentication failed |  -  |
**403** | User does not have permission to view the deleted node |  -  |
**404** | **nodeId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deleted_node_content**
> bytearray get_deleted_node_content(node_id, attachment=attachment, if_modified_since=if_modified_since, range=range)

Get deleted node content

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Gets the content of the deleted node with identifier **nodeId**.


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
    api_instance = alfresco_core_client.TrashcanApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    attachment = True # bool | **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  (optional) (default to True)
    if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`.  (optional)
    range = 'range_example' # str | The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes=1-10.  (optional)

    try:
        # Get deleted node content
        api_response = api_instance.get_deleted_node_content(node_id, attachment=attachment, if_modified_since=if_modified_since, range=range)
        print("The response of TrashcanApi->get_deleted_node_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrashcanApi->get_deleted_node_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **attachment** | **bool**| **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  | [optional] [default to True]
 **if_modified_since** | **datetime**| Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, &#x60;Wed, 09 Mar 2016 16:56:34 GMT&#x60;.  | [optional] 
 **range** | **str**| The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes&#x3D;1-10.  | [optional] 

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
**400** | Invalid parameter: **nodeId** is not a valid format, or is not a file  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission to retrieve content of **nodeId** |  -  |
**404** | **nodeId** does not exist  |  -  |
**416** | Range Not Satisfiable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deleted_node_renditions**
> RenditionPaging list_deleted_node_renditions(node_id, where=where)

List renditions for a deleted node

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Gets a list of the rendition information for each rendition of the file **nodeId**, including the rendition id.

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
    api_instance = alfresco_core_client.TrashcanApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)

    try:
        # List renditions for a deleted node
        api_response = api_instance.list_deleted_node_renditions(node_id, where=where)
        print("The response of TrashcanApi->list_deleted_node_renditions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrashcanApi->list_deleted_node_renditions: %s\n" % e)
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

# **list_deleted_nodes**
> DeletedNodesPaging list_deleted_nodes(skip_count=skip_count, max_items=max_items, include=include)

List deleted nodes

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Gets a list of deleted nodes for the current user.

If the current user is an administrator deleted nodes for all users will be returned.

The list of deleted nodes will be ordered with the most recently deleted node at the top of the list.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.deleted_nodes_paging import DeletedNodesPaging
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
    api_instance = alfresco_core_client.TrashcanApi(api_client)
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    include = ['include_example'] # List[str] | Returns additional information about the node. The following optional fields can be requested: * allowableOperations * aspectNames * association * isLink * isFavorite * isLocked * path * properties * permissions  (optional)

    try:
        # List deleted nodes
        api_response = api_instance.list_deleted_nodes(skip_count=skip_count, max_items=max_items, include=include)
        print("The response of TrashcanApi->list_deleted_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrashcanApi->list_deleted_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **include** | [**List[str]**](str.md)| Returns additional information about the node. The following optional fields can be requested: * allowableOperations * aspectNames * association * isLink * isFavorite * isLocked * path * properties * permissions  | [optional] 

### Return type

[**DeletedNodesPaging**](DeletedNodesPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems** or **skipCount** is invalid  |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_deleted_node**
> NodeEntry restore_deleted_node(node_id, fields=fields, deleted_node_body_restore=deleted_node_body_restore)

Restore a deleted node

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Attempts to restore the deleted node **nodeId** to its original location or to a new location.

If the node is successfully restored to its former primary parent, then only the
primary child association will be restored, including recursively for any primary
children. It should be noted that no other secondary child associations or peer
associations will be restored, for any of the nodes within the primary parent-child
hierarchy of restored nodes, irrespective of whether these associations were to
nodes within or outside of the restored hierarchy.

Also, any previously shared link will not be restored since it is deleted at the time
of delete of each node.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.deleted_node_body_restore import DeletedNodeBodyRestore
from alfresco_core_client.models.node_entry import NodeEntry
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
    api_instance = alfresco_core_client.TrashcanApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)
    deleted_node_body_restore = alfresco_core_client.DeletedNodeBodyRestore() # DeletedNodeBodyRestore | The targetParentId if the node is restored to a new location. (optional)

    try:
        # Restore a deleted node
        api_response = api_instance.restore_deleted_node(node_id, fields=fields, deleted_node_body_restore=deleted_node_body_restore)
        print("The response of TrashcanApi->restore_deleted_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrashcanApi->restore_deleted_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 
 **deleted_node_body_restore** | [**DeletedNodeBodyRestore**](DeletedNodeBodyRestore.md)| The targetParentId if the node is restored to a new location. | [optional] 

### Return type

[**NodeEntry**](NodeEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** or **targetNodeId** is not a valid format  |  -  |
**401** | Authentication failed |  -  |
**403** | User does not have permission to restore the deleted node or user does not have permission to the target node |  -  |
**404** | **nodeId** does not exist or the restore destination parent node does not exists  |  -  |
**409** | Node name already exists in the restore destination |  -  |
**422** | Model integrity exception trying to restore the node |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

