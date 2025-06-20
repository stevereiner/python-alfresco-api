# SharedLinkBodyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | [optional] 
**node_id** | **str** |  | 

## Example

```python
from alfresco_core_client.models.shared_link_body_create import SharedLinkBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SharedLinkBodyCreate from a JSON string
shared_link_body_create_instance = SharedLinkBodyCreate.from_json(json)
# print the JSON string representation of the object
print(SharedLinkBodyCreate.to_json())

# convert the object into a dict
shared_link_body_create_dict = shared_link_body_create_instance.to_dict()
# create an instance of SharedLinkBodyCreate from a dict
shared_link_body_create_from_dict = SharedLinkBodyCreate.from_dict(shared_link_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


