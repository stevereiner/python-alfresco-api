# RequestFacetSet

The interval to Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **str** | The end of the range | [optional] 
**end_inclusive** | **bool** | When true, the set will include values less than or equal to \&quot;end\&quot; | [optional] [default to True]
**label** | **str** | A label to use to identify the set | [optional] 
**start** | **str** | The start of the range | [optional] 
**start_inclusive** | **bool** | When true, the set will include values greater or equal to \&quot;start\&quot; | [optional] [default to True]

## Example

```python
from alfresco_search_client.models.request_facet_set import RequestFacetSet

# TODO update the JSON string below
json = "{}"
# create an instance of RequestFacetSet from a JSON string
request_facet_set_instance = RequestFacetSet.from_json(json)
# print the JSON string representation of the object
print(RequestFacetSet.to_json())

# convert the object into a dict
request_facet_set_dict = request_facet_set_instance.to_dict()
# create an instance of RequestFacetSet from a dict
request_facet_set_from_dict = RequestFacetSet.from_dict(request_facet_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


