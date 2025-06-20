# RequestDefaults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_fts_field_operator** | **str** | The default way to combine query parts in field query groups when AND or OR is not explicitly stated - includes ! - + FIELD:(one two three)  | [optional] [default to 'AND']
**default_fts_operator** | **str** | The default way to combine query parts when AND or OR is not explicitly stated - includes ! - + one two three (one two three)  | [optional] [default to 'AND']
**default_field_name** | **str** |  | [optional] [default to 'TEXT']
**namespace** | **str** | The default name space to use if one is not provided | [optional] [default to 'cm']
**text_attributes** | **list[str]** | A list of query fields/properties used to expand TEXT: queries. The default is cm:content. You could include all content properties using d:content or list all individual content properties or types. As more terms are included the query size, complexity, memory impact and query time will increase.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

