# PersonNetworkPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**PersonNetworkPagingList**](PersonNetworkPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.person_network_paging import PersonNetworkPaging

# TODO update the JSON string below
json = "{}"
# create an instance of PersonNetworkPaging from a JSON string
person_network_paging_instance = PersonNetworkPaging.from_json(json)
# print the JSON string representation of the object
print(PersonNetworkPaging.to_json())

# convert the object into a dict
person_network_paging_dict = person_network_paging_instance.to_dict()
# create an instance of PersonNetworkPaging from a dict
person_network_paging_from_dict = PersonNetworkPaging.from_dict(person_network_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


