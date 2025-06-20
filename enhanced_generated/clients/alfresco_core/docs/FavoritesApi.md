# alfresco_core.FavoritesApi

All URIs are relative to */alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_favorite**](FavoritesApi.md#create_favorite) | **POST** /people/{personId}/favorites | Create a favorite
[**create_site_favorite**](FavoritesApi.md#create_site_favorite) | **POST** /people/{personId}/favorite-sites | Create a site favorite
[**delete_favorite**](FavoritesApi.md#delete_favorite) | **DELETE** /people/{personId}/favorites/{favoriteId} | Delete a favorite
[**delete_site_favorite**](FavoritesApi.md#delete_site_favorite) | **DELETE** /people/{personId}/favorite-sites/{siteId} | Delete a site favorite
[**get_favorite**](FavoritesApi.md#get_favorite) | **GET** /people/{personId}/favorites/{favoriteId} | Get a favorite
[**get_favorite_site**](FavoritesApi.md#get_favorite_site) | **GET** /people/{personId}/favorite-sites/{siteId} | Get a favorite site
[**list_favorite_sites_for_person**](FavoritesApi.md#list_favorite_sites_for_person) | **GET** /people/{personId}/favorite-sites | List favorite sites
[**list_favorites**](FavoritesApi.md#list_favorites) | **GET** /people/{personId}/favorites | List favorites

# **create_favorite**
> FavoriteEntry create_favorite(body, person_id, include=include, fields=fields)

Create a favorite

Favorite a **site**, **file**, or **folder** in the repository.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.  **Note:** You can favorite more than one entity by specifying a list of objects in the JSON body like this:  ```JSON [   {        \"target\": {           \"file\": {              \"guid\": \"abcde-01234-....\"           }        }    },    {        \"target\": {           \"file\": {              \"guid\": \"abcde-09863-....\"           }        }    }, ] ``` If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:  ```JSON {   \"list\": {     \"pagination\": {       \"count\": 2,       \"hasMoreItems\": false,       \"totalItems\": 2,       \"skipCount\": 0,       \"maxItems\": 100     },     \"entries\": [       {         \"entry\": {           ...         }       },       {         \"entry\": {           ...         }       }     ]   } } ``` 

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
api_instance = alfresco_core.FavoritesApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.FavoriteBodyCreate() # FavoriteBodyCreate | An object identifying the entity to be favorited.

The object consists of a single property which is an object with the name `site`, `file`, or `folder`.
The content of that object is the `guid` of the target entity.

For example, to favorite a file the following body would be used:

```JSON
{
   "target": {
      "file": {
         "guid": "abcde-01234-...."
      }
   }
}
```

person_id = 'person_id_example' # str | The identifier of a person.
include = ['include_example'] # list[str] | Returns additional information about favorites, the following optional fields can be requested: * path (note, this only applies to files and folders) * properties  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Create a favorite
    api_response = api_instance.create_favorite(body, person_id, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoritesApi->create_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FavoriteBodyCreate**](FavoriteBodyCreate.md)| An object identifying the entity to be favorited.

The object consists of a single property which is an object with the name &#x60;site&#x60;, &#x60;file&#x60;, or &#x60;folder&#x60;.
The content of that object is the &#x60;guid&#x60; of the target entity.

For example, to favorite a file the following body would be used:

&#x60;&#x60;&#x60;JSON
{
   &quot;target&quot;: {
      &quot;file&quot;: {
         &quot;guid&quot;: &quot;abcde-01234-....&quot;
      }
   }
}
&#x60;&#x60;&#x60;
 | 
 **person_id** | **str**| The identifier of a person. | 
 **include** | [**list[str]**](str.md)| Returns additional information about favorites, the following optional fields can be requested: * path (note, this only applies to files and folders) * properties  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**FavoriteEntry**](FavoriteEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_favorite**
> FavoriteSiteEntry create_site_favorite(body, person_id, fields=fields)

Create a site favorite

**Note:** this endpoint is deprecated as of Alfresco 4.2, and will be removed in the future. Use `/people/{personId}/favorites` instead.  Create a site favorite for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.   **Note:** You can favorite more than one site by specifying a list of sites in the JSON body like this:  ```JSON [   {     \"id\": \"test-site-1\"   },   {     \"id\": \"test-site-2\"   } ] ``` If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:  ```JSON {   \"list\": {     \"pagination\": {       \"count\": 2,       \"hasMoreItems\": false,       \"totalItems\": 2,       \"skipCount\": 0,       \"maxItems\": 100     },     \"entries\": [       {         \"entry\": {           ...         }       },       {         \"entry\": {           ...         }       }     ]   } } ``` 

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
api_instance = alfresco_core.FavoritesApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.FavoriteSiteBodyCreate() # FavoriteSiteBodyCreate | The id of the site to favorite.
person_id = 'person_id_example' # str | The identifier of a person.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Create a site favorite
    api_response = api_instance.create_site_favorite(body, person_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoritesApi->create_site_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FavoriteSiteBodyCreate**](FavoriteSiteBodyCreate.md)| The id of the site to favorite. | 
 **person_id** | **str**| The identifier of a person. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**FavoriteSiteEntry**](FavoriteSiteEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_favorite**
> delete_favorite(person_id, favorite_id)

Delete a favorite

Deletes **favoriteId** as a favorite of person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

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
api_instance = alfresco_core.FavoritesApi(alfresco_core.ApiClient(configuration))
person_id = 'person_id_example' # str | The identifier of a person.
favorite_id = 'favorite_id_example' # str | The identifier of a favorite.

try:
    # Delete a favorite
    api_instance.delete_favorite(person_id, favorite_id)
except ApiException as e:
    print("Exception when calling FavoritesApi->delete_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **favorite_id** | **str**| The identifier of a favorite. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_favorite**
> delete_site_favorite(person_id, site_id)

Delete a site favorite

**Note:** this endpoint is deprecated as of Alfresco 4.2, and will be removed in the future. Use `/people/{personId}/favorites/{favoriteId}` instead.  Deletes site **siteId** from the favorite site list of person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

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
api_instance = alfresco_core.FavoritesApi(alfresco_core.ApiClient(configuration))
person_id = 'person_id_example' # str | The identifier of a person.
site_id = 'site_id_example' # str | The identifier of a site.

try:
    # Delete a site favorite
    api_instance.delete_site_favorite(person_id, site_id)
except ApiException as e:
    print("Exception when calling FavoritesApi->delete_site_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **site_id** | **str**| The identifier of a site. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorite**
> FavoriteEntry get_favorite(person_id, favorite_id, include=include, fields=fields)

Get a favorite

Gets favorite **favoriteId** for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

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
api_instance = alfresco_core.FavoritesApi(alfresco_core.ApiClient(configuration))
person_id = 'person_id_example' # str | The identifier of a person.
favorite_id = 'favorite_id_example' # str | The identifier of a favorite.
include = ['include_example'] # list[str] | Returns additional information about favorites, the following optional fields can be requested: * path (note, this only applies to files and folders) * properties  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Get a favorite
    api_response = api_instance.get_favorite(person_id, favorite_id, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoritesApi->get_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **favorite_id** | **str**| The identifier of a favorite. | 
 **include** | [**list[str]**](str.md)| Returns additional information about favorites, the following optional fields can be requested: * path (note, this only applies to files and folders) * properties  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**FavoriteEntry**](FavoriteEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorite_site**
> SiteEntry get_favorite_site(person_id, site_id, fields=fields)

Get a favorite site

**Note:** this endpoint is deprecated as of Alfresco 4.2, and will be removed in the future. Use `/people/{personId}/favorites/{favoriteId}` instead.  Gets information on favorite site **siteId** of person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

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
api_instance = alfresco_core.FavoritesApi(alfresco_core.ApiClient(configuration))
person_id = 'person_id_example' # str | The identifier of a person.
site_id = 'site_id_example' # str | The identifier of a site.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Get a favorite site
    api_response = api_instance.get_favorite_site(person_id, site_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoritesApi->get_favorite_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **site_id** | **str**| The identifier of a site. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteEntry**](SiteEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_favorite_sites_for_person**
> SitePaging list_favorite_sites_for_person(person_id, skip_count=skip_count, max_items=max_items, fields=fields)

List favorite sites

**Note:** this endpoint is deprecated as of Alfresco 4.2, and will be removed in the future. Use `/people/{personId}/favorites` instead.  Gets a list of a person's favorite sites.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

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
api_instance = alfresco_core.FavoritesApi(alfresco_core.ApiClient(configuration))
person_id = 'person_id_example' # str | The identifier of a person.
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List favorite sites
    api_response = api_instance.list_favorite_sites_for_person(person_id, skip_count=skip_count, max_items=max_items, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoritesApi->list_favorite_sites_for_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SitePaging**](SitePaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_favorites**
> FavoritePaging list_favorites(person_id, skip_count=skip_count, max_items=max_items, order_by=order_by, where=where, include=include, fields=fields)

List favorites

Gets a list of favorites for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.  The default sort order for the returned list of favorites is type ascending, createdAt descending. You can override the default by using the **orderBy** parameter.  You can use any of the following fields to order the results: *   `type` *   `createdAt` *   `title`  You can use the **where** parameter to restrict the list in the response to entries of a specific kind. The **where** parameter takes a value. The value is a single predicate that can include one or more **EXISTS** conditions. The **EXISTS** condition uses a single operand to limit the list to include entries that include that one property. The property values are:  *   `target/file` *   `target/folder` *   `target/site`  For example, the following **where** parameter restricts the returned list to the file favorites for a person:  ```SQL (EXISTS(target/file)) ``` You can specify more than one condition using **OR**. The predicate must be enclosed in parentheses.   For example, the following **where** parameter restricts the returned list to the file and folder favorites for a person:  ```SQL (EXISTS(target/file) OR EXISTS(target/folder)) ``` 

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
api_instance = alfresco_core.FavoritesApi(alfresco_core.ApiClient(configuration))
person_id = 'person_id_example' # str | The identifier of a person.
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
order_by = ['order_by_example'] # list[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)
include = ['include_example'] # list[str] | Returns additional information about favorites, the following optional fields can be requested: * path (note, this only applies to files and folders) * properties  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List favorites
    api_response = api_instance.list_favorites(person_id, skip_count=skip_count, max_items=max_items, order_by=order_by, where=where, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoritesApi->list_favorites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **order_by** | [**list[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 
 **include** | [**list[str]**](str.md)| Returns additional information about favorites, the following optional fields can be requested: * path (note, this only applies to files and folders) * properties  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**FavoritePaging**](FavoritePaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

