# alfresco_workflow_client.TasksApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/workflow/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_item**](TasksApi.md#create_task_item) | **POST** /tasks/{taskId}/items | Create an item
[**create_task_variables**](TasksApi.md#create_task_variables) | **POST** /tasks/{taskId}/variables | Create or update variables
[**delete_task_item**](TasksApi.md#delete_task_item) | **DELETE** /tasks/{taskId}/items/{itemId} | Delete an item
[**delete_task_variable**](TasksApi.md#delete_task_variable) | **DELETE** /tasks/{taskId}/variables/{variableName} | Delete a variable
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{taskId} | Get a task
[**get_task_form_model**](TasksApi.md#get_task_form_model) | **GET** /tasks/{taskId}/task-form-model | Get a task form model
[**list_task_candidates**](TasksApi.md#list_task_candidates) | **GET** /tasks/{taskId}/candidates | List task candidates
[**list_task_items**](TasksApi.md#list_task_items) | **GET** /tasks/{taskId}/items | List items
[**list_task_variables**](TasksApi.md#list_task_variables) | **GET** /tasks/{taskId}/variables | List variables
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /tasks | List tasks
[**list_tasks_for_process**](TasksApi.md#list_tasks_for_process) | **GET** /processes/{processId}/tasks | List tasks for a process
[**update_task**](TasksApi.md#update_task) | **PUT** /tasks/{taskId} | Update a task
[**update_task_variable**](TasksApi.md#update_task_variable) | **PUT** /tasks/{taskId}/variables/{variableName} | Create or update a variable


# **create_task_item**
> ItemPaging create_task_item(task_id, item_body)

Create an item

Creates an item for a given task **taskId**.

If the item  already is part of that task the request will have no effect.

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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    item_body = alfresco_workflow_client.ItemBody() # ItemBody | The nodeId of the item

    try:
        # Create an item
        api_response = api_instance.create_task_item(task_id, item_body)
        print("The response of TasksApi->create_task_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_task_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
 **item_body** | [**ItemBody**](ItemBody.md)| The nodeId of the item | 

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
**404** | **taskId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task_variables**
> VariableEntry create_task_variables(task_id, variable)

Create or update variables

Create or update a variable for the task **taskId**.
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
from alfresco_workflow_client.models.variable import Variable
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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    variable = alfresco_workflow_client.Variable() # Variable | A variable

    try:
        # Create or update variables
        api_response = api_instance.create_task_variables(task_id, variable)
        print("The response of TasksApi->create_task_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_task_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
 **variable** | [**Variable**](Variable.md)| A variable | 

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
**401** | Authentication failed |  -  |
**404** | **taskId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task_item**
> delete_task_item(task_id, item_id)

Delete an item

Deletes the item with the specified **itemId** from the task with the specified **taskId**.


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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    item_id = 'item_id_example' # str | The identifier of an item.

    try:
        # Delete an item
        api_instance.delete_task_item(task_id, item_id)
    except Exception as e:
        print("Exception when calling TasksApi->delete_task_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
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
**404** | The **taskId** does not exist or the **itemId** does not exist |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task_variable**
> delete_task_variable(task_id, variable_name)

Delete a variable

Deletes the variable with the specified **variableName** from the task with the specified **taskId**.


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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    variable_name = 'variable_name_example' # str | The name of a variable.

    try:
        # Delete a variable
        api_instance.delete_task_variable(task_id, variable_name)
    except Exception as e:
        print("Exception when calling TasksApi->delete_task_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
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
**404** | The **taskId** does not exist or the **variableName** does not exist |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> TaskEntry get_task(task_id, properties=properties)

Get a task

Gets the task identified by **taskId**.

An authenticated user will have access to a task if the user has
started the process or if the user is involved in any of the process’s
tasks. In a network, only tasks that are inside the given network are
returned.

In non-network deployments, administrators can see all processes and
perform all operations on tasks. In network deployments, network
administrators can see all processes in their network and perform all
operations on tasks in their network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.task_entry import TaskEntry
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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # Get a task
        api_response = api_instance.get_task(task_id, properties=properties)
        print("The response of TasksApi->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 

### Return type

[**TaskEntry**](TaskEntry.md)

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
**404** | **taskId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_form_model**
> TaskFormModelPaging get_task_form_model(task_id, skip_count=skip_count, max_items=max_items, properties=properties)

Get a task form model

Gets the model of the task form type definition.

An authenticated user will have access to  access to all task form models.
In a network, only task form models that are inside the given network
are returned.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.task_form_model_paging import TaskFormModelPaging
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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # Get a task form model
        api_response = api_instance.get_task_form_model(task_id, skip_count=skip_count, max_items=max_items, properties=properties)
        print("The response of TasksApi->get_task_form_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_form_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
 **skip_count** | **int**| The number of entities that  exist in the collection before those included in this list. | [optional] 
 **max_items** | **int**| The maximum number of items to return in the list. | [optional] 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 

### Return type

[**TaskFormModelPaging**](TaskFormModelPaging.md)

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
**404** | **taskId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_task_candidates**
> CandidatePaging list_task_candidates(task_id, skip_count=skip_count, max_items=max_items, properties=properties)

List task candidates

Gets a list of candidate users and groups for the specified task **taskId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.candidate_paging import CandidatePaging
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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # List task candidates
        api_response = api_instance.list_task_candidates(task_id, skip_count=skip_count, max_items=max_items, properties=properties)
        print("The response of TasksApi->list_task_candidates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_task_candidates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
 **skip_count** | **int**| The number of entities that  exist in the collection before those included in this list. | [optional] 
 **max_items** | **int**| The maximum number of items to return in the list. | [optional] 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 

### Return type

[**CandidatePaging**](CandidatePaging.md)

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
**404** | **taskId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_task_items**
> ItemPaging list_task_items(task_id, skip_count=skip_count, max_items=max_items, properties=properties)

List items

Gets a list of items for the specified task **taskId**.

An authenticated user will have access to a task's items if the
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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # List items
        api_response = api_instance.list_task_items(task_id, skip_count=skip_count, max_items=max_items, properties=properties)
        print("The response of TasksApi->list_task_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_task_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
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
**404** | **taskId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_task_variables**
> VariablePaging list_task_variables(task_id, skip_count=skip_count, max_items=max_items, properties=properties, where=where)

List variables

Gets a list of variables for the specified task **taskId**.

An authenticated user will have access to a tasks variables if the
user has started the process or if the user is involved in any of the
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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)
    where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)

    try:
        # List variables
        api_response = api_instance.list_task_variables(task_id, skip_count=skip_count, max_items=max_items, properties=properties, where=where)
        print("The response of TasksApi->list_task_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_task_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
 **skip_count** | **int**| The number of entities that  exist in the collection before those included in this list. | [optional] 
 **max_items** | **int**| The maximum number of items to return in the list. | [optional] 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 

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
**400** | Invalid parameter: value of **maxItems**, **skipCount**, or **where** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **taskId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> TaskPaging list_tasks(skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)

List tasks

Gets a list of tasks visible to the authenticated user.

Tasks are returned for which the authenticated user is the assignee  or
a candidate. If networks are enabled, the only tasks that are inside
the given network are returned.

In non-network deployments, administrators can see all processes and
perform all operations on tasks. In network deployments, network
administrators can see all processes in their network and perform all
operations on tasks in their network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.task_paging import TaskPaging
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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderby** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
    where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)

    try:
        # List tasks
        api_response = api_instance.list_tasks(skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)
        print("The response of TasksApi->list_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_tasks: %s\n" % e)
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

[**TaskPaging**](TaskPaging.md)

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

# **list_tasks_for_process**
> TaskPaging list_tasks_for_process(process_id, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by)

List tasks for a process

Gets a list of tasks for the specified process **processId**.

An authenticated user will have access to a processes tasks if the
user has started the process or if the user is involved in any of the
process’s tasks.  In a network, only tasks for a process that is
inside the given network are returned.

In non-network deployments, administrators can see all tasks and
perform all operations  on those tasks. In network deployments,
network administrators can see all tasks in their network and
perform all operations on tasks in their network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.task_paging import TaskPaging
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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    process_id = 'process_id_example' # str | The identifier of a process.
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderby** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)

    try:
        # List tasks for a process
        api_response = api_instance.list_tasks_for_process(process_id, skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by)
        print("The response of TasksApi->list_tasks_for_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_tasks_for_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The identifier of a process. | 
 **skip_count** | **int**| The number of entities that  exist in the collection before those included in this list. | [optional] 
 **max_items** | **int**| The maximum number of items to return in the list. | [optional] 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 
 **order_by** | [**List[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderby** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 

### Return type

[**TaskPaging**](TaskPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems**, **skipCount**, or **orderBy** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **processId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> TaskEntry update_task(task_id, task_body, select=select)

Update a task

Updates the state of the task **taskId**.

To perform a task action the authenticated user must be the assignee  or
a candidate. If networks is enabled, the task action is only
performed  if the task is inside the given network.

In non-network deployments, administrators can perform all operations
on  tasks. In network deployments, network administrators can see all
tasks  in their network and perform all operations on tasks in their
network.

You use the **select** parameter in the URL to specify a comma-separated list of
properties in the
task that you want to update. Use the JSON body to specify the new values for those
properties.

So for example to change the state of task **123** to **completed**, use
this URL
http://localhost:8080/alfresco/api/-default-/public/workflow/versions/1/tasks/123?select=state, and
provide this request body:

```JSON
{
  "state": "completed"
}
```
State Transitions
=================

Clients can invoke actions by assigning an allowed value to the state property of a task.
The select parameter can be used to allow for a partial update of the resource.
Alfresco will check for illegal state transitions and return an HTTP Bad Request (Response 400)
if an illegal state transition is attempted.
There are five state transitions, completing, claiming, unclaiming, delegating, resolving.

Completing a task
-----------------

If variables are included in the JSON body, they will be set in the task and then the process will continue.

To complete a task, the authenticated user must be the assignee of the task, the owner of the task, or have started the process.

In non-network deployments, administrators can perform this task operation on all tasks.
In network deployments, network administrators can perform this action on all tasks in their network.

Here's an example PUT request

```
/tasks/123?select=state,variables
```
Here's is a corresponding PUT request body:

```JSON
{
  “state : “completed”,
  “variables” : [
  {
    "name" : "bpm_priority",
    "type" : "d_int",
    "value" : 1,
    "scope" : "global"
  }
 ]
}
```

Claiming a task
-----------------

To claim a task, the authenticated user must be the assignee of the task,
the owner of the task, or have started the process.

Here's an example PUT request

```
/tasks/123?select=state
```
Here's a corresponding PUT request body:

```JSON
{
  “state : “claimed”
}
```

Unclaiming a task
-----------------

This removes the current assignee of the task.

To unclaim a task, the authenticated user must be the assignee of the task,
the owner of the task, or have started the process.

Here's an example PUT request

```
/tasks/123?select=state
```
Here's a corresponding PUT request body:

```JSON
{
  “state : “unclaimed”
}
```

Delegating a task
-----------------

This delegates the task from the owner to an assignee.
The result is the same as if the assignee had claimed the task,
but the task can then be resolved and the owner will
become the assignee again.

To delegate a task, the authenticated user must be the
assignee of the task and the assignee must be different from the owner.

Here's an example PUT request

```
/tasks/123?select=state,assignee
```
Here's a corresponding PUT request body:

```JSON
{
  “state : “delegated”,
  “assignee : “Kermit”
}
```
Resolving a task
-----------------

This returns a delegated task back to the owner.
In order to delegate a task, the authenticated user
must be the assignee of the task and the assignee must
be different from the owner.

To resolve a task, the authenticated user must be
the assignee of the task, the owner of the task,
or have started the process.

Here's an example PUT request

```
/tasks/123?select=state
```
Here's a corresponding PUT request body:

```JSON
{
  “state : “resolved”
}
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.task_body import TaskBody
from alfresco_workflow_client.models.task_entry import TaskEntry
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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    task_body = alfresco_workflow_client.TaskBody() # TaskBody | An object containing the properties to be updated
    select = 56 # int | A string specifying a required subset of properties to be returned for an entity or list of entities. Properties are separated by commas. (optional)

    try:
        # Update a task
        api_response = api_instance.update_task(task_id, task_body, select=select)
        print("The response of TasksApi->update_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->update_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
 **task_body** | [**TaskBody**](TaskBody.md)| An object containing the properties to be updated | 
 **select** | **int**| A string specifying a required subset of properties to be returned for an entity or list of entities. Properties are separated by commas. | [optional] 

### Return type

[**TaskEntry**](TaskEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **taskBody** is invalid  |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_variable**
> VariableEntry update_task_variable(task_id, variable_name, variable)

Create or update a variable

Creates or updates a specific variable **variableName** for a given task **taskId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.variable import Variable
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
    api_instance = alfresco_workflow_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The identifier of a task.
    variable_name = 'variable_name_example' # str | The name of a variable.
    variable = alfresco_workflow_client.Variable() # Variable | A variable

    try:
        # Create or update a variable
        api_response = api_instance.update_task_variable(task_id, variable_name, variable)
        print("The response of TasksApi->update_task_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->update_task_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The identifier of a task. | 
 **variable_name** | **str**| The name of a variable. | 
 **variable** | [**Variable**](Variable.md)| A variable | 

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
**404** | **taskId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

