# RequestFacetFields

Simple facet fields to include The Properties reflect the global properties related to field facts in SOLR. They are descripbed in detail by the SOLR documentation 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facets** | [**List[RequestFacetField]**](RequestFacetField.md) | Define specifc fields on which to facet (adds SOLR facet.field and f.&lt;field&gt;.facet.* options)  | [optional] 

## Example

```python
from alfresco_search_client.models.request_facet_fields import RequestFacetFields

# TODO update the JSON string below
json = "{}"
# create an instance of RequestFacetFields from a JSON string
request_facet_fields_instance = RequestFacetFields.from_json(json)
# print the JSON string representation of the object
print(RequestFacetFields.to_json())

# convert the object into a dict
request_facet_fields_dict = request_facet_fields_instance.to_dict()
# create an instance of RequestFacetFields from a dict
request_facet_fields_from_dict = RequestFacetFields.from_dict(request_facet_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


