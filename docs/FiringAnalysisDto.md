# FiringAnalysisDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument_of_perigee_delta** | **float** |  | [optional] 
**var_date** | **str** |  | [optional] 
**eccentricity_delta** | **float** |  | [optional] 
**estimated_acceleration** | **float** |  | [optional] 
**estimated_thrust** | **float** |  | [optional] 
**estimated_thrust_tnw_direction** | **List[float]** |  | [optional] 
**id** | **str** |  | [optional] 
**inclination_delta** | **float** |  | [optional] 
**raan_delta** | **float** |  | [optional] 
**semi_major_axis_delta** | **float** |  | [optional] 
**smoothed_keplerian_elements_after_firing** | [**SmoothedKeplerianElementsDto**](SmoothedKeplerianElementsDto.md) |  | [optional] 
**smoothed_keplerian_elements_before_firing** | [**SmoothedKeplerianElementsDto**](SmoothedKeplerianElementsDto.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fds_api_gen_client.models.firing_analysis_dto import FiringAnalysisDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiringAnalysisDto from a JSON string
firing_analysis_dto_instance = FiringAnalysisDto.from_json(json)
# print the JSON string representation of the object
print(FiringAnalysisDto.to_json())

# convert the object into a dict
firing_analysis_dto_dict = firing_analysis_dto_instance.to_dict()
# create an instance of FiringAnalysisDto from a dict
firing_analysis_dto_from_dict = FiringAnalysisDto.from_dict(firing_analysis_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


