# ValidTicketEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**ValidTicket**](ValidTicket.md) |  | 

## Example

```python
from alfresco_auth_client.models.valid_ticket_entry import ValidTicketEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ValidTicketEntry from a JSON string
valid_ticket_entry_instance = ValidTicketEntry.from_json(json)
# print the JSON string representation of the object
print(ValidTicketEntry.to_json())

# convert the object into a dict
valid_ticket_entry_dict = valid_ticket_entry_instance.to_dict()
# create an instance of ValidTicketEntry from a dict
valid_ticket_entry_from_dict = ValidTicketEntry.from_dict(valid_ticket_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


