# LicenseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlements** | [**EntitlementsInfo**](EntitlementsInfo.md) |  | [optional] 
**expires_at** | **datetime** |  | 
**holder** | **str** |  | 
**issued_at** | **datetime** |  | 
**mode** | **str** |  | 
**remaining_days** | **int** |  | 

## Example

```python
from alfresco_discovery_client.models.license_info import LicenseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseInfo from a JSON string
license_info_instance = LicenseInfo.from_json(json)
# print the JSON string representation of the object
print(LicenseInfo.to_json())

# convert the object into a dict
license_info_dict = license_info_instance.to_dict()
# create an instance of LicenseInfo from a dict
license_info_from_dict = LicenseInfo.from_dict(license_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


