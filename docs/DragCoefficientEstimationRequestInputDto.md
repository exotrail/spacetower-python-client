# DragCoefficientEstimationRequestInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**parameter_standard_deviation** | **float** | x in (0,1], Units: [-] | 
**process_noise_standard_deviation** | **float** | x in (0,0.1], Units: [-] | 

## Example

```python
from spacetower_python_client.models.drag_coefficient_estimation_request_input_dto import DragCoefficientEstimationRequestInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of DragCoefficientEstimationRequestInputDto from a JSON string
drag_coefficient_estimation_request_input_dto_instance = DragCoefficientEstimationRequestInputDto.from_json(json)
# print the JSON string representation of the object
print(DragCoefficientEstimationRequestInputDto.to_json())

# convert the object into a dict
drag_coefficient_estimation_request_input_dto_dict = drag_coefficient_estimation_request_input_dto_instance.to_dict()
# create an instance of DragCoefficientEstimationRequestInputDto from a dict
drag_coefficient_estimation_request_input_dto_from_dict = DragCoefficientEstimationRequestInputDto.from_dict(drag_coefficient_estimation_request_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


