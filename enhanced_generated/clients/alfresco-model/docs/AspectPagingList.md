# AspectPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[AspectEntry]**](AspectEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_model_client.models.aspect_paging_list import AspectPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of AspectPagingList from a JSON string
aspect_paging_list_instance = AspectPagingList.from_json(json)
# print the JSON string representation of the object
print(AspectPagingList.to_json())

# convert the object into a dict
aspect_paging_list_dict = aspect_paging_list_instance.to_dict()
# create an instance of AspectPagingList from a dict
aspect_paging_list_from_dict = AspectPagingList.from_dict(aspect_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


