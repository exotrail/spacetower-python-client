# OrbitDeterminationResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_keplerian_covariance** | **object** |  | [optional] 
**estimated_states** | [**List[OrbitalStateDto]**](OrbitalStateDto.md) |  | [optional] 
**firing_analysis_report** | [**FiringAnalysisReportDto**](FiringAnalysisReportDto.md) |  | [optional] 
**id** | **str** |  | [optional] 
**in_depth_results** | [**OrbitDeterminationInDepthResultsDto**](OrbitDeterminationInDepthResultsDto.md) |  | [optional] 
**log** | [**OrbitDeterminationLogDto**](OrbitDeterminationLogDto.md) |  | [optional] 
**report** | [**OrbitDeterminationReportDto**](OrbitDeterminationReportDto.md) |  | [optional] 
**request** | **object** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from spacetower_python_client.models.orbit_determination_result_dto import OrbitDeterminationResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitDeterminationResultDto from a JSON string
orbit_determination_result_dto_instance = OrbitDeterminationResultDto.from_json(json)
# print the JSON string representation of the object
print(OrbitDeterminationResultDto.to_json())

# convert the object into a dict
orbit_determination_result_dto_dict = orbit_determination_result_dto_instance.to_dict()
# create an instance of OrbitDeterminationResultDto from a dict
orbit_determination_result_dto_from_dict = OrbitDeterminationResultDto.from_dict(orbit_determination_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


