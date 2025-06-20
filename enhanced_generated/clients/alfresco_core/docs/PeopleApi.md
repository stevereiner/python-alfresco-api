# alfresco_core.PeopleApi

All URIs are relative to */alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_person**](PeopleApi.md#create_person) | **POST** /people | Create person
[**delete_avatar_image**](PeopleApi.md#delete_avatar_image) | **DELETE** /people/{personId}/avatar | Delete avatar image
[**get_avatar_image**](PeopleApi.md#get_avatar_image) | **GET** /people/{personId}/avatar | Get avatar image
[**get_person**](PeopleApi.md#get_person) | **GET** /people/{personId} | Get a person
[**list_people**](PeopleApi.md#list_people) | **GET** /people | List people
[**request_password_reset**](PeopleApi.md#request_password_reset) | **POST** /people/{personId}/request-password-reset | Request password reset
[**reset_password**](PeopleApi.md#reset_password) | **POST** /people/{personId}/reset-password | Reset password
[**update_avatar_image**](PeopleApi.md#update_avatar_image) | **PUT** /people/{personId}/avatar | Update avatar image
[**update_person**](PeopleApi.md#update_person) | **PUT** /people/{personId} | Update person

# **create_person**
> PersonEntry create_person(body, fields=fields)

Create person

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Create a person.  If applicable, the given person's login access can also be optionally disabled.  You must have admin rights to create a person.  You can set custom properties when you create a person: ```JSON {   \"id\": \"abeecher\",   \"firstName\": \"Alice\",   \"lastName\": \"Beecher\",   \"displayName\": \"Alice Beecher\",   \"email\": \"abeecher@example.com\",   \"password\": \"secret\",   \"properties\":   {     \"my:property\": \"The value\"   } } ``` **Note:** setting properties of type d:content and d:category are not supported. 

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
api_instance = alfresco_core.PeopleApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.PersonBodyCreate() # PersonBodyCreate | The person details.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Create person
    api_response = api_instance.create_person(body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->create_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PersonBodyCreate**](PersonBodyCreate.md)| The person details. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**PersonEntry**](PersonEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_avatar_image**
> delete_avatar_image(person_id)

Delete avatar image

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Deletes the avatar image related to person **personId**.  You must be the person or have admin rights to update a person's avatar.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

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
api_instance = alfresco_core.PeopleApi(alfresco_core.ApiClient(configuration))
person_id = 'person_id_example' # str | The identifier of a person.

try:
    # Delete avatar image
    api_instance.delete_avatar_image(person_id)
except ApiException as e:
    print("Exception when calling PeopleApi->delete_avatar_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avatar_image**
> str get_avatar_image(person_id, attachment=attachment, if_modified_since=if_modified_since, placeholder=placeholder)

Get avatar image

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Gets the avatar image related to the person **personId**. If the person has no related avatar then the **placeholder** query parameter can be optionally used to request a placeholder image to be returned.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

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
api_instance = alfresco_core.PeopleApi(alfresco_core.ApiClient(configuration))
person_id = 'person_id_example' # str | The identifier of a person.
attachment = true # bool | **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  (optional) (default to true)
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`.  (optional)
placeholder = true # bool | If **true** and there is no avatar for this **personId** then the placeholder image is returned, rather than a 404 response.  (optional) (default to true)

try:
    # Get avatar image
    api_response = api_instance.get_avatar_image(person_id, attachment=attachment, if_modified_since=if_modified_since, placeholder=placeholder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->get_avatar_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **attachment** | **bool**| **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  | [optional] [default to true]
 **if_modified_since** | **datetime**| Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, &#x60;Wed, 09 Mar 2016 16:56:34 GMT&#x60;.  | [optional] 
 **placeholder** | **bool**| If **true** and there is no avatar for this **personId** then the placeholder image is returned, rather than a 404 response.  | [optional] [default to true]

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person**
> PersonEntry get_person(person_id, fields=fields)

Get a person

Gets information for the person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

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
api_instance = alfresco_core.PeopleApi(alfresco_core.ApiClient(configuration))
person_id = 'person_id_example' # str | The identifier of a person.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Get a person
    api_response = api_instance.get_person(person_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->get_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**PersonEntry**](PersonEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_people**
> PersonPaging list_people(skip_count=skip_count, max_items=max_items, order_by=order_by, include=include, fields=fields)

List people

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  List people.  You can use the **include** parameter to return any additional information.  The default sort order for the returned list is for people to be sorted by ascending id. You can override the default by using the **orderBy** parameter.  You can use any of the following fields to order the results: * id * firstName * lastName 

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
api_instance = alfresco_core.PeopleApi(alfresco_core.ApiClient(configuration))
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
order_by = ['order_by_example'] # list[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
include = ['include_example'] # list[str] | Returns additional information about the person. The following optional fields can be requested: * properties * aspectNames * capabilities  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List people
    api_response = api_instance.list_people(skip_count=skip_count, max_items=max_items, order_by=order_by, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->list_people: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **order_by** | [**list[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **include** | [**list[str]**](str.md)| Returns additional information about the person. The following optional fields can be requested: * properties * aspectNames * capabilities  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**PersonPaging**](PersonPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_password_reset**
> request_password_reset(body, person_id)

Request password reset

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Initiates the reset password workflow to send an email with reset password instruction to the user's registered email.  The client is mandatory in the request body. For example: ```JSON {   \"client\": \"myClient\" } ``` **Note:** The client must be registered before this API can send an email. See [server documentation]. However, out-of-the-box share is registered as a default client, so you could pass **share** as the client name: ```JSON {   \"client\": \"share\" } ``` **Note:** No authentication is required to call this endpoint. 

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
api_instance = alfresco_core.PeopleApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.ClientBody() # ClientBody | The client name to send email with app-specific url.
person_id = 'person_id_example' # str | The identifier of a person.

try:
    # Request password reset
    api_instance.request_password_reset(body, person_id)
except ApiException as e:
    print("Exception when calling PeopleApi->request_password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientBody**](ClientBody.md)| The client name to send email with app-specific url. | 
 **person_id** | **str**| The identifier of a person. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(body, person_id)

Reset password

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Resets user's password  The password, id and key properties are mandatory in the request body. For example: ```JSON {   \"password\":\"newPassword\",   \"id\":\"activiti$10\",   \"key\":\"4dad6d00-0daf-413a-b200-f64af4e12345\" } ``` **Note:** No authentication is required to call this endpoint. 

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
api_instance = alfresco_core.PeopleApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.PasswordResetBody() # PasswordResetBody | The reset password details
person_id = 'person_id_example' # str | The identifier of a person.

try:
    # Reset password
    api_instance.reset_password(body, person_id)
except ApiException as e:
    print("Exception when calling PeopleApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordResetBody**](PasswordResetBody.md)| The reset password details | 
 **person_id** | **str**| The identifier of a person. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avatar_image**
> update_avatar_image(body, person_id)

Update avatar image

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Updates the avatar image related to the person **personId**.  The request body should be the binary stream for the avatar image. The content type of the file should be an image file. This will be used to generate an \"avatar\" thumbnail rendition.  You must be the person or have admin rights to update a person's avatar.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

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
api_instance = alfresco_core.PeopleApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.Object() # Object | The binary content
person_id = 'person_id_example' # str | The identifier of a person.

try:
    # Update avatar image
    api_instance.update_avatar_image(body, person_id)
except ApiException as e:
    print("Exception when calling PeopleApi->update_avatar_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| The binary content | 
 **person_id** | **str**| The identifier of a person. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_person**
> PersonEntry update_person(body, person_id, fields=fields)

Update person

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Update the given person's details.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.  If applicable, the given person's login access can also be optionally disabled or re-enabled.  You must have admin rights to update a person — unless updating your own details.  If you are changing your password, as a non-admin user, then the existing password must also be supplied (using the oldPassword field in addition to the new password value).  Admin users cannot be disabled by setting enabled to false.  Non-admin users may not disable themselves.  You can set custom properties when you update a person: ```JSON {   \"firstName\": \"Alice\",   \"properties\":   {     \"my:property\": \"The value\"   } } ``` **Note:** setting properties of type d:content and d:category are not supported. 

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
api_instance = alfresco_core.PeopleApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.PersonBodyUpdate() # PersonBodyUpdate | The person details.
person_id = 'person_id_example' # str | The identifier of a person.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Update person
    api_response = api_instance.update_person(body, person_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->update_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PersonBodyUpdate**](PersonBodyUpdate.md)| The person details. | 
 **person_id** | **str**| The identifier of a person. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**PersonEntry**](PersonEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

