# GpsPvTelemetryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dates** | **List[str]** | List of UTC dates | 
**frame** | **str** | Frame of definition of the position velocity vectors | [optional] 
**id** | **str** |  | [optional] 
**measurements** | **List[List[float]]** | List containing position and velocity vectors [x y z vx vy vz], Units: [m] [ms^-1] | 
**position_standard_deviation** | **float** | Units: [m] | 
**velocity_standard_deviation** | **float** | Units: [ms^-1] | 

## Example

```python
from spacetower_python_client.models.gps_pv_telemetry_dto import GpsPvTelemetryDto

# TODO update the JSON string below
json = "{}"
# create an instance of GpsPvTelemetryDto from a JSON string
gps_pv_telemetry_dto_instance = GpsPvTelemetryDto.from_json(json)
# print the JSON string representation of the object
print(GpsPvTelemetryDto.to_json())

# convert the object into a dict
gps_pv_telemetry_dto_dict = gps_pv_telemetry_dto_instance.to_dict()
# create an instance of GpsPvTelemetryDto from a dict
gps_pv_telemetry_dto_from_dict = GpsPvTelemetryDto.from_dict(gps_pv_telemetry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


