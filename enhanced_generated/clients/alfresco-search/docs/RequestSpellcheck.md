# RequestSpellcheck

Request that spellcheck fragments to be added to result set rows The properties reflect SOLR spellcheck parameters. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 

## Example

```python
from alfresco_search_client.models.request_spellcheck import RequestSpellcheck

# TODO update the JSON string below
json = "{}"
# create an instance of RequestSpellcheck from a JSON string
request_spellcheck_instance = RequestSpellcheck.from_json(json)
# print the JSON string representation of the object
print(RequestSpellcheck.to_json())

# convert the object into a dict
request_spellcheck_dict = request_spellcheck_instance.to_dict()
# create an instance of RequestSpellcheck from a dict
request_spellcheck_from_dict = RequestSpellcheck.from_dict(request_spellcheck_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


