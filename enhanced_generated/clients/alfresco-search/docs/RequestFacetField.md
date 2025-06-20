# RequestFacetField

A simple facet field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_filters** | **List[str]** | Filter Queries with tags listed here will not be included in facet counts. This is used for multi-select facetting.  | [optional] 
**facet_enum_cache_min_df** | **int** |  | [optional] 
**var_field** | **str** | The facet field | [optional] 
**label** | **str** | A label to include in place of the facet field | [optional] 
**limit** | **int** |  | [optional] 
**method** | **str** |  | [optional] 
**mincount** | **int** | The minimum count required for a facet field to be included in the response. | [optional] [default to 1]
**missing** | **bool** | When true, count results that match the query but which have no facet value for the field (in addition to the Term-based constraints). | [optional] [default to False]
**offset** | **int** |  | [optional] 
**prefix** | **str** | Restricts the possible constraints to only indexed values with a specified prefix. | [optional] 
**sort** | **str** |  | [optional] 

## Example

```python
from alfresco_search_client.models.request_facet_field import RequestFacetField

# TODO update the JSON string below
json = "{}"
# create an instance of RequestFacetField from a JSON string
request_facet_field_instance = RequestFacetField.from_json(json)
# print the JSON string representation of the object
print(RequestFacetField.to_json())

# convert the object into a dict
request_facet_field_dict = request_facet_field_instance.to_dict()
# create an instance of RequestFacetField from a dict
request_facet_field_from_dict = RequestFacetField.from_dict(request_facet_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


