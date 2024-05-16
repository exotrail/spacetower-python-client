# OpticalTelemetryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azimuth_standard_deviation** | **float** | Units: [deg] | 
**dates** | **List[str]** | List of UTC dates | 
**elevation_standard_deviation** | **float** | Units: [deg] | 
**ground_station_id** | **str** |  | 
**id** | **str** |  | [optional] 
**measurements** | **List[List[float]]** | Array of double: azimuth, elevation. Units: [deg], [deg] | 

## Example

```python
from fds_api_gen_client.models.optical_telemetry_dto import OpticalTelemetryDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalTelemetryDto from a JSON string
optical_telemetry_dto_instance = OpticalTelemetryDto.from_json(json)
# print the JSON string representation of the object
print(OpticalTelemetryDto.to_json())

# convert the object into a dict
optical_telemetry_dto_dict = optical_telemetry_dto_instance.to_dict()
# create an instance of OpticalTelemetryDto from a dict
optical_telemetry_dto_from_dict = OpticalTelemetryDto.from_dict(optical_telemetry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


