# UkfOrbitDeterminationInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** |  | 
**estimated_results_min_step** | **float** | Minimum step for the estimated results. Unit: s. | [optional] 
**initial_orbital_state_id** | **str** |  | 
**parameter_estimation_request_ids** | **List[str]** |  | [optional] 
**roadmap_id** | **str** |  | [optional] 
**telemetry_id** | **str** |  | 

## Example

```python
from spacetower_python_client.models.ukf_orbit_determination_input_dto import UkfOrbitDeterminationInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of UkfOrbitDeterminationInputDto from a JSON string
ukf_orbit_determination_input_dto_instance = UkfOrbitDeterminationInputDto.from_json(json)
# print the JSON string representation of the object
print(UkfOrbitDeterminationInputDto.to_json())

# convert the object into a dict
ukf_orbit_determination_input_dto_dict = ukf_orbit_determination_input_dto_instance.to_dict()
# create an instance of UkfOrbitDeterminationInputDto from a dict
ukf_orbit_determination_input_dto_from_dict = UkfOrbitDeterminationInputDto.from_dict(ukf_orbit_determination_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


