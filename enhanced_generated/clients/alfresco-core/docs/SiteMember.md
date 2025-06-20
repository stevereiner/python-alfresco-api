# SiteMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_member_of_group** | **bool** |  | [optional] 
**person** | [**Person**](Person.md) |  | 
**role** | **str** |  | 

## Example

```python
from alfresco_core_client.models.site_member import SiteMember

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMember from a JSON string
site_member_instance = SiteMember.from_json(json)
# print the JSON string representation of the object
print(SiteMember.to_json())

# convert the object into a dict
site_member_dict = site_member_instance.to_dict()
# create an instance of SiteMember from a dict
site_member_from_dict = SiteMember.from_dict(site_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


