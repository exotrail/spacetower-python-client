# OpticalMeasurementsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azimuth_standard_deviation** | **float** | Units: [deg] | 
**elevation_standard_deviation** | **float** | Units: [deg] | 
**generation_step** | **int** | Units: [s] | 
**ground_station_id** | **str** | The UUID of the observation station | 
**id** | **str** |  | [optional] 

## Example

```python
from spacetower_python_client.models.optical_measurements_request_dto import OpticalMeasurementsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalMeasurementsRequestDto from a JSON string
optical_measurements_request_dto_instance = OpticalMeasurementsRequestDto.from_json(json)
# print the JSON string representation of the object
print(OpticalMeasurementsRequestDto.to_json())

# convert the object into a dict
optical_measurements_request_dto_dict = optical_measurements_request_dto_instance.to_dict()
# create an instance of OpticalMeasurementsRequestDto from a dict
optical_measurements_request_dto_from_dict = OpticalMeasurementsRequestDto.from_dict(optical_measurements_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


