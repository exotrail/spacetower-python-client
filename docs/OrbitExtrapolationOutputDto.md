# OrbitExtrapolationOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ephemeris_request** | [**EphemerisRequestDto**](EphemerisRequestDto.md) |  | [optional] 
**events_requests** | **List[object]** |  | [optional] 
**extrapolate_covariance** | **bool** |  | [optional] 
**extrapolation_duration** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**initial_orbital_state** | [**OrbitalStateDto**](OrbitalStateDto.md) |  | [optional] 
**measurements_request** | **object** |  | [optional] 
**orbit_data_message_request** | **object** |  | [optional] 
**required_output_orbital_states** | **str** |  | [optional] 
**roadmap** | **object** |  | [optional] 

## Example

```python
from fds_api_gen_client.models.orbit_extrapolation_output_dto import OrbitExtrapolationOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitExtrapolationOutputDto from a JSON string
orbit_extrapolation_output_dto_instance = OrbitExtrapolationOutputDto.from_json(json)
# print the JSON string representation of the object
print(OrbitExtrapolationOutputDto.to_json())

# convert the object into a dict
orbit_extrapolation_output_dto_dict = orbit_extrapolation_output_dto_instance.to_dict()
# create an instance of OrbitExtrapolationOutputDto from a dict
orbit_extrapolation_output_dto_from_dict = OrbitExtrapolationOutputDto.from_dict(orbit_extrapolation_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


