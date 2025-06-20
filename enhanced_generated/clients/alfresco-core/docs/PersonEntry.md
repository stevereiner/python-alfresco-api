# PersonEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Person**](Person.md) |  | 

## Example

```python
from alfresco_core_client.models.person_entry import PersonEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PersonEntry from a JSON string
person_entry_instance = PersonEntry.from_json(json)
# print the JSON string representation of the object
print(PersonEntry.to_json())

# convert the object into a dict
person_entry_dict = person_entry_instance.to_dict()
# create an instance of PersonEntry from a dict
person_entry_from_dict = PersonEntry.from_dict(person_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


