# ClientBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | **str** | the client name | 

## Example

```python
from alfresco_core_client.models.client_body import ClientBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClientBody from a JSON string
client_body_instance = ClientBody.from_json(json)
# print the JSON string representation of the object
print(ClientBody.to_json())

# convert the object into a dict
client_body_dict = client_body_instance.to_dict()
# create an instance of ClientBody from a dict
client_body_from_dict = ClientBody.from_dict(client_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


