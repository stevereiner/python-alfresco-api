# Preference

A specific preference. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the preference | 
**value** | **str** | The value of the preference. Note that this can be of any JSON type. | [optional] 

## Example

```python
from alfresco_core_client.models.preference import Preference

# TODO update the JSON string below
json = "{}"
# create an instance of Preference from a JSON string
preference_instance = Preference.from_json(json)
# print the JSON string representation of the object
print(Preference.to_json())

# convert the object into a dict
preference_dict = preference_instance.to_dict()
# create an instance of Preference from a dict
preference_from_dict = Preference.from_dict(preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


