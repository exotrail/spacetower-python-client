# RadarTelemetryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azimuth_standard_deviation** | **float** | Units: [deg] | 
**dates** | **List[str]** | List of UTC dates | 
**elevation_standard_deviation** | **float** | Units: [deg] | 
**ground_station_id** | **str** |  | 
**id** | **str** |  | [optional] 
**measurements** | **List[List[float]]** | Array of double: range, range rate, azimuth, elevation. Units: [m], [m/s], [deg], [deg] | 
**range_rate_standard_deviation** | **float** | Units: [m/s] | 
**range_standard_deviation** | **float** | Units: [m] | 
**two_way_measurement** | **bool** |  | 

## Example

```python
from fds_api_gen_client.models.radar_telemetry_dto import RadarTelemetryDto

# TODO update the JSON string below
json = "{}"
# create an instance of RadarTelemetryDto from a JSON string
radar_telemetry_dto_instance = RadarTelemetryDto.from_json(json)
# print the JSON string representation of the object
print(RadarTelemetryDto.to_json())

# convert the object into a dict
radar_telemetry_dto_dict = radar_telemetry_dto_instance.to_dict()
# create an instance of RadarTelemetryDto from a dict
radar_telemetry_dto_from_dict = RadarTelemetryDto.from_dict(radar_telemetry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


