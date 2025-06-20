# GroupPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**GroupPagingList**](GroupPagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.group_paging import GroupPaging

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPaging from a JSON string
group_paging_instance = GroupPaging.from_json(json)
# print the JSON string representation of the object
print(GroupPaging.to_json())

# convert the object into a dict
group_paging_dict = group_paging_instance.to_dict()
# create an instance of GroupPaging from a dict
group_paging_from_dict = GroupPaging.from_dict(group_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


