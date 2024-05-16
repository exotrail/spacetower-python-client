# OrbitExtrapolationResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computed_events** | **List[object]** |  | [optional] 
**computed_measurements** | **List[object]** |  | [optional] 
**ephemerides** | [**List[EphemerisDto]**](EphemerisDto.md) |  | [optional] 
**id** | **str** |  | [optional] 
**log** | [**OrbitExtrapolationLogDto**](OrbitExtrapolationLogDto.md) |  | [optional] 
**orbit_data_message_output** | **str** |  | [optional] 
**orbital_states** | [**List[OrbitalStateDto]**](OrbitalStateDto.md) |  | [optional] 
**request** | [**OrbitExtrapolationOutputDto**](OrbitExtrapolationOutputDto.md) |  | [optional] 

## Example

```python
from fds_api_gen_client.models.orbit_extrapolation_result_dto import OrbitExtrapolationResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitExtrapolationResultDto from a JSON string
orbit_extrapolation_result_dto_instance = OrbitExtrapolationResultDto.from_json(json)
# print the JSON string representation of the object
print(OrbitExtrapolationResultDto.to_json())

# convert the object into a dict
orbit_extrapolation_result_dto_dict = orbit_extrapolation_result_dto_instance.to_dict()
# create an instance of OrbitExtrapolationResultDto from a dict
orbit_extrapolation_result_dto_from_dict = OrbitExtrapolationResultDto.from_dict(orbit_extrapolation_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


