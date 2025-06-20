# PreferencePaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**PreferencePagingList**](PreferencePagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.preference_paging import PreferencePaging

# TODO update the JSON string below
json = "{}"
# create an instance of PreferencePaging from a JSON string
preference_paging_instance = PreferencePaging.from_json(json)
# print the JSON string representation of the object
print(PreferencePaging.to_json())

# convert the object into a dict
preference_paging_dict = preference_paging_instance.to_dict()
# create an instance of PreferencePaging from a dict
preference_paging_from_dict = PreferencePaging.from_dict(preference_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


