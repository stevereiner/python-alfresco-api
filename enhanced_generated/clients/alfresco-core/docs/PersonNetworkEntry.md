# PersonNetworkEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**PersonNetwork**](PersonNetwork.md) |  | 

## Example

```python
from alfresco_core_client.models.person_network_entry import PersonNetworkEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PersonNetworkEntry from a JSON string
person_network_entry_instance = PersonNetworkEntry.from_json(json)
# print the JSON string representation of the object
print(PersonNetworkEntry.to_json())

# convert the object into a dict
person_network_entry_dict = person_network_entry_instance.to_dict()
# create an instance of PersonNetworkEntry from a dict
person_network_entry_from_dict = PersonNetworkEntry.from_dict(person_network_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


