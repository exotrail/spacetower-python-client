# GpsNmeaRawTelemetryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**altitude_standard_deviation** | **float** | Units: [m] | 
**ground_speed_standard_deviation** | **float** | Units: [m/s] | 
**id** | **str** |  | [optional] 
**latitude_standard_deviation** | **float** | Units: [deg] | 
**longitude_standard_deviation** | **float** | Units: [deg] | 
**nmea_sentences** | **List[str]** |  | [optional] 

## Example

```python
from spacetower_python_client.models.gps_nmea_raw_telemetry_dto import GpsNmeaRawTelemetryDto

# TODO update the JSON string below
json = "{}"
# create an instance of GpsNmeaRawTelemetryDto from a JSON string
gps_nmea_raw_telemetry_dto_instance = GpsNmeaRawTelemetryDto.from_json(json)
# print the JSON string representation of the object
print(GpsNmeaRawTelemetryDto.to_json())

# convert the object into a dict
gps_nmea_raw_telemetry_dto_dict = gps_nmea_raw_telemetry_dto_instance.to_dict()
# create an instance of GpsNmeaRawTelemetryDto from a dict
gps_nmea_raw_telemetry_dto_from_dict = GpsNmeaRawTelemetryDto.from_dict(gps_nmea_raw_telemetry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


