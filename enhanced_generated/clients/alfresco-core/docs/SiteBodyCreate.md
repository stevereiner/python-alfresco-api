# SiteBodyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | 
**visibility** | **str** |  | [default to 'PUBLIC']

## Example

```python
from alfresco_core_client.models.site_body_create import SiteBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SiteBodyCreate from a JSON string
site_body_create_instance = SiteBodyCreate.from_json(json)
# print the JSON string representation of the object
print(SiteBodyCreate.to_json())

# convert the object into a dict
site_body_create_dict = site_body_create_instance.to_dict()
# create an instance of SiteBodyCreate from a dict
site_body_create_from_dict = SiteBodyCreate.from_dict(site_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


