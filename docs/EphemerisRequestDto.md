# EphemerisRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ephemeris_types** | **List[str]** | List of requested ephemeris types | 
**id** | **str** |  | [optional] 
**step** | **float** | Units: [s] | 

## Example

```python
from fds_api_gen_client.models.ephemeris_request_dto import EphemerisRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EphemerisRequestDto from a JSON string
ephemeris_request_dto_instance = EphemerisRequestDto.from_json(json)
# print the JSON string representation of the object
print(EphemerisRequestDto.to_json())

# convert the object into a dict
ephemeris_request_dto_dict = ephemeris_request_dto_instance.to_dict()
# create an instance of EphemerisRequestDto from a dict
ephemeris_request_dto_from_dict = EphemerisRequestDto.from_dict(ephemeris_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


