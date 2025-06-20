# AuditEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_application_id** | **str** |  | 
**created_at** | **datetime** |  | 
**created_by_user** | [**UserInfo**](UserInfo.md) |  | 
**id** | **str** |  | 
**values** | **object** |  | [optional] 

## Example

```python
from alfresco_core_client.models.audit_entry import AuditEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEntry from a JSON string
audit_entry_instance = AuditEntry.from_json(json)
# print the JSON string representation of the object
print(AuditEntry.to_json())

# convert the object into a dict
audit_entry_dict = audit_entry_instance.to_dict()
# create an instance of AuditEntry from a dict
audit_entry_from_dict = AuditEntry.from_dict(audit_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


