# AbstractClassAssociationSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cls** | **str** |  | [optional] 
**is_mandatory** | **bool** |  | [optional] 
**is_mandatory_enforced** | **bool** |  | [optional] 
**is_many** | **bool** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from alfresco_model_client.models.abstract_class_association_source import AbstractClassAssociationSource

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractClassAssociationSource from a JSON string
abstract_class_association_source_instance = AbstractClassAssociationSource.from_json(json)
# print the JSON string representation of the object
print(AbstractClassAssociationSource.to_json())

# convert the object into a dict
abstract_class_association_source_dict = abstract_class_association_source_instance.to_dict()
# create an instance of AbstractClassAssociationSource from a dict
abstract_class_association_source_from_dict = AbstractClassAssociationSource.from_dict(abstract_class_association_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


