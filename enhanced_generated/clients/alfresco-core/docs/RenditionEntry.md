# RenditionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Rendition**](Rendition.md) |  | 

## Example

```python
from alfresco_core_client.models.rendition_entry import RenditionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RenditionEntry from a JSON string
rendition_entry_instance = RenditionEntry.from_json(json)
# print the JSON string representation of the object
print(RenditionEntry.to_json())

# convert the object into a dict
rendition_entry_dict = rendition_entry_instance.to_dict()
# create an instance of RenditionEntry from a dict
rendition_entry_from_dict = RenditionEntry.from_dict(rendition_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


