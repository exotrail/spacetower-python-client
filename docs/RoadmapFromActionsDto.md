# RoadmapFromActionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**final_date** | **str** | UTC date | 
**id** | **str** |  | [optional] 
**initial_date** | **str** | UTC date | 
**roadmap_action_ids** | **List[str]** | The UUIDs of the roadmap actions (firing, attitude or quaternion) to be executed | 

## Example

```python
from fds_api_gen_client.models.roadmap_from_actions_dto import RoadmapFromActionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoadmapFromActionsDto from a JSON string
roadmap_from_actions_dto_instance = RoadmapFromActionsDto.from_json(json)
# print the JSON string representation of the object
print(RoadmapFromActionsDto.to_json())

# convert the object into a dict
roadmap_from_actions_dto_dict = roadmap_from_actions_dto_instance.to_dict()
# create an instance of RoadmapFromActionsDto from a dict
roadmap_from_actions_dto_from_dict = RoadmapFromActionsDto.from_dict(roadmap_from_actions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


