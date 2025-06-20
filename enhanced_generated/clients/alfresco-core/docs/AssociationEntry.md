# AssociationEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Association**](Association.md) |  | 

## Example

```python
from alfresco_core_client.models.association_entry import AssociationEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationEntry from a JSON string
association_entry_instance = AssociationEntry.from_json(json)
# print the JSON string representation of the object
print(AssociationEntry.to_json())

# convert the object into a dict
association_entry_dict = association_entry_instance.to_dict()
# create an instance of AssociationEntry from a dict
association_entry_from_dict = AssociationEntry.from_dict(association_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


