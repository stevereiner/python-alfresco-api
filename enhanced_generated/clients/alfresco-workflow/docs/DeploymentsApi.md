# alfresco_workflow_client.DeploymentsApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/workflow/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_deployment**](DeploymentsApi.md#delete_deployment) | **DELETE** /deployments/{deploymentId} | Delete a deployment
[**get_deployment**](DeploymentsApi.md#get_deployment) | **GET** /deployments/{deploymentId} | Get a deployment
[**list_deployments**](DeploymentsApi.md#list_deployments) | **GET** /deployments | List deployments


# **delete_deployment**
> delete_deployment(deployment_id)

Delete a deployment

This request will delete the deployment including the tasks, process definitions contained in the deployment.

The request will also delete processes and history information associated with the deployment.


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
    api_instance = alfresco_workflow_client.DeploymentsApi(api_client)
    deployment_id = 'deployment_id_example' # str | The unique id must be a String. It is returned as an **id** from the entity

    try:
        # Delete a deployment
        api_instance.delete_deployment(deployment_id)
    except Exception as e:
        print("Exception when calling DeploymentsApi->delete_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| The unique id must be a String. It is returned as an **id** from the entity | 

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> DeploymentEntry get_deployment(deployment_id, properties=properties)

Get a deployment

Gets a specified deployment defined by **deploymentId**.

The authenticated user must have role admin (non-network deployments) or
network admin (networks enabled).

If networks are enabled, the deployment is only returned if the deployment
is in the given network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.deployment_entry import DeploymentEntry
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
    api_instance = alfresco_workflow_client.DeploymentsApi(api_client)
    deployment_id = 'deployment_id_example' # str | The unique id must be a String. It is returned as an **id** from the entity.
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # Get a deployment
        api_response = api_instance.get_deployment(deployment_id, properties=properties)
        print("The response of DeploymentsApi->get_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->get_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| The unique id must be a String. It is returned as an **id** from the entity. | 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 

### Return type

[**DeploymentEntry**](DeploymentEntry.md)

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
**404** | **deploymentId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments**
> DeploymentPaging list_deployments(skip_count=skip_count, max_items=max_items, properties=properties)

List deployments

Gets a list of deployments.

The authenticated user must have role admin (non-network deployments) or
network admin (networks enabled).

If networks are enabled, the network admin can only see the deployments
in the given network.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_workflow_client
from alfresco_workflow_client.models.deployment_paging import DeploymentPaging
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
    api_instance = alfresco_workflow_client.DeploymentsApi(api_client)
    skip_count = 56 # int | The number of entities that  exist in the collection before those included in this list. (optional)
    max_items = 56 # int | The maximum number of items to return in the list. (optional)
    properties = ['properties_example'] # List[str] | A list of property names. You can use the properties parameter to restrict the number of returned properties. (optional)

    try:
        # List deployments
        api_response = api_instance.list_deployments(skip_count=skip_count, max_items=max_items, properties=properties)
        print("The response of DeploymentsApi->list_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->list_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that  exist in the collection before those included in this list. | [optional] 
 **max_items** | **int**| The maximum number of items to return in the list. | [optional] 
 **properties** | [**List[str]**](str.md)| A list of property names. You can use the properties parameter to restrict the number of returned properties. | [optional] 

### Return type

[**DeploymentPaging**](DeploymentPaging.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

