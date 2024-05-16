# RadarMeasurementsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azimuth_standard_deviation** | **float** | Units: [deg] | 
**elevation_standard_deviation** | **float** | Units: [deg] | 
**generation_step** | **int** | Units: [s] | 
**ground_station_id** | **str** | The UUID of the tracking station | 
**id** | **str** |  | [optional] 
**range_rate_standard_deviation** | **float** | Units: [m/s] | 
**range_standard_deviation** | **float** | Units: [m] | 
**two_way_measurement** | **bool** | True for a two way signal | 

## Example

```python
from spacetower_python_client.models.radar_measurements_request_dto import RadarMeasurementsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RadarMeasurementsRequestDto from a JSON string
radar_measurements_request_dto_instance = RadarMeasurementsRequestDto.from_json(json)
# print the JSON string representation of the object
print(RadarMeasurementsRequestDto.to_json())

# convert the object into a dict
radar_measurements_request_dto_dict = radar_measurements_request_dto_instance.to_dict()
# create an instance of RadarMeasurementsRequestDto from a dict
radar_measurements_request_dto_from_dict = RadarMeasurementsRequestDto.from_dict(radar_measurements_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


