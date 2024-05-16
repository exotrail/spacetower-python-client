# StationVisibilityEventsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ground_station_ids** | **List[str]** | The station&#39;s UUID | 
**id** | **str** |  | [optional] 
**start_date** | **str** | UTC date | [optional] 

## Example

```python
from spacetower_python_client.models.station_visibility_events_request_dto import StationVisibilityEventsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of StationVisibilityEventsRequestDto from a JSON string
station_visibility_events_request_dto_instance = StationVisibilityEventsRequestDto.from_json(json)
# print the JSON string representation of the object
print(StationVisibilityEventsRequestDto.to_json())

# convert the object into a dict
station_visibility_events_request_dto_dict = station_visibility_events_request_dto_instance.to_dict()
# create an instance of StationVisibilityEventsRequestDto from a dict
station_visibility_events_request_dto_from_dict = StationVisibilityEventsRequestDto.from_dict(station_visibility_events_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


