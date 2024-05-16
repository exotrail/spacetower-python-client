# EphemerisDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ephemeris_type** | **str** |  | 
**id** | **str** |  | [optional] 
**lines** | **List[object]** |  | 

## Example

```python
from fds_api_gen_client.models.ephemeris_dto import EphemerisDto

# TODO update the JSON string below
json = "{}"
# create an instance of EphemerisDto from a JSON string
ephemeris_dto_instance = EphemerisDto.from_json(json)
# print the JSON string representation of the object
print(EphemerisDto.to_json())

# convert the object into a dict
ephemeris_dto_dict = ephemeris_dto_instance.to_dict()
# create an instance of EphemerisDto from a dict
ephemeris_dto_from_dict = EphemerisDto.from_dict(ephemeris_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


