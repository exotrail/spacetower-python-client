# ReflectivityCoefficientEstimationRequestInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**parameter_standard_deviation** | **float** | x in (0,1], Units: [-] | 
**process_noise_standard_deviation** | **float** | x in (0,0.1], Units: [-] | 

## Example

```python
from fds_api_gen_client.models.reflectivity_coefficient_estimation_request_input_dto import ReflectivityCoefficientEstimationRequestInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReflectivityCoefficientEstimationRequestInputDto from a JSON string
reflectivity_coefficient_estimation_request_input_dto_instance = ReflectivityCoefficientEstimationRequestInputDto.from_json(json)
# print the JSON string representation of the object
print(ReflectivityCoefficientEstimationRequestInputDto.to_json())

# convert the object into a dict
reflectivity_coefficient_estimation_request_input_dto_dict = reflectivity_coefficient_estimation_request_input_dto_instance.to_dict()
# create an instance of ReflectivityCoefficientEstimationRequestInputDto from a dict
reflectivity_coefficient_estimation_request_input_dto_from_dict = ReflectivityCoefficientEstimationRequestInputDto.from_dict(reflectivity_coefficient_estimation_request_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


