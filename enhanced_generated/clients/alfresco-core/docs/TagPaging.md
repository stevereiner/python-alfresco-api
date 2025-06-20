# TagPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**TagPagingList**](TagPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.tag_paging import TagPaging

# TODO update the JSON string below
json = "{}"
# create an instance of TagPaging from a JSON string
tag_paging_instance = TagPaging.from_json(json)
# print the JSON string representation of the object
print(TagPaging.to_json())

# convert the object into a dict
tag_paging_dict = tag_paging_instance.to_dict()
# create an instance of TagPaging from a dict
tag_paging_from_dict = TagPaging.from_dict(tag_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


