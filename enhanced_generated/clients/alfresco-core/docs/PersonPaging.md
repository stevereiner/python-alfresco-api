# PersonPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**PersonPagingList**](PersonPagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.person_paging import PersonPaging

# TODO update the JSON string below
json = "{}"
# create an instance of PersonPaging from a JSON string
person_paging_instance = PersonPaging.from_json(json)
# print the JSON string representation of the object
print(PersonPaging.to_json())

# convert the object into a dict
person_paging_dict = person_paging_instance.to_dict()
# create an instance of PersonPaging from a dict
person_paging_from_dict = PersonPaging.from_dict(person_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


