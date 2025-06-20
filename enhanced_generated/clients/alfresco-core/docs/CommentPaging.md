# CommentPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**CommentPagingList**](CommentPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.comment_paging import CommentPaging

# TODO update the JSON string below
json = "{}"
# create an instance of CommentPaging from a JSON string
comment_paging_instance = CommentPaging.from_json(json)
# print the JSON string representation of the object
print(CommentPaging.to_json())

# convert the object into a dict
comment_paging_dict = comment_paging_instance.to_dict()
# create an instance of CommentPaging from a dict
comment_paging_from_dict = CommentPaging.from_dict(comment_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


