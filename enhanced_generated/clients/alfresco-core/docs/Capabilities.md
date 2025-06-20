# Capabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_admin** | **bool** |  | [optional] 
**is_guest** | **bool** |  | [optional] 
**is_mutable** | **bool** |  | [optional] 

## Example

```python
from alfresco_core_client.models.capabilities import Capabilities

# TODO update the JSON string below
json = "{}"
# create an instance of Capabilities from a JSON string
capabilities_instance = Capabilities.from_json(json)
# print the JSON string representation of the object
print(Capabilities.to_json())

# convert the object into a dict
capabilities_dict = capabilities_instance.to_dict()
# create an instance of Capabilities from a dict
capabilities_from_dict = Capabilities.from_dict(capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


