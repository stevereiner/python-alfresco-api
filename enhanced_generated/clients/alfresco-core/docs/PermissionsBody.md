# PermissionsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_inheritance_enabled** | **bool** |  | [optional] 
**locally_set** | [**List[PermissionElement]**](PermissionElement.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.permissions_body import PermissionsBody

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsBody from a JSON string
permissions_body_instance = PermissionsBody.from_json(json)
# print the JSON string representation of the object
print(PermissionsBody.to_json())

# convert the object into a dict
permissions_body_dict = permissions_body_instance.to_dict()
# create an instance of PermissionsBody from a dict
permissions_body_from_dict = PermissionsBody.from_dict(permissions_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


