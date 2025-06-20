# alfresco_model_client.TypesApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_type**](TypesApi.md#get_type) | **GET** /types/{typeId} | Get a type
[**list_types**](TypesApi.md#list_types) | **GET** /types | List types


# **get_type**
> TypeEntry get_type(type_id)

Get a type

**Note:** This is available in Alfresco 7.0.0 and newer versions.
Get information for type **typeId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_model_client
from alfresco_model_client.models.type_entry import TypeEntry
from alfresco_model_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_model_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_model_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_model_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_model_client.TypesApi(api_client)
    type_id = 'type_id_example' # str | The Qname of a type(`prefix:name`) e.g 'cm:content'

    try:
        # Get a type
        api_response = api_instance.get_type(type_id)
        print("The response of TypesApi->get_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesApi->get_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**| The Qname of a type(&#x60;prefix:name&#x60;) e.g &#39;cm:content&#39; | 

### Return type

[**TypeEntry**](TypeEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: unknown typeId scheme specified  |  -  |
**401** | Authentication failed |  -  |
**404** | **typeId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_types**
> TypePaging list_types(where=where, skip_count=skip_count, max_items=max_items, include=include)

List types

**Note:** This is available in Alfresco 7.0.0 and newer versions.

Gets a list of types from the data dictionary. The System types will be ignored by default.
```JSON
{
  "list": {
    "pagination": {
      "count": 0,
      "hasMoreItems": true,
      "totalItems": 0,
      "skipCount": 0,
      "maxItems": 0
    },
    "entries": [
      {
        "entry": {
          "associations": [],
          "isArchive": true,
          "mandatoryAspects": [
              "cm:auditable",
              "sys:referenceable",
              "sys:localized"
          ],
          "includedInSupertypeQuery": true,
          "description": "Base Content Object",
          "isContainer": false,
          "model": {
              "id": "cm:contentmodel",
              "author": "Alfresco",
              "description": "Alfresco Content Domain Model",
              "namespaceUri": "http://www.alfresco.org/model/content/1.0",
              "namespacePrefix": "cm"
          },
          "id": "cm:content",
          "title": "Content",
          "parentId": "cm:cmobject"
          "properties": [
            {
              "id": "cm:name",
              "title": "Name",
              "description": "Name",
              "dataType": "d:text",
              "isMultiValued": false,
              "isMandatory": true,
              "isMandatoryEnforced": true
              "isProtected": false
              ...
            },
            {
              ...
            }
          ]
        }
      },
      {
        "entry": {
          ...
        }
      },
      {
        "entry": {
          ...
        }
      },
    ]
  }
}
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_model_client
from alfresco_model_client.models.type_paging import TypePaging
from alfresco_model_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_model_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_model_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_model_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_model_client.TypesApi(api_client)
    where = 'where_example' # str | Optionally filter the list. Here are some examples:  A type should represented in the following format(`prefix:name`). e.g 'cm:content'.  The following where clause will only return types from the `namespace1:model` and `namespace2:model`.   ```   where=(modelId in ('namespace1:model','namespace2:model'))   where=(modelId in ('namespace1:model INCLUDESUBTYPES','namespace2:model'))   ```  The following where clause will only return sub types for the given parents.   ```   where=(parentId in ('namespace1:parent','namespace2:parent'))   ```  The following where clause will only return types that match the pattern.   ```   where=(namespaceUri matches('http://www.alfresco.*'))   ```  The following where clause will only return types that don't match the pattern.   ```   where=(not namespaceUri matches('http://www.alfresco.*'))   ```  (optional)
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    include = ['include_example'] # List[str] | Returns additional information about the type. The following optional fields can be requested: * properties * mandatoryAspects * associations  (optional)

    try:
        # List types
        api_response = api_instance.list_types(where=where, skip_count=skip_count, max_items=max_items, include=include)
        print("The response of TypesApi->list_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesApi->list_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Optionally filter the list. Here are some examples:  A type should represented in the following format(&#x60;prefix:name&#x60;). e.g &#39;cm:content&#39;.  The following where clause will only return types from the &#x60;namespace1:model&#x60; and &#x60;namespace2:model&#x60;.   &#x60;&#x60;&#x60;   where&#x3D;(modelId in (&#39;namespace1:model&#39;,&#39;namespace2:model&#39;))   where&#x3D;(modelId in (&#39;namespace1:model INCLUDESUBTYPES&#39;,&#39;namespace2:model&#39;))   &#x60;&#x60;&#x60;  The following where clause will only return sub types for the given parents.   &#x60;&#x60;&#x60;   where&#x3D;(parentId in (&#39;namespace1:parent&#39;,&#39;namespace2:parent&#39;))   &#x60;&#x60;&#x60;  The following where clause will only return types that match the pattern.   &#x60;&#x60;&#x60;   where&#x3D;(namespaceUri matches(&#39;http://www.alfresco.*&#39;))   &#x60;&#x60;&#x60;  The following where clause will only return types that don&#39;t match the pattern.   &#x60;&#x60;&#x60;   where&#x3D;(not namespaceUri matches(&#39;http://www.alfresco.*&#39;))   &#x60;&#x60;&#x60;  | [optional] 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **include** | [**List[str]**](str.md)| Returns additional information about the type. The following optional fields can be requested: * properties * mandatoryAspects * associations  | [optional] 

### Return type

[**TypePaging**](TypePaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

