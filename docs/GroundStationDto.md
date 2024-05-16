# GroundStationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**altitude** | **float** | Units: [km] | 
**elevation_mask** | **List[List[float]]** | Units: Double[deg][deg] | [optional] 
**id** | **str** |  | [optional] 
**latitude** | **float** | Units: [deg] | 
**longitude** | **float** | Units: [deg] | 
**min_elevation** | **float** | Units: [deg] | [optional] 
**name** | **str** |  | 

## Example

```python
from spacetower_python_client.models.ground_station_dto import GroundStationDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroundStationDto from a JSON string
ground_station_dto_instance = GroundStationDto.from_json(json)
# print the JSON string representation of the object
print(GroundStationDto.to_json())

# convert the object into a dict
ground_station_dto_dict = ground_station_dto_instance.to_dict()
# create an instance of GroundStationDto from a dict
ground_station_dto_from_dict = GroundStationDto.from_dict(ground_station_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


