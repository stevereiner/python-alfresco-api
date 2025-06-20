# RequestLocalization

Localization settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locales** | **List[str]** | A list of Locales definied by IETF BCP 47.  The ordering is significant.  The first locale (leftmost) is used for sort and query localization, whereas the remaining locales are used for query only. | [optional] 
**timezone** | **str** | A valid timezone id supported by @see java.time.ZoneId | [optional] 

## Example

```python
from alfresco_search_client.models.request_localization import RequestLocalization

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLocalization from a JSON string
request_localization_instance = RequestLocalization.from_json(json)
# print the JSON string representation of the object
print(RequestLocalization.to_json())

# convert the object into a dict
request_localization_dict = request_localization_instance.to_dict()
# create an instance of RequestLocalization from a dict
request_localization_from_dict = RequestLocalization.from_dict(request_localization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


