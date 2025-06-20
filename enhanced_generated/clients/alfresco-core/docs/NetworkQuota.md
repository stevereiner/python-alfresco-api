# NetworkQuota

Limits and usage of each quota. A network will have quotas for File space, the number of sites in the network, the number of people in the network, and the number of network administrators 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**limit** | **int** |  | 
**usage** | **int** |  | 

## Example

```python
from alfresco_core_client.models.network_quota import NetworkQuota

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkQuota from a JSON string
network_quota_instance = NetworkQuota.from_json(json)
# print the JSON string representation of the object
print(NetworkQuota.to_json())

# convert the object into a dict
network_quota_dict = network_quota_instance.to_dict()
# create an instance of NetworkQuota from a dict
network_quota_from_dict = NetworkQuota.from_dict(network_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


