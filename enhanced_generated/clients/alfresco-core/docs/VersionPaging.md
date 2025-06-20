# VersionPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**VersionPagingList**](VersionPagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.version_paging import VersionPaging

# TODO update the JSON string below
json = "{}"
# create an instance of VersionPaging from a JSON string
version_paging_instance = VersionPaging.from_json(json)
# print the JSON string representation of the object
print(VersionPaging.to_json())

# convert the object into a dict
version_paging_dict = version_paging_instance.to_dict()
# create an instance of VersionPaging from a dict
version_paging_from_dict = VersionPaging.from_dict(version_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


