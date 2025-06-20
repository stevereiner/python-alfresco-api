# PersonNetworkPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[PersonNetworkEntry]**](PersonNetworkEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.person_network_paging_list import PersonNetworkPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of PersonNetworkPagingList from a JSON string
person_network_paging_list_instance = PersonNetworkPagingList.from_json(json)
# print the JSON string representation of the object
print(PersonNetworkPagingList.to_json())

# convert the object into a dict
person_network_paging_list_dict = person_network_paging_list_instance.to_dict()
# create an instance of PersonNetworkPagingList from a dict
person_network_paging_list_from_dict = PersonNetworkPagingList.from_dict(person_network_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


