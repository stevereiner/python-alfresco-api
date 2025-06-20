# RepositoryInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edition** | **str** |  | 
**id** | **str** |  | 
**license** | [**LicenseInfo**](LicenseInfo.md) |  | [optional] 
**modules** | [**List[ModuleInfo]**](ModuleInfo.md) |  | [optional] 
**status** | [**StatusInfo**](StatusInfo.md) |  | 
**version** | [**VersionInfo**](VersionInfo.md) |  | 

## Example

```python
from alfresco_discovery_client.models.repository_info import RepositoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryInfo from a JSON string
repository_info_instance = RepositoryInfo.from_json(json)
# print the JSON string representation of the object
print(RepositoryInfo.to_json())

# convert the object into a dict
repository_info_dict = repository_info_instance.to_dict()
# create an instance of RepositoryInfo from a dict
repository_info_from_dict = RepositoryInfo.from_dict(repository_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


