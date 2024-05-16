# FiringAnalysisReportDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_analyses_dates** | **List[datetime]** |  | [optional] 
**number_of_failed_analyses** | **int** |  | [optional] 
**number_of_pending_analyses** | **int** |  | [optional] 
**number_of_processed_analyses** | **int** |  | [optional] 
**pending_analyses_dates** | **List[datetime]** |  | [optional] 
**processed_analyses** | [**List[FiringAnalysisDto]**](FiringAnalysisDto.md) |  | [optional] 

## Example

```python
from spacetower_python_client.models.firing_analysis_report_dto import FiringAnalysisReportDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiringAnalysisReportDto from a JSON string
firing_analysis_report_dto_instance = FiringAnalysisReportDto.from_json(json)
# print the JSON string representation of the object
print(FiringAnalysisReportDto.to_json())

# convert the object into a dict
firing_analysis_report_dto_dict = firing_analysis_report_dto_instance.to_dict()
# create an instance of FiringAnalysisReportDto from a dict
firing_analysis_report_dto_from_dict = FiringAnalysisReportDto.from_dict(firing_analysis_report_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


