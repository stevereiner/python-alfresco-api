# RenditionPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**RenditionPagingList**](RenditionPagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.rendition_paging import RenditionPaging

# TODO update the JSON string below
json = "{}"
# create an instance of RenditionPaging from a JSON string
rendition_paging_instance = RenditionPaging.from_json(json)
# print the JSON string representation of the object
print(RenditionPaging.to_json())

# convert the object into a dict
rendition_paging_dict = rendition_paging_instance.to_dict()
# create an instance of RenditionPaging from a dict
rendition_paging_from_dict = RenditionPaging.from_dict(rendition_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


