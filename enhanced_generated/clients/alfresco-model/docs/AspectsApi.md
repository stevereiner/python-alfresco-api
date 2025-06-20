# alfresco_model_client.AspectsApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aspect**](AspectsApi.md#get_aspect) | **GET** /aspects/{aspectId} | Get an aspect
[**list_aspects**](AspectsApi.md#list_aspects) | **GET** /aspects | List aspects


# **get_aspect**
> AspectEntry get_aspect(aspect_id)

Get an aspect

**Note:** This is available in Alfresco 7.0.0 and newer versions.
Get information for aspect **aspectId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_model_client
from alfresco_model_client.models.aspect_entry import AspectEntry
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
    api_instance = alfresco_model_client.AspectsApi(api_client)
    aspect_id = 'aspect_id_example' # str | The Qname of an aspect(`prefix:name`) e.g 'cm:title'

    try:
        # Get an aspect
        api_response = api_instance.get_aspect(aspect_id)
        print("The response of AspectsApi->get_aspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AspectsApi->get_aspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aspect_id** | **str**| The Qname of an aspect(&#x60;prefix:name&#x60;) e.g &#39;cm:title&#39; | 

### Return type

[**AspectEntry**](AspectEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: unknown aspectId scheme specified  |  -  |
**401** | Authentication failed |  -  |
**404** | **aspectId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aspects**
> AspectPaging list_aspects(where=where, skip_count=skip_count, max_items=max_items, include=include)

List aspects

**Note:** This is available in Alfresco 7.0.0 and newer versions.

Gets a list of aspects from the data dictionary. The System aspects will be ignored by default.
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
          "mandatoryAspects": [],
          "includedInSupertypeQuery": true,
          "description": "Titled",
          "isContainer": false,
          "model": {
              "id": "cm:contentmodel",
              "author": "Alfresco",
              "description": "Alfresco Content Domain Model",
              "namespaceUri": "http://www.alfresco.org/model/content/1.0",
              "namespacePrefix": "cm"
          },
          "id": "cm:titled",
          "title": "Titled",
          "properties": [
            {
              "id": "cm:title",
              "title": "Title",
              "description": "Content Title",
              "dataType": "d:mltext",
              "isMultiValued": false,
              "isMandatory": false,
              "isMandatoryEnforced": false,
              "isProtected": false
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
from alfresco_model_client.models.aspect_paging import AspectPaging
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
    api_instance = alfresco_model_client.AspectsApi(api_client)
    where = 'where_example' # str | Optionally filter the list. Here are some examples:  An aspect should represented in the following format(`prefix:name`). e.g 'cm:title'.  The following where clause will only return aspects from the `namespace1:model` and `namespace2:model`.   ```   where=(modelId in ('namespace1:model','namespace2:model'))   where=(modelId in ('namespace1:model INCLUDESUBASPECTS','namespace2:model'))   ```  The following where clause will only return sub aspects for the given parents.   ```   where=(parentId in ('namespace1:parent','namespace2:parent'))   ```  The following where clause will only return aspects that match the pattern.   ```   where=(namespaceUri matches('http://www.alfresco.*'))   ```  The following where clause will only return aspects that don't match the pattern.   ```   where=(not namespaceUri matches('http://www.alfresco.*'))   ```  (optional)
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    include = ['include_example'] # List[str] | Returns additional information about the aspect. The following optional fields can be requested: * properties * mandatoryAspects * associations  (optional)

    try:
        # List aspects
        api_response = api_instance.list_aspects(where=where, skip_count=skip_count, max_items=max_items, include=include)
        print("The response of AspectsApi->list_aspects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AspectsApi->list_aspects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Optionally filter the list. Here are some examples:  An aspect should represented in the following format(&#x60;prefix:name&#x60;). e.g &#39;cm:title&#39;.  The following where clause will only return aspects from the &#x60;namespace1:model&#x60; and &#x60;namespace2:model&#x60;.   &#x60;&#x60;&#x60;   where&#x3D;(modelId in (&#39;namespace1:model&#39;,&#39;namespace2:model&#39;))   where&#x3D;(modelId in (&#39;namespace1:model INCLUDESUBASPECTS&#39;,&#39;namespace2:model&#39;))   &#x60;&#x60;&#x60;  The following where clause will only return sub aspects for the given parents.   &#x60;&#x60;&#x60;   where&#x3D;(parentId in (&#39;namespace1:parent&#39;,&#39;namespace2:parent&#39;))   &#x60;&#x60;&#x60;  The following where clause will only return aspects that match the pattern.   &#x60;&#x60;&#x60;   where&#x3D;(namespaceUri matches(&#39;http://www.alfresco.*&#39;))   &#x60;&#x60;&#x60;  The following where clause will only return aspects that don&#39;t match the pattern.   &#x60;&#x60;&#x60;   where&#x3D;(not namespaceUri matches(&#39;http://www.alfresco.*&#39;))   &#x60;&#x60;&#x60;  | [optional] 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **include** | [**List[str]**](str.md)| Returns additional information about the aspect. The following optional fields can be requested: * properties * mandatoryAspects * associations  | [optional] 

### Return type

[**AspectPaging**](AspectPaging.md)

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

