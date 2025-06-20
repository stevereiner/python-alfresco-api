# AspectPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**AspectPagingList**](AspectPagingList.md) |  | [optional] 

## Example

```python
from alfresco_model_client.models.aspect_paging import AspectPaging

# TODO update the JSON string below
json = "{}"
# create an instance of AspectPaging from a JSON string
aspect_paging_instance = AspectPaging.from_json(json)
# print the JSON string representation of the object
print(AspectPaging.to_json())

# convert the object into a dict
aspect_paging_dict = aspect_paging_instance.to_dict()
# create an instance of AspectPaging from a dict
aspect_paging_from_dict = AspectPaging.from_dict(aspect_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


