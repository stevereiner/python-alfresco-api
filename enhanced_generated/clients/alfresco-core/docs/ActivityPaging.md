# ActivityPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ActivityPagingList**](ActivityPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.activity_paging import ActivityPaging

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityPaging from a JSON string
activity_paging_instance = ActivityPaging.from_json(json)
# print the JSON string representation of the object
print(ActivityPaging.to_json())

# convert the object into a dict
activity_paging_dict = activity_paging_instance.to_dict()
# create an instance of ActivityPaging from a dict
activity_paging_from_dict = ActivityPaging.from_dict(activity_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


