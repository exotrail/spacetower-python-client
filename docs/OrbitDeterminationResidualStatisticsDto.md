# OrbitDeterminationResidualStatisticsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mean** | **float** |  | [optional] 
**median** | **float** |  | [optional] 
**residuals** | [**List[ResidualDto]**](ResidualDto.md) |  | [optional] 
**standard_deviation** | **float** |  | [optional] 

## Example

```python
from spacetower_python_client.models.orbit_determination_residual_statistics_dto import OrbitDeterminationResidualStatisticsDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitDeterminationResidualStatisticsDto from a JSON string
orbit_determination_residual_statistics_dto_instance = OrbitDeterminationResidualStatisticsDto.from_json(json)
# print the JSON string representation of the object
print(OrbitDeterminationResidualStatisticsDto.to_json())

# convert the object into a dict
orbit_determination_residual_statistics_dto_dict = orbit_determination_residual_statistics_dto_instance.to_dict()
# create an instance of OrbitDeterminationResidualStatisticsDto from a dict
orbit_determination_residual_statistics_dto_from_dict = OrbitDeterminationResidualStatisticsDto.from_dict(orbit_determination_residual_statistics_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


