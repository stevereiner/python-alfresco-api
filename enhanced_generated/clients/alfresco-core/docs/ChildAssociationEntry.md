# ChildAssociationEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**ChildAssociation**](ChildAssociation.md) |  | 

## Example

```python
from alfresco_core_client.models.child_association_entry import ChildAssociationEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ChildAssociationEntry from a JSON string
child_association_entry_instance = ChildAssociationEntry.from_json(json)
# print the JSON string representation of the object
print(ChildAssociationEntry.to_json())

# convert the object into a dict
child_association_entry_dict = child_association_entry_instance.to_dict()
# create an instance of ChildAssociationEntry from a dict
child_association_entry_from_dict = ChildAssociationEntry.from_dict(child_association_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


