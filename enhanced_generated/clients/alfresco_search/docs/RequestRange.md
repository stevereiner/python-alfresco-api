# RequestRange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **str** | The end of the range | [optional] 
**exclude_filters** | **list[str]** | Filter queries to exclude when calculating statistics | [optional] 
**field** | **str** | The name of the field to perform range | [optional] 
**gap** | **str** | Bucket size | [optional] 
**hardend** | **bool** | If true means that the last bucket will end at “end” even if it is less than “gap” wide. | [optional] 
**include** | **list[str]** | lower, upper, edge, outer, all | [optional] 
**label** | **str** | A label to include as a pivot reference | [optional] 
**other** | **list[str]** | before, after, between, non, all | [optional] 
**start** | **str** | The start of the range | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

