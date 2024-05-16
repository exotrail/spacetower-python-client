# SensorEventRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ephemerides_step** | **float** |  | 
**events_type** | **List[str]** |  | 
**id** | **str** |  | [optional] 
**sensor_axis_in_spacecraft_frame** | **List[float]** |  | 
**sensor_field_of_view_half_angle** | **float** | The half angle defining the conical field of view. Units [deg] | 
**start_date** | **str** | UTC date | [optional] 

## Example

```python
from fds_api_gen_client.models.sensor_event_request_dto import SensorEventRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SensorEventRequestDto from a JSON string
sensor_event_request_dto_instance = SensorEventRequestDto.from_json(json)
# print the JSON string representation of the object
print(SensorEventRequestDto.to_json())

# convert the object into a dict
sensor_event_request_dto_dict = sensor_event_request_dto_instance.to_dict()
# create an instance of SensorEventRequestDto from a dict
sensor_event_request_dto_from_dict = SensorEventRequestDto.from_dict(sensor_event_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


