# spacetower_python_client.RoadmapActionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attitude_action**](RoadmapActionApi.md#create_attitude_action) | **POST** /roadmap-action/attitude | 
[**create_firing_action**](RoadmapActionApi.md#create_firing_action) | **POST** /roadmap-action/firing | 
[**create_quaternion_action**](RoadmapActionApi.md#create_quaternion_action) | **POST** /roadmap-action/quaternion | 
[**delete_roadmap_action**](RoadmapActionApi.md#delete_roadmap_action) | **DELETE** /roadmap-action/{id} | 
[**retrieve_all_roadmap_actions**](RoadmapActionApi.md#retrieve_all_roadmap_actions) | **GET** /roadmap-actions | 
[**retrieve_roadmap_action**](RoadmapActionApi.md#retrieve_roadmap_action) | **GET** /roadmap-action/{id} | 


# **create_attitude_action**
> object create_attitude_action(attitude_action_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.attitude_action_dto import AttitudeActionDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.RoadmapActionApi(api_client)
    attitude_action_dto = spacetower_python_client.AttitudeActionDto() # AttitudeActionDto | 

    try:
        api_response = api_instance.create_attitude_action(attitude_action_dto)
        print("The response of RoadmapActionApi->create_attitude_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadmapActionApi->create_attitude_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attitude_action_dto** | [**AttitudeActionDto**](AttitudeActionDto.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_firing_action**
> object create_firing_action(firing_action_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.firing_action_dto import FiringActionDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.RoadmapActionApi(api_client)
    firing_action_dto = spacetower_python_client.FiringActionDto() # FiringActionDto | 

    try:
        api_response = api_instance.create_firing_action(firing_action_dto)
        print("The response of RoadmapActionApi->create_firing_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadmapActionApi->create_firing_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firing_action_dto** | [**FiringActionDto**](FiringActionDto.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quaternion_action**
> object create_quaternion_action(quaternion_action_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.quaternion_action_dto import QuaternionActionDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.RoadmapActionApi(api_client)
    quaternion_action_dto = spacetower_python_client.QuaternionActionDto() # QuaternionActionDto | 

    try:
        api_response = api_instance.create_quaternion_action(quaternion_action_dto)
        print("The response of RoadmapActionApi->create_quaternion_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadmapActionApi->create_quaternion_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quaternion_action_dto** | [**QuaternionActionDto**](QuaternionActionDto.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_roadmap_action**
> delete_roadmap_action(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.RoadmapActionApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_roadmap_action(id)
    except Exception as e:
        print("Exception when calling RoadmapActionApi->delete_roadmap_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_roadmap_actions**
> List[object] retrieve_all_roadmap_actions()



### Example


```python
import spacetower_python_client
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.RoadmapActionApi(api_client)

    try:
        api_response = api_instance.retrieve_all_roadmap_actions()
        print("The response of RoadmapActionApi->retrieve_all_roadmap_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadmapActionApi->retrieve_all_roadmap_actions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_roadmap_action**
> object retrieve_roadmap_action(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.RoadmapActionApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_roadmap_action(id)
        print("The response of RoadmapActionApi->retrieve_roadmap_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadmapActionApi->retrieve_roadmap_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

