# PreferencePagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[PreferenceEntry]**](PreferenceEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.preference_paging_list import PreferencePagingList

# TODO update the JSON string below
json = "{}"
# create an instance of PreferencePagingList from a JSON string
preference_paging_list_instance = PreferencePagingList.from_json(json)
# print the JSON string representation of the object
print(PreferencePagingList.to_json())

# convert the object into a dict
preference_paging_list_dict = preference_paging_list_instance.to_dict()
# create an instance of PreferencePagingList from a dict
preference_paging_list_from_dict = PreferencePagingList.from_dict(preference_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


