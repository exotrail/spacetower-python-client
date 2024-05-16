# OrbitDeterminationReportDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_rejected_measurements** | **int** |  | [optional] 
**number_of_used_measurements** | **int** |  | [optional] 
**residuals_statistics** | [**List[OrbitDeterminationResidualStatisticsDto]**](OrbitDeterminationResidualStatisticsDto.md) |  | [optional] 

## Example

```python
from spacetower_python_client.models.orbit_determination_report_dto import OrbitDeterminationReportDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitDeterminationReportDto from a JSON string
orbit_determination_report_dto_instance = OrbitDeterminationReportDto.from_json(json)
# print the JSON string representation of the object
print(OrbitDeterminationReportDto.to_json())

# convert the object into a dict
orbit_determination_report_dto_dict = orbit_determination_report_dto_instance.to_dict()
# create an instance of OrbitDeterminationReportDto from a dict
orbit_determination_report_dto_from_dict = OrbitDeterminationReportDto.from_dict(orbit_determination_report_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


