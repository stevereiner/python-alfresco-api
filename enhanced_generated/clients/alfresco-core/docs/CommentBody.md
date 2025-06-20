# CommentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 

## Example

```python
from alfresco_core_client.models.comment_body import CommentBody

# TODO update the JSON string below
json = "{}"
# create an instance of CommentBody from a JSON string
comment_body_instance = CommentBody.from_json(json)
# print the JSON string representation of the object
print(CommentBody.to_json())

# convert the object into a dict
comment_body_dict = comment_body_instance.to_dict()
# create an instance of CommentBody from a dict
comment_body_from_dict = CommentBody.from_dict(comment_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


