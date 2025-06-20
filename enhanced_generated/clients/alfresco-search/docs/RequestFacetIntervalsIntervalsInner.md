# RequestFacetIntervalsIntervalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field to facet on | [optional] 
**label** | **str** | A label to use to identify the field facet | [optional] 
**sets** | [**List[RequestFacetSet]**](RequestFacetSet.md) | Sets the intervals for all fields. | [optional] 

## Example

```python
from alfresco_search_client.models.request_facet_intervals_intervals_inner import RequestFacetIntervalsIntervalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestFacetIntervalsIntervalsInner from a JSON string
request_facet_intervals_intervals_inner_instance = RequestFacetIntervalsIntervalsInner.from_json(json)
# print the JSON string representation of the object
print(RequestFacetIntervalsIntervalsInner.to_json())

# convert the object into a dict
request_facet_intervals_intervals_inner_dict = request_facet_intervals_intervals_inner_instance.to_dict()
# create an instance of RequestFacetIntervalsIntervalsInner from a dict
request_facet_intervals_intervals_inner_from_dict = RequestFacetIntervalsIntervalsInner.from_dict(request_facet_intervals_intervals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


