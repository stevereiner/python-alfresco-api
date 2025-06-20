# alfresco_core_client.QueriesApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_nodes**](QueriesApi.md#find_nodes) | **GET** /queries/nodes | Find nodes
[**find_people**](QueriesApi.md#find_people) | **GET** /queries/people | Find people
[**find_sites**](QueriesApi.md#find_sites) | **GET** /queries/sites | Find sites


# **find_nodes**
> NodePaging find_nodes(term, root_node_id=root_node_id, skip_count=skip_count, max_items=max_items, node_type=node_type, include=include, order_by=order_by, fields=fields)

Find nodes

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Gets a list of nodes that match the given search criteria.

The search term is used to look for nodes that match against name, title, description, full text content or tags.

The search term:
- must contain a minimum of 3 alphanumeric characters
- allows "quoted term"
- can optionally use '*' for wildcard matching

By default, file and folder types will be searched unless a specific type is provided as a query parameter.

By default, the search will be across the repository unless a specific root node id is provided to start the search from.

You can sort the result list using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter:
* name
* modifiedAt
* createdAt


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.node_paging import NodePaging
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
    api_instance = alfresco_core_client.QueriesApi(api_client)
    term = 'term_example' # str | The term to search for.
    root_node_id = 'root_node_id_example' # str | The id of the node to start the search from.  Supports the aliases -my-, -root- and -shared-.  (optional)
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    node_type = 'node_type_example' # str | Restrict the returned results to only those of the given node type and its sub-types  (optional)
    include = ['include_example'] # List[str] | Returns additional information about the node. The following optional fields can be requested: * allowableOperations * aspectNames * isLink * isFavorite * isLocked * path * properties  (optional)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Find nodes
        api_response = api_instance.find_nodes(term, root_node_id=root_node_id, skip_count=skip_count, max_items=max_items, node_type=node_type, include=include, order_by=order_by, fields=fields)
        print("The response of QueriesApi->find_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueriesApi->find_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| The term to search for. | 
 **root_node_id** | **str**| The id of the node to start the search from.  Supports the aliases -my-, -root- and -shared-.  | [optional] 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **node_type** | **str**| Restrict the returned results to only those of the given node type and its sub-types  | [optional] 
 **include** | [**List[str]**](str.md)| Returns additional information about the node. The following optional fields can be requested: * allowableOperations * aspectNames * isLink * isFavorite * isLocked * path * properties  | [optional] 
 **order_by** | [**List[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**NodePaging**](NodePaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems** or **skipCount** is invalid, or search **term** too short, or **nodeType** unknown, or **orderBy** invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **rootNodeId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_people**
> PersonPaging find_people(term, skip_count=skip_count, max_items=max_items, fields=fields, order_by=order_by)

Find people

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Gets a list of people that match the given search criteria.

The search term is used to look for matches against person id, firstname and lastname.

The search term:
- must contain a minimum of 2 alphanumeric characters
- can optionally use '*' for wildcard matching within the term

You can sort the result list using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter:
* id
* firstName
* lastName


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.person_paging import PersonPaging
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
    api_instance = alfresco_core_client.QueriesApi(api_client)
    term = 'term_example' # str | The term to search for. 
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)

    try:
        # Find people
        api_response = api_instance.find_people(term, skip_count=skip_count, max_items=max_items, fields=fields, order_by=order_by)
        print("The response of QueriesApi->find_people:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueriesApi->find_people: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| The term to search for.  | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 
 **order_by** | [**List[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 

### Return type

[**PersonPaging**](PersonPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems** or **skipCount** is invalid, or search **term** too short, or **orderBy** invalid  |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_sites**
> SitePaging find_sites(term, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)

Find sites

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Gets a list of sites that match the given search criteria.

The search term is used to look for sites that match against site id, title or description.

The search term:
- must contain a minimum of 2 alphanumeric characters
- can optionally use '*' for wildcard matching within the term

The default sort order for the returned list is for sites to be sorted by ascending id.
You can override the default by using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter:
* id
* title
* description


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_paging import SitePaging
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
    api_instance = alfresco_core_client.QueriesApi(api_client)
    term = 'term_example' # str | The term to search for.
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Find sites
        api_response = api_instance.find_sites(term, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)
        print("The response of QueriesApi->find_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueriesApi->find_sites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| The term to search for. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **order_by** | [**List[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SitePaging**](SitePaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems** or **skipCount** is invalid, or search **term** too short, or **orderBy** invalid  |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

