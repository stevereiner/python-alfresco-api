# alfresco_core_client.ActionsApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_details**](ActionsApi.md#action_details) | **GET** /action-definitions/{actionDefinitionId} | Retrieve the details of an action definition
[**action_exec**](ActionsApi.md#action_exec) | **POST** /action-executions | Execute an action
[**list_actions**](ActionsApi.md#list_actions) | **GET** /action-definitions | Retrieve list of available actions
[**node_actions**](ActionsApi.md#node_actions) | **GET** /nodes/{nodeId}/action-definitions | Retrieve actions for a node


# **action_details**
> ActionDefinitionEntry action_details(action_definition_id)

Retrieve the details of an action definition

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Retrieve the details of the action denoted by **actionDefinitionId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.action_definition_entry import ActionDefinitionEntry
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
    api_instance = alfresco_core_client.ActionsApi(api_client)
    action_definition_id = 'action_definition_id_example' # str | The identifier of an action definition.

    try:
        # Retrieve the details of an action definition
        api_response = api_instance.action_details(action_definition_id)
        print("The response of ActionsApi->action_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->action_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_definition_id** | **str**| The identifier of an action definition. | 

### Return type

[**ActionDefinitionEntry**](ActionDefinitionEntry.md)

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
**404** | **actionDefinitionId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_exec**
> ActionExecResultEntry action_exec(action_body_exec)

Execute an action

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Executes an action

An action may be executed against a node specified by **targetId**. For example:

```
{
  "actionDefinitionId": "copy",
  "targetId": "4c4b3c43-f18b-43ff-af84-751f16f1ddfd",
  "params": {
  	"destination-folder": "34219f79-66fa-4ebf-b371-118598af898c"
  }
}
```

Performing a POST with the request body shown above will result in the node identified by ```targetId```
being copied to the destination folder specified in the ```params``` object by the key ```destination-folder```.

**targetId** is optional, however, currently **targetId** must be a valid node ID.
In the future, actions may be executed against different entity types or
executed without the need for the context of an entity.


Parameters supplied to the action within the ```params``` object will be converted to the expected type,
where possible using the DefaultTypeConverter class. In addition:

* Node IDs may be supplied in their short form (implicit workspace://SpacesStore prefix)
* Aspect names may be supplied using their short form, e.g. cm:versionable or cm:auditable

In this example, we add the aspect ```cm:versionable``` to a node using the QName resolution mentioned above:

```
{
  "actionDefinitionId": "add-features",
  "targetId": "16349e3f-2977-44d1-93f2-73c12b8083b5",
  "params": {
  	"aspect-name": "cm:versionable"
  }
}
```

The ```actionDefinitionId``` is the ```id``` of an action definition as returned by
the _list actions_ operations (e.g. GET /action-definitions).

The action will be executed **asynchronously** with a `202` HTTP response signifying that
the request has been accepted successfully. The response body contains the unique ID of the action
pending execution. The ID may be used, for example to correlate an execution with output in the server logs.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.action_body_exec import ActionBodyExec
from alfresco_core_client.models.action_exec_result_entry import ActionExecResultEntry
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
    api_instance = alfresco_core_client.ActionsApi(api_client)
    action_body_exec = alfresco_core_client.ActionBodyExec() # ActionBodyExec | Action execution details

    try:
        # Execute an action
        api_response = api_instance.action_exec(action_body_exec)
        print("The response of ActionsApi->action_exec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->action_exec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_body_exec** | [**ActionBodyExec**](ActionBodyExec.md)| Action execution details | 

### Return type

[**ActionExecResultEntry**](ActionExecResultEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Action execution request accepted and pending execution.  |  -  |
**400** | Invalid parameter: **actionDefinitionId** missing but required by the action  |  -  |
**401** | Authentication failed |  -  |
**404** | **actionDefinitionId** or **targetId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_actions**
> ActionDefinitionList list_actions(skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)

Retrieve list of available actions

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

Gets a list of all available actions

The default sort order for the returned list is for actions to be sorted by ascending name.
You can override the default by using the **orderBy** parameter.

You can use any of the following fields to order the results:
* name
* title


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.action_definition_list import ActionDefinitionList
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
    api_instance = alfresco_core_client.ActionsApi(api_client)
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Retrieve list of available actions
        api_response = api_instance.list_actions(skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)
        print("The response of ActionsApi->list_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->list_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **order_by** | [**List[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**ActionDefinitionList**](ActionDefinitionList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems**, **skipCount** or **orderBy** is invalid  |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_actions**
> ActionDefinitionList node_actions(node_id, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)

Retrieve actions for a node

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Retrieve the list of actions that may be executed against the given **nodeId**.

The default sort order for the returned list is for actions to be sorted by ascending name.
You can override the default by using the **orderBy** parameter.

You can use any of the following fields to order the results:
* name
* title


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.action_definition_list import ActionDefinitionList
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
    api_instance = alfresco_core_client.ActionsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Retrieve actions for a node
        api_response = api_instance.node_actions(node_id, skip_count=skip_count, max_items=max_items, order_by=order_by, fields=fields)
        print("The response of ActionsApi->node_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->node_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **order_by** | [**List[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**ActionDefinitionList**](ActionDefinitionList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems**, **skipCount** or **orderBy** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **nodeId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

