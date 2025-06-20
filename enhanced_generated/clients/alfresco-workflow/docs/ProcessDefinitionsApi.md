# alfresco_workflow_client.ProcessDefinitionsApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/workflow/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_process_definition**](ProcessDefinitionsApi.md#get_process_definition) | **GET** /process-definitions/{processDefinitionId} | Get a process definition
[**get_process_definition_image**](ProcessDefinitionsApi.md#get_process_definition_image) | **GET** /process-definitions/{processDefinitionId}/image | Get a process definition image
[**get_process_definition_start_form_model**](ProcessDefinitionsApi.md#get_process_definition_start_form_model) | **GET** /process-definitions/{processDefinitionId}/start-form-model | Get a start form model
[**list_process_definitions**](ProcessDefinitionsApi.md#list_process_definitions) | **GET** /process-definitions | List process definitions


# **get_process_definition**
> ProcessDefinitionEntry get_process_definition(process_definition_id, properties=properties)

Get a process definition

Gets a process definition identified by **processDefinitionId**.

In non-network deployments, any authenticated user will see all the
process definitions. If networks are enabled, the network admin can only
see the deployments in the given network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.process_definition_entry import ProcessDefinitionEntry
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
    api_instance = alfresco_workflow_client.ProcessDefinitionsApi(api_client)
    process_definition_id = 'process_definition_id_example' # str | The identifier of a process definition.
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # Get a process definition
        api_response = api_instance.get_process_definition(process_definition_id, properties=properties)
        print("The response of ProcessDefinitionsApi->get_process_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessDefinitionsApi->get_process_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_definition_id** | **str**| The identifier of a process definition. | 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 

### Return type

[**ProcessDefinitionEntry**](ProcessDefinitionEntry.md)

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
**404** | **processDefinitionId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition_image**
> bytearray get_process_definition_image(process_definition_id)

Get a process definition image

Gets an image that represents a single process definition identified by **processDefinitionId**.

In non-network deployments, any authenticated user will see all the
process definitions.

If networks are enabled, the network admin can only see the deployments
in the given network.


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
    api_instance = alfresco_workflow_client.ProcessDefinitionsApi(api_client)
    process_definition_id = 'process_definition_id_example' # str | The identifier of a process definition.

    try:
        # Get a process definition image
        api_response = api_instance.get_process_definition_image(process_definition_id)
        print("The response of ProcessDefinitionsApi->get_process_definition_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessDefinitionsApi->get_process_definition_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_definition_id** | **str**| The identifier of a process definition. | 

### Return type

**bytearray**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **processDefinitionId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition_start_form_model**
> TaskFormModelPaging get_process_definition_start_form_model(process_definition_id, properties=properties)

Get a start form model

Gets a model of the start form type definition.

An authenticated user will have access to all start form models.
In a network, only start form models that are inside the given network are returned.


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
    api_instance = alfresco_workflow_client.ProcessDefinitionsApi(api_client)
    process_definition_id = 'process_definition_id_example' # str | The identifier of a process definition.
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # Get a start form model
        api_response = api_instance.get_process_definition_start_form_model(process_definition_id, properties=properties)
        print("The response of ProcessDefinitionsApi->get_process_definition_start_form_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessDefinitionsApi->get_process_definition_start_form_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_definition_id** | **str**| The identifier of a process definition. | 
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
**401** | Authentication failed |  -  |
**404** | **processDefinitionId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_process_definitions**
> ProcessDefinitionPaging list_process_definitions(skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)

List process definitions

Gets a list of process definitions.

In non-network deployments, any authenticated user will see all the
process definitions.

If networks are enabled, the network admin can only see the deployments
in the given network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.process_definition_paging import ProcessDefinitionPaging
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
    api_instance = alfresco_workflow_client.ProcessDefinitionsApi(api_client)
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderby** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
    where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)

    try:
        # List process definitions
        api_response = api_instance.list_process_definitions(skip_count=skip_count, max_items=max_items, properties=properties, order_by=order_by, where=where)
        print("The response of ProcessDefinitionsApi->list_process_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessDefinitionsApi->list_process_definitions: %s\n" % e)
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

[**ProcessDefinitionPaging**](ProcessDefinitionPaging.md)

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

