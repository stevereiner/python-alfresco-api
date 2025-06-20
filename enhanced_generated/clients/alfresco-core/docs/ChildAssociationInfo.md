# ChildAssociationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assoc_type** | **str** |  | 
**is_primary** | **bool** |  | 

## Example

```python
from alfresco_core_client.models.child_association_info import ChildAssociationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChildAssociationInfo from a JSON string
child_association_info_instance = ChildAssociationInfo.from_json(json)
# print the JSON string representation of the object
print(ChildAssociationInfo.to_json())

# convert the object into a dict
child_association_info_dict = child_association_info_instance.to_dict()
# create an instance of ChildAssociationInfo from a dict
child_association_info_from_dict = ChildAssociationInfo.from_dict(child_association_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


