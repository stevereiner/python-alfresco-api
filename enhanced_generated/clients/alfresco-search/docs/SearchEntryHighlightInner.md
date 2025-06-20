# SearchEntryHighlightInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field where a match occured (one of the fields defined on the request) | [optional] 
**snippets** | **List[str]** | Any number of snippets for the specified field highlighting the matching text | [optional] 

## Example

```python
from alfresco_search_client.models.search_entry_highlight_inner import SearchEntryHighlightInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEntryHighlightInner from a JSON string
search_entry_highlight_inner_instance = SearchEntryHighlightInner.from_json(json)
# print the JSON string representation of the object
print(SearchEntryHighlightInner.to_json())

# convert the object into a dict
search_entry_highlight_inner_dict = search_entry_highlight_inner_instance.to_dict()
# create an instance of SearchEntryHighlightInner from a dict
search_entry_highlight_inner_from_dict = SearchEntryHighlightInner.from_dict(search_entry_highlight_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


