# Comment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_delete** | **bool** |  | 
**can_edit** | **bool** |  | 
**content** | **str** |  | 
**created_at** | **datetime** |  | 
**created_by** | [**Person**](Person.md) |  | 
**edited** | **bool** |  | 
**id** | **str** |  | 
**modified_at** | **datetime** |  | 
**modified_by** | [**Person**](Person.md) |  | 
**title** | **str** |  | 

## Example

```python
from alfresco_core_client.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


