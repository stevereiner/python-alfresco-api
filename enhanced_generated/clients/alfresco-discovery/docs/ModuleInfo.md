# ModuleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**install_date** | **datetime** |  | [optional] 
**install_state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**version_max** | **str** |  | [optional] 
**version_min** | **str** |  | [optional] 

## Example

```python
from alfresco_discovery_client.models.module_info import ModuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleInfo from a JSON string
module_info_instance = ModuleInfo.from_json(json)
# print the JSON string representation of the object
print(ModuleInfo.to_json())

# convert the object into a dict
module_info_dict = module_info_instance.to_dict()
# create an instance of ModuleInfo from a dict
module_info_from_dict = ModuleInfo.from_dict(module_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


