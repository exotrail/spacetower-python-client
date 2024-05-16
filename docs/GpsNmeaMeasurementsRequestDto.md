# GpsNmeaMeasurementsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**altitude_standard_deviation** | **float** | Expected altitude standard deviation. Units: [m] | 
**generation_step** | **int** | Units: [s] | 
**ground_speed_standard_deviation** | **float** | Expected ground speed standard deviation. Units: [m/s] | 
**id** | **str** |  | [optional] 
**latitude_standard_deviation** | **float** | Expected latitude standard deviation. Units: [deg] | 
**longitude_standard_deviation** | **float** | Expected longitude standard deviation. Units: [deg] | 

## Example

```python
from fds_api_gen_client.models.gps_nmea_measurements_request_dto import GpsNmeaMeasurementsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GpsNmeaMeasurementsRequestDto from a JSON string
gps_nmea_measurements_request_dto_instance = GpsNmeaMeasurementsRequestDto.from_json(json)
# print the JSON string representation of the object
print(GpsNmeaMeasurementsRequestDto.to_json())

# convert the object into a dict
gps_nmea_measurements_request_dto_dict = gps_nmea_measurements_request_dto_instance.to_dict()
# create an instance of GpsNmeaMeasurementsRequestDto from a dict
gps_nmea_measurements_request_dto_from_dict = GpsNmeaMeasurementsRequestDto.from_dict(gps_nmea_measurements_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


