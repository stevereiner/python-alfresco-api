# RevertBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**major_version** | **bool** |  | [optional] 

## Example

```python
from alfresco_core_client.models.revert_body import RevertBody

# TODO update the JSON string below
json = "{}"
# create an instance of RevertBody from a JSON string
revert_body_instance = RevertBody.from_json(json)
# print the JSON string representation of the object
print(RevertBody.to_json())

# convert the object into a dict
revert_body_dict = revert_body_instance.to_dict()
# create an instance of RevertBody from a dict
revert_body_from_dict = RevertBody.from_dict(revert_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


