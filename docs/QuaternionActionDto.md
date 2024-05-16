# QuaternionActionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**q0** | **float** | Scalar component. Units: [-] | [default to 1.0]
**q1** | **float** | Vector part of the quaternion. First component. Units: [-] | 
**q2** | **float** | Vector part of the quaternion. Second component. Units: [-] | 
**q3** | **float** | Vector part of the quaternion. Third component. Units: [-] | 
**transition_date** | **str** | UTC date | 

## Example

```python
from spacetower_python_client.models.quaternion_action_dto import QuaternionActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuaternionActionDto from a JSON string
quaternion_action_dto_instance = QuaternionActionDto.from_json(json)
# print the JSON string representation of the object
print(QuaternionActionDto.to_json())

# convert the object into a dict
quaternion_action_dto_dict = quaternion_action_dto_instance.to_dict()
# create an instance of QuaternionActionDto from a dict
quaternion_action_dto_from_dict = QuaternionActionDto.from_dict(quaternion_action_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


