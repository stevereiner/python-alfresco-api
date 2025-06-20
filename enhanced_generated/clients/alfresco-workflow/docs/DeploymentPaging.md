# DeploymentPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**DeploymentPagingList**](DeploymentPagingList.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.deployment_paging import DeploymentPaging

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentPaging from a JSON string
deployment_paging_instance = DeploymentPaging.from_json(json)
# print the JSON string representation of the object
print(DeploymentPaging.to_json())

# convert the object into a dict
deployment_paging_dict = deployment_paging_instance.to_dict()
# create an instance of DeploymentPaging from a dict
deployment_paging_from_dict = DeploymentPaging.from_dict(deployment_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


