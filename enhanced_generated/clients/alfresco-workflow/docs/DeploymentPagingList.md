# DeploymentPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[DeploymentEntry]**](DeploymentEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.deployment_paging_list import DeploymentPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentPagingList from a JSON string
deployment_paging_list_instance = DeploymentPagingList.from_json(json)
# print the JSON string representation of the object
print(DeploymentPagingList.to_json())

# convert the object into a dict
deployment_paging_list_dict = deployment_paging_list_instance.to_dict()
# create an instance of DeploymentPagingList from a dict
deployment_paging_list_from_dict = DeploymentPagingList.from_dict(deployment_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


