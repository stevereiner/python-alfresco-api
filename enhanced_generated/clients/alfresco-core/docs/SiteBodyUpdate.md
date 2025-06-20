# SiteBodyUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.site_body_update import SiteBodyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SiteBodyUpdate from a JSON string
site_body_update_instance = SiteBodyUpdate.from_json(json)
# print the JSON string representation of the object
print(SiteBodyUpdate.to_json())

# convert the object into a dict
site_body_update_dict = site_body_update_instance.to_dict()
# create an instance of SiteBodyUpdate from a dict
site_body_update_from_dict = SiteBodyUpdate.from_dict(site_body_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


