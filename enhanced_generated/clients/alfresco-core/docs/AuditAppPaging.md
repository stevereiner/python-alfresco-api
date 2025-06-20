# AuditAppPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**AuditAppPagingList**](AuditAppPagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.audit_app_paging import AuditAppPaging

# TODO update the JSON string below
json = "{}"
# create an instance of AuditAppPaging from a JSON string
audit_app_paging_instance = AuditAppPaging.from_json(json)
# print the JSON string representation of the object
print(AuditAppPaging.to_json())

# convert the object into a dict
audit_app_paging_dict = audit_app_paging_instance.to_dict()
# create an instance of AuditAppPaging from a dict
audit_app_paging_from_dict = AuditAppPaging.from_dict(audit_app_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


