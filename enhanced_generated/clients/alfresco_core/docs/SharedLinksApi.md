# alfresco_core.SharedLinksApi

All URIs are relative to */alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shared_link**](SharedLinksApi.md#create_shared_link) | **POST** /shared-links | Create a shared link to a file
[**delete_shared_link**](SharedLinksApi.md#delete_shared_link) | **DELETE** /shared-links/{sharedId} | Deletes a shared link
[**email_shared_link**](SharedLinksApi.md#email_shared_link) | **POST** /shared-links/{sharedId}/email | Email shared link
[**get_shared_link**](SharedLinksApi.md#get_shared_link) | **GET** /shared-links/{sharedId} | Get a shared link
[**get_shared_link_content**](SharedLinksApi.md#get_shared_link_content) | **GET** /shared-links/{sharedId}/content | Get shared link content
[**get_shared_link_rendition**](SharedLinksApi.md#get_shared_link_rendition) | **GET** /shared-links/{sharedId}/renditions/{renditionId} | Get shared link rendition information
[**get_shared_link_rendition_content**](SharedLinksApi.md#get_shared_link_rendition_content) | **GET** /shared-links/{sharedId}/renditions/{renditionId}/content | Get shared link rendition content
[**list_shared_link_renditions**](SharedLinksApi.md#list_shared_link_renditions) | **GET** /shared-links/{sharedId}/renditions | List renditions for a shared link
[**list_shared_links**](SharedLinksApi.md#list_shared_links) | **GET** /shared-links | List shared links

# **create_shared_link**
> SharedLinkEntry create_shared_link(body, include=include, fields=fields)

Create a shared link to a file

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Create a shared link to the file **nodeId** in the request body. Also, an optional expiry date could be set, so the shared link would become invalid when the expiry date is reached. For example:  ```JSON   {     \"nodeId\": \"1ff9da1a-ee2f-4b9c-8c34-3333333333\",     \"expiresAt\": \"2017-03-23T23:00:00.000+0000\"   } ```  **Note:** You can create shared links to more than one file specifying a list of **nodeId**s in the JSON body like this:  ```JSON [   {     \"nodeId\": \"1ff9da1a-ee2f-4b9c-8c34-4444444444\"   },   {     \"nodeId\": \"1ff9da1a-ee2f-4b9c-8c34-5555555555\"   } ] ``` If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:  ```JSON {   \"list\": {     \"pagination\": {       \"count\": 2,       \"hasMoreItems\": false,       \"totalItems\": 2,       \"skipCount\": 0,       \"maxItems\": 100     },     \"entries\": [       {         \"entry\": {           ...         }       },       {         \"entry\": {           ...         }       }     ]   } } ``` 

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
api_instance = alfresco_core.SharedLinksApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.SharedLinkBodyCreate() # SharedLinkBodyCreate | The nodeId to create a shared link for.
include = ['include_example'] # list[str] | Returns additional information about the shared link, the following optional fields can be requested: * allowableOperations * path * properties * isFavorite * aspectNames  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Create a shared link to a file
    api_response = api_instance.create_shared_link(body, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLinksApi->create_shared_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharedLinkBodyCreate**](SharedLinkBodyCreate.md)| The nodeId to create a shared link for. | 
 **include** | [**list[str]**](str.md)| Returns additional information about the shared link, the following optional fields can be requested: * allowableOperations * path * properties * isFavorite * aspectNames  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SharedLinkEntry**](SharedLinkEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shared_link**
> delete_shared_link(shared_id)

Deletes a shared link

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Deletes the shared link with identifier **sharedId**. 

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
api_instance = alfresco_core.SharedLinksApi(alfresco_core.ApiClient(configuration))
shared_id = 'shared_id_example' # str | The identifier of a shared link to a file.

try:
    # Deletes a shared link
    api_instance.delete_shared_link(shared_id)
except ApiException as e:
    print("Exception when calling SharedLinksApi->delete_shared_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_id** | **str**| The identifier of a shared link to a file. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_shared_link**
> email_shared_link(body, shared_id)

Email shared link

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Sends email with app-specific url including identifier **sharedId**.  The client and recipientEmails properties are mandatory in the request body. For example, to email a shared link with minimum info: ```JSON {     \"client\": \"myClient\",     \"recipientEmails\": [\"john.doe@acme.com\", \"joe.bloggs@acme.com\"] } ``` A plain text message property can be optionally provided in the request body to customise the sent email. Also, a locale property can be optionally provided in the request body to send the emails in a particular language (if the locale is supported by Alfresco). For example, to email a shared link with a messages and a locale: ```JSON {     \"client\": \"myClient\",     \"recipientEmails\": [\"john.doe@acme.com\", \"joe.bloggs@acme.com\"],     \"message\": \"myMessage\",     \"locale\":\"en-GB\" } ``` **Note:** The client must be registered before you can send a shared link email. See [server documentation]. However, out-of-the-box  share is registered as a default client, so you could pass **share** as the client name: ```JSON {     \"client\": \"share\",     \"recipientEmails\": [\"john.doe@acme.com\"] } ``` 

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
api_instance = alfresco_core.SharedLinksApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.SharedLinkBodyEmail() # SharedLinkBodyEmail | The shared link email to send.
shared_id = 'shared_id_example' # str | The identifier of a shared link to a file.

try:
    # Email shared link
    api_instance.email_shared_link(body, shared_id)
except ApiException as e:
    print("Exception when calling SharedLinksApi->email_shared_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharedLinkBodyEmail**](SharedLinkBodyEmail.md)| The shared link email to send. | 
 **shared_id** | **str**| The identifier of a shared link to a file. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_link**
> SharedLinkEntry get_shared_link(shared_id, fields=fields)

Get a shared link

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets minimal information for the file with shared link identifier **sharedId**.  **Note:** No authentication is required to call this endpoint. 

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
api_instance = alfresco_core.SharedLinksApi(alfresco_core.ApiClient(configuration))
shared_id = 'shared_id_example' # str | The identifier of a shared link to a file.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Get a shared link
    api_response = api_instance.get_shared_link(shared_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLinksApi->get_shared_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_id** | **str**| The identifier of a shared link to a file. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SharedLinkEntry**](SharedLinkEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_link_content**
> str get_shared_link_content(shared_id, attachment=attachment, if_modified_since=if_modified_since, range=range)

Get shared link content

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the content of the file with shared link identifier **sharedId**.  **Note:** No authentication is required to call this endpoint. 

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
api_instance = alfresco_core.SharedLinksApi(alfresco_core.ApiClient(configuration))
shared_id = 'shared_id_example' # str | The identifier of a shared link to a file.
attachment = true # bool | **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  (optional) (default to true)
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`.  (optional)
range = 'range_example' # str | The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes=1-10.  (optional)

try:
    # Get shared link content
    api_response = api_instance.get_shared_link_content(shared_id, attachment=attachment, if_modified_since=if_modified_since, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLinksApi->get_shared_link_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_id** | **str**| The identifier of a shared link to a file. | 
 **attachment** | **bool**| **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  | [optional] [default to true]
 **if_modified_since** | **datetime**| Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, &#x60;Wed, 09 Mar 2016 16:56:34 GMT&#x60;.  | [optional] 
 **range** | **str**| The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes&#x3D;1-10.  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_link_rendition**
> RenditionEntry get_shared_link_rendition(shared_id, rendition_id)

Get shared link rendition information

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets rendition information for the file with shared link identifier **sharedId**.  This API method returns rendition information where the rendition status is CREATED, which means the rendition is available to view/download.  **Note:** No authentication is required to call this endpoint. 

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
api_instance = alfresco_core.SharedLinksApi(alfresco_core.ApiClient(configuration))
shared_id = 'shared_id_example' # str | The identifier of a shared link to a file.
rendition_id = 'rendition_id_example' # str | The name of a thumbnail rendition, for example *doclib*, or *pdf*.

try:
    # Get shared link rendition information
    api_response = api_instance.get_shared_link_rendition(shared_id, rendition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLinksApi->get_shared_link_rendition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_id** | **str**| The identifier of a shared link to a file. | 
 **rendition_id** | **str**| The name of a thumbnail rendition, for example *doclib*, or *pdf*. | 

### Return type

[**RenditionEntry**](RenditionEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_link_rendition_content**
> str get_shared_link_rendition_content(shared_id, rendition_id, attachment=attachment, if_modified_since=if_modified_since, range=range)

Get shared link rendition content

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the rendition content for file with shared link identifier **sharedId**.  **Note:** No authentication is required to call this endpoint. 

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
api_instance = alfresco_core.SharedLinksApi(alfresco_core.ApiClient(configuration))
shared_id = 'shared_id_example' # str | The identifier of a shared link to a file.
rendition_id = 'rendition_id_example' # str | The name of a thumbnail rendition, for example *doclib*, or *pdf*.
attachment = true # bool | **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  (optional) (default to true)
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`.  (optional)
range = 'range_example' # str | The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes=1-10.  (optional)

try:
    # Get shared link rendition content
    api_response = api_instance.get_shared_link_rendition_content(shared_id, rendition_id, attachment=attachment, if_modified_since=if_modified_since, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLinksApi->get_shared_link_rendition_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_id** | **str**| The identifier of a shared link to a file. | 
 **rendition_id** | **str**| The name of a thumbnail rendition, for example *doclib*, or *pdf*. | 
 **attachment** | **bool**| **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  | [optional] [default to true]
 **if_modified_since** | **datetime**| Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, &#x60;Wed, 09 Mar 2016 16:56:34 GMT&#x60;.  | [optional] 
 **range** | **str**| The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes&#x3D;1-10.  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shared_link_renditions**
> RenditionPaging list_shared_link_renditions(shared_id)

List renditions for a shared link

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets a list of the rendition information for the file with shared link identifier **sharedId**.  This API method returns rendition information, including the rendition id, for each rendition where the rendition status is CREATED, which means the rendition is available to view/download.  **Note:** No authentication is required to call this endpoint. 

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
api_instance = alfresco_core.SharedLinksApi(alfresco_core.ApiClient(configuration))
shared_id = 'shared_id_example' # str | The identifier of a shared link to a file.

try:
    # List renditions for a shared link
    api_response = api_instance.list_shared_link_renditions(shared_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLinksApi->list_shared_link_renditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_id** | **str**| The identifier of a shared link to a file. | 

### Return type

[**RenditionPaging**](RenditionPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shared_links**
> SharedLinkPaging list_shared_links(skip_count=skip_count, max_items=max_items, where=where, include=include, fields=fields)

List shared links

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Get a list of links that the current user has read permission on source node.  The list is ordered in descending modified order.  **Note:** The list of links is eventually consistent so newly created shared links may not appear immediately. 

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
api_instance = alfresco_core.SharedLinksApi(alfresco_core.ApiClient(configuration))
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
where = 'where_example' # str | Optionally filter the list by \"sharedByUser\" userid of person who shared the link (can also use -me-)  *   ```where=(sharedByUser='jbloggs')```  *   ```where=(sharedByUser='-me-')```  (optional)
include = ['include_example'] # list[str] | Returns additional information about the shared link, the following optional fields can be requested: * allowableOperations * path * properties * isFavorite * aspectNames  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List shared links
    api_response = api_instance.list_shared_links(skip_count=skip_count, max_items=max_items, where=where, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedLinksApi->list_shared_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **where** | **str**| Optionally filter the list by \&quot;sharedByUser\&quot; userid of person who shared the link (can also use -me-)  *   &#x60;&#x60;&#x60;where&#x3D;(sharedByUser&#x3D;&#x27;jbloggs&#x27;)&#x60;&#x60;&#x60;  *   &#x60;&#x60;&#x60;where&#x3D;(sharedByUser&#x3D;&#x27;-me-&#x27;)&#x60;&#x60;&#x60;  | [optional] 
 **include** | [**list[str]**](str.md)| Returns additional information about the shared link, the following optional fields can be requested: * allowableOperations * path * properties * isFavorite * aspectNames  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SharedLinkPaging**](SharedLinkPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

