# alfresco_workflow_client.ProcessesApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/workflow/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_process**](ProcessesApi.md#create_process) | **POST** /processes | Create a process
[**create_process_item**](ProcessesApi.md#create_process_item) | **POST** /processes/{processId}/items | Create an item
[**create_process_variable**](ProcessesApi.md#create_process_variable) | **PUT** /processes/{processId}/variables/{variableName} | Create or update a variable
[**create_process_variables**](ProcessesApi.md#create_process_variables) | **POST** /processes/{processId}/variables | Create or update variables
[**delete_process**](ProcessesApi.md#delete_process) | **DELETE** /processes/{processId} | Delete a process
[**delete_process_item**](ProcessesApi.md#delete_process_item) | **DELETE** /processes/{processId}/items/{itemId} | Delete an item
[**delete_process_variable**](ProcessesApi.md#delete_process_variable) | **DELETE** /processes/{processId}/variables/{variableName} | Delete a variable
[**get_process**](ProcessesApi.md#get_process) | **GET** /processes/{processId} | Get a process
[**list_process_items**](ProcessesApi.md#list_process_items) | **GET** /processes/{processId}/items | List items
[**list_process_variables**](ProcessesApi.md#list_process_variables) | **GET** /processes/{processId}/variables | List variables
[**list_processes**](ProcessesApi.md#list_processes) | **GET** /processes | List processes


# **create_process**
> ProcessEntry create_process(process_body)

Create a process

Creates a new process.

In non-network deployments, any authenticated user can start a new process for
any process definition.

If networks are enabled, the authenticated user can start a new process for a
process definition in the user's network.

**Note:** You can start more than one process by
specifying a list of process entries in the JSON body like this:

```JSON
[
  {
     "processDefinitionKey": "activitiAdhoc",
     "variables": {
        "bpm_assignee": "fred"
    }
  },
  {
     "processDefinitionKey": "activitiAdhoc",
     "variables": {
        "bpm_assignee": "joe"
    }
]
```
If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:

```JSON
{
  "list": {
    "pagination": {
      "count": 2,
      "hasMoreItems": false,
      "totalItems": 2,
      "skipCount": 0,
      "maxItems": 100
    },
    "entries": [
      {
        "entry": {
          ...
        }
      },
      {
        "entry": {
          ...
        }
      }
    ]
  }
}
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.process_body import ProcessBody
from alfresco_workflow_client.models.process_entry import ProcessEntry
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    process_body = alfresco_workflow_client.ProcessBody() # ProcessBody | process properties

    try:
        # Create a process
        api_response = api_instance.create_process(process_body)
        print("The response of ProcessesApi->create_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->create_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_body** | [**ProcessBody**](ProcessBody.md)| process properties | 

### Return type

[**ProcessEntry**](ProcessEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **processBody** is invalid  |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_process_item**
> ItemPaging create_process_item(process_id, item_body)

Create an item

Creates an item for process **processId**".

If the item  already is part of that process the request will have no effect.

**Note:** You can create more than one item by
specifying a list of items in the JSON body like this:

```JSON
[
  {
     "id": "1ff9da1a-ee2f-4b9c-8c34-44665e844444"
  },
  {
     "id": "1ff9da1a-ee2f-4b9c-8c34-44665e855555"
  }
]
```
If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:

```JSON
{
  "list": {
    "pagination": {
      "count": 2,
      "hasMoreItems": false,
      "totalItems": 2,
      "skipCount": 0,
      "maxItems": 100
    },
    "entries": [
      {
        "entry": {
          ...
        }
      },
      {
        "entry": {
          ...
        }
      }
    ]
  }
}
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.item_body import ItemBody
from alfresco_workflow_client.models.item_paging import ItemPaging
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | The identifier of a process.
    item_body = alfresco_workflow_client.ItemBody() # ItemBody | The **nodeId** of the item

    try:
        # Create an item
        api_response = api_instance.create_process_item(process_id, item_body)
        print("The response of ProcessesApi->create_process_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->create_process_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The identifier of a process. | 
 **item_body** | [**ItemBody**](ItemBody.md)| The **nodeId** of the item | 

### Return type

[**ItemPaging**](ItemPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Invalid parameter: **itemBody** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **processId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_process_variable**
> VariableEntry create_process_variable(process_id, variable_name, variable_body)

Create or update a variable

Creates or updates a specific variable **variableName** for process **processId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.variable_body import VariableBody
from alfresco_workflow_client.models.variable_entry import VariableEntry
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | The identifier of a process.
    variable_name = 'variable_name_example' # str | The name of a variable.
    variable_body = alfresco_workflow_client.VariableBody() # VariableBody | A variable

    try:
        # Create or update a variable
        api_response = api_instance.create_process_variable(process_id, variable_name, variable_body)
        print("The response of ProcessesApi->create_process_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->create_process_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The identifier of a process. | 
 **variable_name** | **str**| The name of a variable. | 
 **variable_body** | [**VariableBody**](VariableBody.md)| A variable | 

### Return type

[**VariableEntry**](VariableEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **variableBody** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **processId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_process_variables**
> VariableEntry create_process_variables(process_id, variable_body)

Create or update variables

Create or update a variable for a given process.
If the variable does not exist yet, it will be created.        


**Note:** You can create or update more than one variable by 
specifying a list of variables in the JSON body like this:

```JSON
[
  {
    "name": "string",
    "value": "string",
    "type": "string"
  },
  {
    "name": "string",
    "value": "string",
    "type": "string"
  }
]
```
If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:

```JSON
{
  "list": {
    "pagination": {
      "count": 2,
      "hasMoreItems": false,
      "totalItems": 2,
      "skipCount": 0,
      "maxItems": 100
    },
    "entries": [
      {
        "entry": {
          ...
        }
      },
      {
        "entry": {
         ...
        }
      }
    ]
  }
}
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.variable_body import VariableBody
from alfresco_workflow_client.models.variable_entry import VariableEntry
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | The identifier of a process.
    variable_body = alfresco_workflow_client.VariableBody() # VariableBody | A variable

    try:
        # Create or update variables
        api_response = api_instance.create_process_variables(process_id, variable_body)
        print("The response of ProcessesApi->create_process_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->create_process_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The identifier of a process. | 
 **variable_body** | [**VariableBody**](VariableBody.md)| A variable | 

### Return type

[**VariableEntry**](VariableEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Invalid parameter: **variableBody** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **processId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_process**
> delete_process(process_id)

Delete a process

Deletes the process with the specified **processId**.

### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | The identifier of a process.

    try:
        # Delete a process
        api_instance.delete_process(process_id)
    except Exception as e:
        print("Exception when calling ProcessesApi->delete_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The identifier of a process. | 

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
**401** | Authentication failed |  -  |
**404** | The processId does not exist |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_process_item**
> delete_process_item(process_id, item_id)

Delete an item

Deletes the item with the specified **itemId** from the process with the specified **processId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | The identifier of a process.
    item_id = 'item_id_example' # str | The identifier of an item.

    try:
        # Delete an item
        api_instance.delete_process_item(process_id, item_id)
    except Exception as e:
        print("Exception when calling ProcessesApi->delete_process_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The identifier of a process. | 
 **item_id** | **str**| The identifier of an item. | 

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
**401** | Authentication failed |  -  |
**404** | The **processId** does not exist or the **itemId** does not exist |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_process_variable**
> delete_process_variable(process_id, variable_name)

Delete a variable

Deletes the variable **variableName** from the process with the specified **processId**.

### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | The identifier of a process.
    variable_name = 'variable_name_example' # str | The name of a variable.

    try:
        # Delete a variable
        api_instance.delete_process_variable(process_id, variable_name)
    except Exception as e:
        print("Exception when calling ProcessesApi->delete_process_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The identifier of a process. | 
 **variable_name** | **str**| The name of a variable. | 

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
**401** | Authentication failed |  -  |
**404** | The **processId** does not exist or the **variableName** does not exist |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process**
> ProcessEntry get_process(process_id, properties=properties)

Get a process

Gets the process identified by **processId**.

An authenticated user will have access to a process if the user has
started the process or if the user is involved in any of the process’s
tasks. In a network, only processes that are inside the given network are
returned.

In non-network deployments, administrators can see all processes and
perform all operations on tasks. In network deployments, network
administrators can see all processes in their network and perform all
operations on tasks in their network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.process_entry import ProcessEntry
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | The identifier of a process.
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # Get a process
        api_response = api_instance.get_process(process_id, properties=properties)
        print("The response of ProcessesApi->get_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->get_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The identifier of a process. | 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 

### Return type

[**ProcessEntry**](ProcessEntry.md)

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
**404** | **processId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_process_items**
> ItemPaging list_process_items(process_id, skip_count=skip_count, max_items=max_items, properties=properties)

List items

Gets a list of items for the specified process **processId**.

An authenticated user will have access to a processes items if the
user has started the process or if the user is involved in any of the
process’s tasks.  In a network, only items for a process that is
inside the given network are returned.

In non-network deployments, administrators can see all items and
perform all operations  on those items. In network deployments,
network administrators can see all items in their network and
perform all operations on items in their network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.item_paging import ItemPaging
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | The identifier of a process.
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # List items
        api_response = api_instance.list_process_items(process_id, skip_count=skip_count, max_items=max_items, properties=properties)
        print("The response of ProcessesApi->list_process_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->list_process_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The identifier of a process. | 
 **skip_count** | **int**| The number of entities that  exist in the collection before those included in this list. | [optional] 
 **max_items** | **int**| The maximum number of items to return in the list. | [optional] 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 

### Return type

[**ItemPaging**](ItemPaging.md)

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
**404** | **processId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_process_variables**
> VariablePaging list_process_variables(process_id, skip_count=skip_count, max_items=max_items, properties=properties)

List variables

Gets a list of variables for the process **processId**.

An authenticated user will have access to a processes variables if the
user has started  the process or if the user is involved in any of the
process’s tasks.  In a network, only variables for a process that is
inside the given network are returned.

In non-network deployments, administrators can see all variables and
perform all operations  on those variable. In network deployments,
network administrators can see all variables in  their network and
perform all operations on variables in their network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.variable_paging import VariablePaging
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | The identifier of a process.
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # List variables
        api_response = api_instance.list_process_variables(process_id, skip_count=skip_count, max_items=max_items, properties=properties)
        print("The response of ProcessesApi->list_process_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->list_process_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The identifier of a process. | 
 **skip_count** | **int**| The number of entities that  exist in the collection before those included in this list. | [optional] 
 **max_items** | **int**| The maximum number of items to return in the list. | [optional] 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 

### Return type

[**VariablePaging**](VariablePaging.md)

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
**404** | **processId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_processes**
> ProcessPaging list_processes(skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)

List processes

Gets a  list of processes.

An authenticated user will have access to a processes if the user has
started the process or if the user is involved in any of the process’s
tasks. In a network, only processes that are inside the given network are
returned.

In non-network deployments, any authenticated user will see all the
process definitions.

If networks are enabled, the network admin can only see the deployments
in the given network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.process_paging import ProcessPaging
from alfresco_workflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/workflow/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_workflow_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/workflow/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_workflow_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_workflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_workflow_client.ProcessesApi(api_client)
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderby** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
    where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)

    try:
        # List processes
        api_response = api_instance.list_processes(skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)
        print("The response of ProcessesApi->list_processes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->list_processes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that  exist in the collection before those included in this list. | [optional] 
 **max_items** | **int**| The maximum number of items to return in the list. | [optional] 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 
 **order_by** | [**List[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderby** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 

### Return type

[**ProcessPaging**](ProcessPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems**, **skipCount**, **orderBy**, or **where** is invalid  |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

