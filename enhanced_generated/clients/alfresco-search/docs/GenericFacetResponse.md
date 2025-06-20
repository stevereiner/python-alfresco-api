# GenericFacetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | [**List[GenericBucket]**](GenericBucket.md) | An array of buckets and values | [optional] 
**label** | **str** | The field name or its explicit label, if provided on the request | [optional] 
**type** | **str** | The facet type, eg. interval, range, pivot, stats | [optional] 

## Example

```python
from alfresco_search_client.models.generic_facet_response import GenericFacetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenericFacetResponse from a JSON string
generic_facet_response_instance = GenericFacetResponse.from_json(json)
# print the JSON string representation of the object
print(GenericFacetResponse.to_json())

# convert the object into a dict
generic_facet_response_dict = generic_facet_response_instance.to_dict()
# create an instance of GenericFacetResponse from a dict
generic_facet_response_from_dict = GenericFacetResponse.from_dict(generic_facet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


