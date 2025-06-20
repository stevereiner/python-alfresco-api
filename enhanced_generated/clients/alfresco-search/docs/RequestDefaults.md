# RequestDefaults

Common query defaults

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_fts_field_operator** | **str** | The default way to combine query parts in field query groups when AND or OR is not explicitly stated - includes ! - + FIELD:(one two three)  | [optional] [default to 'AND']
**default_fts_operator** | **str** | The default way to combine query parts when AND or OR is not explicitly stated - includes ! - + one two three (one two three)  | [optional] [default to 'AND']
**default_field_name** | **str** |  | [optional] [default to 'TEXT']
**namespace** | **str** | The default name space to use if one is not provided | [optional] [default to 'cm']
**text_attributes** | **List[str]** | A list of query fields/properties used to expand TEXT: queries. The default is cm:content. You could include all content properties using d:content or list all individual content properties or types. As more terms are included the query size, complexity, memory impact and query time will increase.  | [optional] 

## Example

```python
from alfresco_search_client.models.request_defaults import RequestDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDefaults from a JSON string
request_defaults_instance = RequestDefaults.from_json(json)
# print the JSON string representation of the object
print(RequestDefaults.to_json())

# convert the object into a dict
request_defaults_dict = request_defaults_instance.to_dict()
# create an instance of RequestDefaults from a dict
request_defaults_from_dict = RequestDefaults.from_dict(request_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


