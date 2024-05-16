# spacetower_python_client.SolarArrayApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_solar_array**](SolarArrayApi.md#create_solar_array) | **POST** /solar-array | 
[**delete_solar_array**](SolarArrayApi.md#delete_solar_array) | **DELETE** /solar-array/{id} | 
[**retrieve_all_solar_arrays**](SolarArrayApi.md#retrieve_all_solar_arrays) | **GET** /solar-arrays | 
[**retrieve_solar_array**](SolarArrayApi.md#retrieve_solar_array) | **GET** /solar-array/{id} | 


# **create_solar_array**
> SolarArrayDto create_solar_array(solar_array_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.solar_array_dto import SolarArrayDto
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
    api_instance = spacetower_python_client.SolarArrayApi(api_client)
    solar_array_dto = spacetower_python_client.SolarArrayDto() # SolarArrayDto | 

    try:
        api_response = api_instance.create_solar_array(solar_array_dto)
        print("The response of SolarArrayApi->create_solar_array:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolarArrayApi->create_solar_array: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solar_array_dto** | [**SolarArrayDto**](SolarArrayDto.md)|  | 

### Return type

[**SolarArrayDto**](SolarArrayDto.md)

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

# **delete_solar_array**
> delete_solar_array(id)



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
    api_instance = spacetower_python_client.SolarArrayApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_solar_array(id)
    except Exception as e:
        print("Exception when calling SolarArrayApi->delete_solar_array: %s\n" % e)
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

# **retrieve_all_solar_arrays**
> List[SolarArrayDto] retrieve_all_solar_arrays()



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.solar_array_dto import SolarArrayDto
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
    api_instance = spacetower_python_client.SolarArrayApi(api_client)

    try:
        api_response = api_instance.retrieve_all_solar_arrays()
        print("The response of SolarArrayApi->retrieve_all_solar_arrays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolarArrayApi->retrieve_all_solar_arrays: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SolarArrayDto]**](SolarArrayDto.md)

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

# **retrieve_solar_array**
> SolarArrayDto retrieve_solar_array(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.solar_array_dto import SolarArrayDto
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
    api_instance = spacetower_python_client.SolarArrayApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_solar_array(id)
        print("The response of SolarArrayApi->retrieve_solar_array:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SolarArrayApi->retrieve_solar_array: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SolarArrayDto**](SolarArrayDto.md)

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

