# PersonPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[PersonEntry]**](PersonEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.person_paging_list import PersonPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of PersonPagingList from a JSON string
person_paging_list_instance = PersonPagingList.from_json(json)
# print the JSON string representation of the object
print(PersonPagingList.to_json())

# convert the object into a dict
person_paging_list_dict = person_paging_list_instance.to_dict()
# create an instance of PersonPagingList from a dict
person_paging_list_from_dict = PersonPagingList.from_dict(person_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


