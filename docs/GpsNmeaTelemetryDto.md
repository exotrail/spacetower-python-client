# GpsNmeaTelemetryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**altitude_standard_deviation** | **float** | Units: [m] | 
**dates** | **List[str]** | List of UTC dates | 
**ground_speed_standard_deviation** | **float** | Units: [m/s] | 
**id** | **str** |  | [optional] 
**latitude_standard_deviation** | **float** | Units: [deg] | 
**longitude_standard_deviation** | **float** | Units: [deg] | 
**measurements** | **List[List[float]]** | Array of double: latitude, longitude, norm of velocity in ECF frame, altitude, geoid separation. Units: [deg], [deg], [m/s], [m], [m] | 

## Example

```python
from spacetower_python_client.models.gps_nmea_telemetry_dto import GpsNmeaTelemetryDto

# TODO update the JSON string below
json = "{}"
# create an instance of GpsNmeaTelemetryDto from a JSON string
gps_nmea_telemetry_dto_instance = GpsNmeaTelemetryDto.from_json(json)
# print the JSON string representation of the object
print(GpsNmeaTelemetryDto.to_json())

# convert the object into a dict
gps_nmea_telemetry_dto_dict = gps_nmea_telemetry_dto_instance.to_dict()
# create an instance of GpsNmeaTelemetryDto from a dict
gps_nmea_telemetry_dto_from_dict = GpsNmeaTelemetryDto.from_dict(gps_nmea_telemetry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


