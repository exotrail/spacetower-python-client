# AttitudeActionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attitude_mode** | **str** | Attitude list, can contains quaternions | 
**id** | **str** |  | [optional] 
**quaternions** | [**List[QuaternionActionDto]**](QuaternionActionDto.md) | List of quaternions related to the current attitude. Required if attitudeMode is QUATERNION | [optional] 
**transition_date** | **str** | UTC date | 

## Example

```python
from fds_api_gen_client.models.attitude_action_dto import AttitudeActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of AttitudeActionDto from a JSON string
attitude_action_dto_instance = AttitudeActionDto.from_json(json)
# print the JSON string representation of the object
print(AttitudeActionDto.to_json())

# convert the object into a dict
attitude_action_dto_dict = attitude_action_dto_instance.to_dict()
# create an instance of AttitudeActionDto from a dict
attitude_action_dto_from_dict = AttitudeActionDto.from_dict(attitude_action_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


