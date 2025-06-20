# RequestFacetIntervals

Facet Intervals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervals** | [**List[RequestFacetIntervalsIntervalsInner]**](RequestFacetIntervalsIntervalsInner.md) | Specifies the fields to facet by interval. | [optional] 
**sets** | [**List[RequestFacetSet]**](RequestFacetSet.md) | Sets the intervals for all fields. | [optional] 

## Example

```python
from alfresco_search_client.models.request_facet_intervals import RequestFacetIntervals

# TODO update the JSON string below
json = "{}"
# create an instance of RequestFacetIntervals from a JSON string
request_facet_intervals_instance = RequestFacetIntervals.from_json(json)
# print the JSON string representation of the object
print(RequestFacetIntervals.to_json())

# convert the object into a dict
request_facet_intervals_dict = request_facet_intervals_instance.to_dict()
# create an instance of RequestFacetIntervals from a dict
request_facet_intervals_from_dict = RequestFacetIntervals.from_dict(request_facet_intervals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


