# NodeAssociation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowable_operations** | **List[str]** |  | [optional] 
**aspect_names** | **List[str]** |  | [optional] 
**content** | [**ContentInfo**](ContentInfo.md) |  | [optional] 
**created_at** | **datetime** |  | 
**created_by_user** | [**UserInfo**](UserInfo.md) |  | 
**definition** | [**Definition**](Definition.md) |  | [optional] 
**id** | **str** |  | 
**is_favorite** | **bool** |  | [optional] 
**is_file** | **bool** |  | 
**is_folder** | **bool** |  | 
**is_link** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] [default to False]
**modified_at** | **datetime** |  | 
**modified_by_user** | [**UserInfo**](UserInfo.md) |  | 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | 
**node_type** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**path** | [**PathInfo**](PathInfo.md) |  | [optional] 
**permissions** | [**PermissionsInfo**](PermissionsInfo.md) |  | [optional] 
**properties** | **object** |  | [optional] 
**association** | [**AssociationInfo**](AssociationInfo.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.node_association import NodeAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAssociation from a JSON string
node_association_instance = NodeAssociation.from_json(json)
# print the JSON string representation of the object
print(NodeAssociation.to_json())

# convert the object into a dict
node_association_dict = node_association_instance.to_dict()
# create an instance of NodeAssociation from a dict
node_association_from_dict = NodeAssociation.from_dict(node_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


