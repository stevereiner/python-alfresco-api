# EntitlementsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_cluster_enabled** | **bool** |  | [optional] [default to False]
**is_cryptodoc_enabled** | **bool** |  | [optional] [default to False]
**max_docs** | **int** |  | [optional] 
**max_users** | **int** |  | [optional] 

## Example

```python
from alfresco_discovery_client.models.entitlements_info import EntitlementsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementsInfo from a JSON string
entitlements_info_instance = EntitlementsInfo.from_json(json)
# print the JSON string representation of the object
print(EntitlementsInfo.to_json())

# convert the object into a dict
entitlements_info_dict = entitlements_info_instance.to_dict()
# create an instance of EntitlementsInfo from a dict
entitlements_info_from_dict = EntitlementsInfo.from_dict(entitlements_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


