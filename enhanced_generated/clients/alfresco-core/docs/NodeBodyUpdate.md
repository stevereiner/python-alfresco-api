# NodeBodyUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_names** | **List[str]** |  | [optional] 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | [optional] 
**node_type** | **str** |  | [optional] 
**permissions** | [**PermissionsBody**](PermissionsBody.md) |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 

## Example

```python
from alfresco_core_client.models.node_body_update import NodeBodyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBodyUpdate from a JSON string
node_body_update_instance = NodeBodyUpdate.from_json(json)
# print the JSON string representation of the object
print(NodeBodyUpdate.to_json())

# convert the object into a dict
node_body_update_dict = node_body_update_instance.to_dict()
# create an instance of NodeBodyUpdate from a dict
node_body_update_from_dict = NodeBodyUpdate.from_dict(node_body_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


