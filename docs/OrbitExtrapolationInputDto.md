# OrbitExtrapolationInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ephemeris_request_id** | **str** |  | [optional] 
**events_request_ids** | **List[str]** |  | [optional] 
**extrapolate_covariance** | **bool** | Should the covariance be propagated. Default is false | [optional] 
**extrapolation_duration** | **float** | Units: [s] | 
**initial_orbital_state_id** | **str** |  | 
**measurements_request_id** | **str** |  | [optional] 
**orbit_data_message_request_id** | **str** |  | [optional] 
**required_output_orbital_states** | **str** | Which orbital states should be included in the output | [optional] 
**roadmap_id** | **str** |  | [optional] 

## Example

```python
from spacetower_python_client.models.orbit_extrapolation_input_dto import OrbitExtrapolationInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitExtrapolationInputDto from a JSON string
orbit_extrapolation_input_dto_instance = OrbitExtrapolationInputDto.from_json(json)
# print the JSON string representation of the object
print(OrbitExtrapolationInputDto.to_json())

# convert the object into a dict
orbit_extrapolation_input_dto_dict = orbit_extrapolation_input_dto_instance.to_dict()
# create an instance of OrbitExtrapolationInputDto from a dict
orbit_extrapolation_input_dto_from_dict = OrbitExtrapolationInputDto.from_dict(orbit_extrapolation_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


