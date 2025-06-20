# Deployment

A deployment resource represents one file inside a deployment.  Process files, forms and perhaps some other files are authored in a separate environment. The act of deployment brings them into the runtime workflow engine.  A deployment is a collection of files that include all resources to specify one or more process definitions. After deployment, the included process definitions are known to the workflow runtime engine and new processes can be started.  Users can then continue to edit the process and other files in their authoring environment like e.g. our eclipse based process editor. A redeployment will result in a complete separate deployment containing new versions of the process definition.  When a process definition inside a new deployment has the same key as an existing process definition, then it is considered a new version of the existing process definition. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**deployed_at** | **datetime** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.deployment import Deployment

# TODO update the JSON string below
json = "{}"
# create an instance of Deployment from a JSON string
deployment_instance = Deployment.from_json(json)
# print the JSON string representation of the object
print(Deployment.to_json())

# convert the object into a dict
deployment_dict = deployment_instance.to_dict()
# create an instance of Deployment from a dict
deployment_from_dict = Deployment.from_dict(deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


