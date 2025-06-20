# PathInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**List[PathElement]**](PathElement.md) |  | [optional] 
**is_complete** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.path_info import PathInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PathInfo from a JSON string
path_info_instance = PathInfo.from_json(json)
# print the JSON string representation of the object
print(PathInfo.to_json())

# convert the object into a dict
path_info_dict = path_info_instance.to_dict()
# create an instance of PathInfo from a dict
path_info_from_dict = PathInfo.from_dict(path_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


