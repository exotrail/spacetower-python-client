# OemRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | **str** |  | 
**ephemerides_step** | **float** | Units: [s] | 
**frame** | **str** | The frame must be inertial | 
**id** | **str** |  | [optional] 
**object_id** | **str** |  | 
**object_name** | **str** |  | 
**write_acceleration** | **bool** | Include the accelerations in the output file | [optional] 
**write_covariance** | **bool** | Include the covariance matrices in the output file | [optional] 

## Example

```python
from spacetower_python_client.models.oem_request_dto import OemRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of OemRequestDto from a JSON string
oem_request_dto_instance = OemRequestDto.from_json(json)
# print the JSON string representation of the object
print(OemRequestDto.to_json())

# convert the object into a dict
oem_request_dto_dict = oem_request_dto_instance.to_dict()
# create an instance of OemRequestDto from a dict
oem_request_dto_from_dict = OemRequestDto.from_dict(oem_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


