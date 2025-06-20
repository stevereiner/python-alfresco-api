# SharedLinkBodyEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**recipient_emails** | **List[str]** |  | [optional] 

## Example

```python
from alfresco_core_client.models.shared_link_body_email import SharedLinkBodyEmail

# TODO update the JSON string below
json = "{}"
# create an instance of SharedLinkBodyEmail from a JSON string
shared_link_body_email_instance = SharedLinkBodyEmail.from_json(json)
# print the JSON string representation of the object
print(SharedLinkBodyEmail.to_json())

# convert the object into a dict
shared_link_body_email_dict = shared_link_body_email_instance.to_dict()
# create an instance of SharedLinkBodyEmail from a dict
shared_link_body_email_from_dict = SharedLinkBodyEmail.from_dict(shared_link_body_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


