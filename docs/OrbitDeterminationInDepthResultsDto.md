# OrbitDeterminationInDepthResultsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**covariance_matrices** | **List[object]** |  | [optional] 
**estimated_drag_coefficients** | [**List[EstimatedParameterDto]**](EstimatedParameterDto.md) |  | [optional] 
**estimated_reflectivity_coefficients** | [**List[EstimatedParameterDto]**](EstimatedParameterDto.md) |  | [optional] 
**mean_orbits** | **List[object]** |  | [optional] 
**osculating_orbits** | **List[object]** |  | [optional] 

## Example

```python
from spacetower_python_client.models.orbit_determination_in_depth_results_dto import OrbitDeterminationInDepthResultsDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitDeterminationInDepthResultsDto from a JSON string
orbit_determination_in_depth_results_dto_instance = OrbitDeterminationInDepthResultsDto.from_json(json)
# print the JSON string representation of the object
print(OrbitDeterminationInDepthResultsDto.to_json())

# convert the object into a dict
orbit_determination_in_depth_results_dto_dict = orbit_determination_in_depth_results_dto_instance.to_dict()
# create an instance of OrbitDeterminationInDepthResultsDto from a dict
orbit_determination_in_depth_results_dto_from_dict = OrbitDeterminationInDepthResultsDto.from_dict(orbit_determination_in_depth_results_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


