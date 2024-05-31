# spacetower_python_client.RoadmapApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_roadmap**](RoadmapApi.md#create_roadmap) | **POST** /roadmap/from-actions | 
[**delete_roadmap**](RoadmapApi.md#delete_roadmap) | **DELETE** /roadmap/{id} | 
[**retrieve_all_roadmaps**](RoadmapApi.md#retrieve_all_roadmaps) | **GET** /roadmaps | 
[**retrieve_roadmap**](RoadmapApi.md#retrieve_roadmap) | **GET** /roadmap/{id} | 


# **create_roadmap**
> object create_roadmap(roadmap_from_actions_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.roadmap_from_actions_dto import RoadmapFromActionsDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = spacetower_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.RoadmapApi(api_client)
    roadmap_from_actions_dto = spacetower_python_client.RoadmapFromActionsDto() # RoadmapFromActionsDto | 

    try:
        api_response = api_instance.create_roadmap(roadmap_from_actions_dto)
        print("The response of RoadmapApi->create_roadmap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadmapApi->create_roadmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roadmap_from_actions_dto** | [**RoadmapFromActionsDto**](RoadmapFromActionsDto.md)|  | 

### Return type

**object**

### Authorization

[bearer-key](../README.md#bearer-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_roadmap**
> delete_roadmap(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = spacetower_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.RoadmapApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_roadmap(id)
    except Exception as e:
        print("Exception when calling RoadmapApi->delete_roadmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer-key](../README.md#bearer-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_roadmaps**
> List[object] retrieve_all_roadmaps()



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = spacetower_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.RoadmapApi(api_client)

    try:
        api_response = api_instance.retrieve_all_roadmaps()
        print("The response of RoadmapApi->retrieve_all_roadmaps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadmapApi->retrieve_all_roadmaps: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[bearer-key](../README.md#bearer-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_roadmap**
> object retrieve_roadmap(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = spacetower_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.RoadmapApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_roadmap(id)
        print("The response of RoadmapApi->retrieve_roadmap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoadmapApi->retrieve_roadmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[bearer-key](../README.md#bearer-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

