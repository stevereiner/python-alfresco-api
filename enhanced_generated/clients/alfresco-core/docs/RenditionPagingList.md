# RenditionPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[RenditionEntry]**](RenditionEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.rendition_paging_list import RenditionPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of RenditionPagingList from a JSON string
rendition_paging_list_instance = RenditionPagingList.from_json(json)
# print the JSON string representation of the object
print(RenditionPagingList.to_json())

# convert the object into a dict
rendition_paging_list_dict = rendition_paging_list_instance.to_dict()
# create an instance of RenditionPagingList from a dict
rendition_paging_list_from_dict = RenditionPagingList.from_dict(rendition_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


