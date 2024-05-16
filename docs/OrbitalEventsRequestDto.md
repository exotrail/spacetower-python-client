# OrbitalEventsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events_type** | **List[str]** |  | 
**id** | **str** |  | [optional] 
**start_date** | **str** | UTC date | [optional] 

## Example

```python
from fds_api_gen_client.models.orbital_events_request_dto import OrbitalEventsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitalEventsRequestDto from a JSON string
orbital_events_request_dto_instance = OrbitalEventsRequestDto.from_json(json)
# print the JSON string representation of the object
print(OrbitalEventsRequestDto.to_json())

# convert the object into a dict
orbital_events_request_dto_dict = orbital_events_request_dto_instance.to_dict()
# create an instance of OrbitalEventsRequestDto from a dict
orbital_events_request_dto_from_dict = OrbitalEventsRequestDto.from_dict(orbital_events_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


