# TicketBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from alfresco_auth_client.models.ticket_body import TicketBody

# TODO update the JSON string below
json = "{}"
# create an instance of TicketBody from a JSON string
ticket_body_instance = TicketBody.from_json(json)
# print the JSON string representation of the object
print(TicketBody.to_json())

# convert the object into a dict
ticket_body_dict = ticket_body_instance.to_dict()
# create an instance of TicketBody from a dict
ticket_body_from_dict = TicketBody.from_dict(ticket_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


