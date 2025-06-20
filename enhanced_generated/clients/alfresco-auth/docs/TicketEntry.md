# TicketEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Ticket**](Ticket.md) |  | 

## Example

```python
from alfresco_auth_client.models.ticket_entry import TicketEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TicketEntry from a JSON string
ticket_entry_instance = TicketEntry.from_json(json)
# print the JSON string representation of the object
print(TicketEntry.to_json())

# convert the object into a dict
ticket_entry_dict = ticket_entry_instance.to_dict()
# create an instance of TicketEntry from a dict
ticket_entry_from_dict = TicketEntry.from_dict(ticket_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


