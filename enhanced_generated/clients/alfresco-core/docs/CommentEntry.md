# CommentEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Comment**](Comment.md) |  | 

## Example

```python
from alfresco_core_client.models.comment_entry import CommentEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CommentEntry from a JSON string
comment_entry_instance = CommentEntry.from_json(json)
# print the JSON string representation of the object
print(CommentEntry.to_json())

# convert the object into a dict
comment_entry_dict = comment_entry_instance.to_dict()
# create an instance of CommentEntry from a dict
comment_entry_from_dict = CommentEntry.from_dict(comment_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


