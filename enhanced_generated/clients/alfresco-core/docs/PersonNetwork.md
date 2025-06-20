# PersonNetwork

A network is the group of users and sites that belong to an organization. Networks are organized by email domain. When a user signs up for an Alfresco account , their email domain becomes their Home Network. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**home_network** | **bool** | Is this the home network? | [optional] 
**id** | **str** | This network&#39;s unique id | 
**is_enabled** | **bool** |  | 
**paid_network** | **bool** |  | [optional] 
**quotas** | [**List[NetworkQuota]**](NetworkQuota.md) |  | [optional] 
**subscription_level** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.person_network import PersonNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of PersonNetwork from a JSON string
person_network_instance = PersonNetwork.from_json(json)
# print the JSON string representation of the object
print(PersonNetwork.to_json())

# convert the object into a dict
person_network_dict = person_network_instance.to_dict()
# create an instance of PersonNetwork from a dict
person_network_from_dict = PersonNetwork.from_dict(person_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


