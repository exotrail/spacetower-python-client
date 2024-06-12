# EstimatedThrustDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**magnitude** | **float** |  | [optional] 
**scale_factors** | **List[float]** |  | [optional] 
**tnw_direction** | **List[float]** |  | [optional] 

## Example

```python
from spacetower_python_client.models.estimated_thrust_dto import EstimatedThrustDto

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedThrustDto from a JSON string
estimated_thrust_dto_instance = EstimatedThrustDto.from_json(json)
# print the JSON string representation of the object
print(EstimatedThrustDto.to_json())

# convert the object into a dict
estimated_thrust_dto_dict = estimated_thrust_dto_instance.to_dict()
# create an instance of EstimatedThrustDto from a dict
estimated_thrust_dto_from_dict = EstimatedThrustDto.from_dict(estimated_thrust_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


