# SearchEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**highlight** | [**List[SearchEntryHighlightInner]**](SearchEntryHighlightInner.md) | Highlight fragments if requested and available. A match can happen in any of the requested field.  | [optional] 
**score** | **float** | The score for this row | [optional] 

## Example

```python
from alfresco_search_client.models.search_entry import SearchEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEntry from a JSON string
search_entry_instance = SearchEntry.from_json(json)
# print the JSON string representation of the object
print(SearchEntry.to_json())

# convert the object into a dict
search_entry_dict = search_entry_instance.to_dict()
# create an instance of SearchEntry from a dict
search_entry_from_dict = SearchEntry.from_dict(search_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


