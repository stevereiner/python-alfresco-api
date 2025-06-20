# NodeBodyCreateAssociation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_type** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.node_body_create_association import NodeBodyCreateAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBodyCreateAssociation from a JSON string
node_body_create_association_instance = NodeBodyCreateAssociation.from_json(json)
# print the JSON string representation of the object
print(NodeBodyCreateAssociation.to_json())

# convert the object into a dict
node_body_create_association_dict = node_body_create_association_instance.to_dict()
# create an instance of NodeBodyCreateAssociation from a dict
node_body_create_association_from_dict = NodeBodyCreateAssociation.from_dict(node_body_create_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


