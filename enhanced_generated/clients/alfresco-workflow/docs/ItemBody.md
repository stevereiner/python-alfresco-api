# ItemBody

The **nodeId** of the item 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.item_body import ItemBody

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBody from a JSON string
item_body_instance = ItemBody.from_json(json)
# print the JSON string representation of the object
print(ItemBody.to_json())

# convert the object into a dict
item_body_dict = item_body_instance.to_dict()
# create an instance of ItemBody from a dict
item_body_from_dict = ItemBody.from_dict(item_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


