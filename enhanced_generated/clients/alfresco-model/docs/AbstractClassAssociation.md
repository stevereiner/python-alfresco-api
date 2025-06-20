# AbstractClassAssociation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**is_child** | **bool** |  | [optional] 
**is_protected** | **bool** |  | [optional] 
**source** | [**AbstractClassAssociationSource**](AbstractClassAssociationSource.md) |  | [optional] 
**target** | [**AbstractClassAssociationSource**](AbstractClassAssociationSource.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from alfresco_model_client.models.abstract_class_association import AbstractClassAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractClassAssociation from a JSON string
abstract_class_association_instance = AbstractClassAssociation.from_json(json)
# print the JSON string representation of the object
print(AbstractClassAssociation.to_json())

# convert the object into a dict
abstract_class_association_dict = abstract_class_association_instance.to_dict()
# create an instance of AbstractClassAssociation from a dict
abstract_class_association_from_dict = AbstractClassAssociation.from_dict(abstract_class_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


