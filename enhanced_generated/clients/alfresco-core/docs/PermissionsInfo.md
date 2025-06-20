# PermissionsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inherited** | [**List[PermissionElement]**](PermissionElement.md) |  | [optional] 
**is_inheritance_enabled** | **bool** |  | [optional] 
**locally_set** | [**List[PermissionElement]**](PermissionElement.md) |  | [optional] 
**settable** | **List[str]** |  | [optional] 

## Example

```python
from alfresco_core_client.models.permissions_info import PermissionsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsInfo from a JSON string
permissions_info_instance = PermissionsInfo.from_json(json)
# print the JSON string representation of the object
print(PermissionsInfo.to_json())

# convert the object into a dict
permissions_info_dict = permissions_info_instance.to_dict()
# create an instance of PermissionsInfo from a dict
permissions_info_from_dict = PermissionsInfo.from_dict(permissions_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


