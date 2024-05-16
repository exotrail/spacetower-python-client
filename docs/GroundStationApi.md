# spacetower_python_client.GroundStationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ground_station**](GroundStationApi.md#create_ground_station) | **POST** /station | 
[**delete_ground_station**](GroundStationApi.md#delete_ground_station) | **DELETE** /station/{id} | 
[**retrieve_all_stations**](GroundStationApi.md#retrieve_all_stations) | **GET** /stations | 
[**retrieve_ground_station**](GroundStationApi.md#retrieve_ground_station) | **GET** /station/{id} | 


# **create_ground_station**
> GroundStationDto create_ground_station(ground_station_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.ground_station_dto import GroundStationDto
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
    api_instance = spacetower_python_client.GroundStationApi(api_client)
    ground_station_dto = spacetower_python_client.GroundStationDto() # GroundStationDto | 

    try:
        api_response = api_instance.create_ground_station(ground_station_dto)
        print("The response of GroundStationApi->create_ground_station:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroundStationApi->create_ground_station: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ground_station_dto** | [**GroundStationDto**](GroundStationDto.md)|  | 

### Return type

[**GroundStationDto**](GroundStationDto.md)

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

# **delete_ground_station**
> delete_ground_station(id)



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
    api_instance = spacetower_python_client.GroundStationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_ground_station(id)
    except Exception as e:
        print("Exception when calling GroundStationApi->delete_ground_station: %s\n" % e)
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

# **retrieve_all_stations**
> List[GroundStationDto] retrieve_all_stations()



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.ground_station_dto import GroundStationDto
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
    api_instance = spacetower_python_client.GroundStationApi(api_client)

    try:
        api_response = api_instance.retrieve_all_stations()
        print("The response of GroundStationApi->retrieve_all_stations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroundStationApi->retrieve_all_stations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GroundStationDto]**](GroundStationDto.md)

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

# **retrieve_ground_station**
> GroundStationDto retrieve_ground_station(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.ground_station_dto import GroundStationDto
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
    api_instance = spacetower_python_client.GroundStationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_ground_station(id)
        print("The response of GroundStationApi->retrieve_ground_station:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroundStationApi->retrieve_ground_station: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GroundStationDto**](GroundStationDto.md)

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

