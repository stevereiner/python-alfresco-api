# PreferenceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Preference**](Preference.md) |  | 

## Example

```python
from alfresco_core_client.models.preference_entry import PreferenceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PreferenceEntry from a JSON string
preference_entry_instance = PreferenceEntry.from_json(json)
# print the JSON string representation of the object
print(PreferenceEntry.to_json())

# convert the object into a dict
preference_entry_dict = preference_entry_instance.to_dict()
# create an instance of PreferenceEntry from a dict
preference_entry_from_dict = PreferenceEntry.from_dict(preference_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


