# SolrResultSet

SQL results in Solr formatting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_set** | [**List[DocsInner]**](DocsInner.md) | Array of documents returned by the query, note that this is a Solr convention. | [optional] 

## Example

```python
from alfresco_search_sql_client.models.solr_result_set import SolrResultSet

# TODO update the JSON string below
json = "{}"
# create an instance of SolrResultSet from a JSON string
solr_result_set_instance = SolrResultSet.from_json(json)
# print the JSON string representation of the object
print(SolrResultSet.to_json())

# convert the object into a dict
solr_result_set_dict = solr_result_set_instance.to_dict()
# create an instance of SolrResultSet from a dict
solr_result_set_from_dict = SolrResultSet.from_dict(solr_result_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


