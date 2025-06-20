# AuditAppEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**AuditApp**](AuditApp.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.audit_app_entry import AuditAppEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AuditAppEntry from a JSON string
audit_app_entry_instance = AuditAppEntry.from_json(json)
# print the JSON string representation of the object
print(AuditAppEntry.to_json())

# convert the object into a dict
audit_app_entry_dict = audit_app_entry_instance.to_dict()
# create an instance of AuditAppEntry from a dict
audit_app_entry_from_dict = AuditAppEntry.from_dict(audit_app_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


