# AbstractClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**List[AbstractClassAssociation]**](AbstractClassAssociation.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**included_in_supertype_query** | **bool** |  | [optional] 
**is_archive** | **bool** |  | [optional] 
**is_container** | **bool** |  | [optional] 
**mandatory_aspects** | **List[str]** |  | [optional] 
**model** | [**Model**](Model.md) |  | [optional] 
**parent_id** | **str** |  | [optional] 
**properties** | [**List[ModelProperty]**](ModelProperty.md) |  | [optional] 
**title** | **str** |  | 

## Example

```python
from alfresco_model_client.models.abstract_class import AbstractClass

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractClass from a JSON string
abstract_class_instance = AbstractClass.from_json(json)
# print the JSON string representation of the object
print(AbstractClass.to_json())

# convert the object into a dict
abstract_class_dict = abstract_class_instance.to_dict()
# create an instance of AbstractClass from a dict
abstract_class_from_dict = AbstractClass.from_dict(abstract_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


