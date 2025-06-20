# NodeBodyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_names** | **List[str]** |  | [optional] 
**association** | [**NodeBodyCreateAssociation**](NodeBodyCreateAssociation.md) |  | [optional] 
**definition** | [**Definition**](Definition.md) |  | [optional] 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | 
**node_type** | **str** |  | 
**permissions** | [**PermissionsBody**](PermissionsBody.md) |  | [optional] 
**properties** | **object** |  | [optional] 
**relative_path** | **str** |  | [optional] 
**secondary_children** | [**List[ChildAssociationBody]**](ChildAssociationBody.md) |  | [optional] 
**targets** | [**List[AssociationBody]**](AssociationBody.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.node_body_create import NodeBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBodyCreate from a JSON string
node_body_create_instance = NodeBodyCreate.from_json(json)
# print the JSON string representation of the object
print(NodeBodyCreate.to_json())

# convert the object into a dict
node_body_create_dict = node_body_create_instance.to_dict()
# create an instance of NodeBodyCreate from a dict
node_body_create_from_dict = NodeBodyCreate.from_dict(node_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


