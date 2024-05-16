# GpsPvMeasurementsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frame** | **str** |  | 
**generation_step** | **int** | Units: [s] | 
**id** | **str** |  | [optional] 
**position_standard_deviation** | **float** | Units: [m] | 
**velocity_standard_deviation** | **float** | Units: [m/s] | 

## Example

```python
from spacetower_python_client.models.gps_pv_measurements_request_dto import GpsPvMeasurementsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GpsPvMeasurementsRequestDto from a JSON string
gps_pv_measurements_request_dto_instance = GpsPvMeasurementsRequestDto.from_json(json)
# print the JSON string representation of the object
print(GpsPvMeasurementsRequestDto.to_json())

# convert the object into a dict
gps_pv_measurements_request_dto_dict = gps_pv_measurements_request_dto_instance.to_dict()
# create an instance of GpsPvMeasurementsRequestDto from a dict
gps_pv_measurements_request_dto_from_dict = GpsPvMeasurementsRequestDto.from_dict(gps_pv_measurements_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


