# DeploymentEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Deployment**](Deployment.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.deployment_entry import DeploymentEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentEntry from a JSON string
deployment_entry_instance = DeploymentEntry.from_json(json)
# print the JSON string representation of the object
print(DeploymentEntry.to_json())

# convert the object into a dict
deployment_entry_dict = deployment_entry_instance.to_dict()
# create an instance of DeploymentEntry from a dict
deployment_entry_from_dict = DeploymentEntry.from_dict(deployment_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


