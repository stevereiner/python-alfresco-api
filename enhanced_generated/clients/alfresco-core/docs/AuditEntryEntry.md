# AuditEntryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**AuditEntry**](AuditEntry.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.audit_entry_entry import AuditEntryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEntryEntry from a JSON string
audit_entry_entry_instance = AuditEntryEntry.from_json(json)
# print the JSON string representation of the object
print(AuditEntryEntry.to_json())

# convert the object into a dict
audit_entry_entry_dict = audit_entry_entry_instance.to_dict()
# create an instance of AuditEntryEntry from a dict
audit_entry_entry_from_dict = AuditEntryEntry.from_dict(audit_entry_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


