# SiteContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from alfresco_core_client.models.site_container import SiteContainer

# TODO update the JSON string below
json = "{}"
# create an instance of SiteContainer from a JSON string
site_container_instance = SiteContainer.from_json(json)
# print the JSON string representation of the object
print(SiteContainer.to_json())

# convert the object into a dict
site_container_dict = site_container_instance.to_dict()
# create an instance of SiteContainer from a dict
site_container_from_dict = SiteContainer.from_dict(site_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


