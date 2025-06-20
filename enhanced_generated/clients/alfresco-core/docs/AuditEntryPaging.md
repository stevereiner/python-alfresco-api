# AuditEntryPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**AuditEntryPagingList**](AuditEntryPagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.audit_entry_paging import AuditEntryPaging

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEntryPaging from a JSON string
audit_entry_paging_instance = AuditEntryPaging.from_json(json)
# print the JSON string representation of the object
print(AuditEntryPaging.to_json())

# convert the object into a dict
audit_entry_paging_dict = audit_entry_paging_instance.to_dict()
# create an instance of AuditEntryPaging from a dict
audit_entry_paging_from_dict = AuditEntryPaging.from_dict(audit_entry_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


