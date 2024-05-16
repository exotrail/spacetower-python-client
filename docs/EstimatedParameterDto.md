# EstimatedParameterDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from spacetower_python_client.models.estimated_parameter_dto import EstimatedParameterDto

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedParameterDto from a JSON string
estimated_parameter_dto_instance = EstimatedParameterDto.from_json(json)
# print the JSON string representation of the object
print(EstimatedParameterDto.to_json())

# convert the object into a dict
estimated_parameter_dto_dict = estimated_parameter_dto_instance.to_dict()
# create an instance of EstimatedParameterDto from a dict
estimated_parameter_dto_from_dict = EstimatedParameterDto.from_dict(estimated_parameter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


