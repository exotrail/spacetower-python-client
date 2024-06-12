# spacetower_python_client.OrbitExtrapolationApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_orbit_extrapolation**](OrbitExtrapolationApi.md#get_orbit_extrapolation) | **GET** /extrapolation/{id} | 
[**get_orbit_extrapolation_result**](OrbitExtrapolationApi.md#get_orbit_extrapolation_result) | **GET** /extrapolation/result/{id} | 
[**get_orbit_extrapolation_result_by_extrapolation_id**](OrbitExtrapolationApi.md#get_orbit_extrapolation_result_by_extrapolation_id) | **GET** /extrapolation/{id}/results | 
[**retrieve_all_orbit_extrapolations**](OrbitExtrapolationApi.md#retrieve_all_orbit_extrapolations) | **GET** /extrapolations | 
[**run_orbit_extrapolation**](OrbitExtrapolationApi.md#run_orbit_extrapolation) | **POST** /extrapolation | 


# **get_orbit_extrapolation**
> OrbitExtrapolationOutputDto get_orbit_extrapolation(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.orbit_extrapolation_output_dto import OrbitExtrapolationOutputDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.OrbitExtrapolationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_orbit_extrapolation(id)
        print("The response of OrbitExtrapolationApi->get_orbit_extrapolation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitExtrapolationApi->get_orbit_extrapolation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrbitExtrapolationOutputDto**](OrbitExtrapolationOutputDto.md)

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

# **get_orbit_extrapolation_result**
> OrbitExtrapolationResultDto get_orbit_extrapolation_result(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.orbit_extrapolation_result_dto import OrbitExtrapolationResultDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.OrbitExtrapolationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_orbit_extrapolation_result(id)
        print("The response of OrbitExtrapolationApi->get_orbit_extrapolation_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitExtrapolationApi->get_orbit_extrapolation_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrbitExtrapolationResultDto**](OrbitExtrapolationResultDto.md)

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

# **get_orbit_extrapolation_result_by_extrapolation_id**
> List[OrbitExtrapolationResultDto] get_orbit_extrapolation_result_by_extrapolation_id(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.orbit_extrapolation_result_dto import OrbitExtrapolationResultDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.OrbitExtrapolationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_orbit_extrapolation_result_by_extrapolation_id(id)
        print("The response of OrbitExtrapolationApi->get_orbit_extrapolation_result_by_extrapolation_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitExtrapolationApi->get_orbit_extrapolation_result_by_extrapolation_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[OrbitExtrapolationResultDto]**](OrbitExtrapolationResultDto.md)

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

# **retrieve_all_orbit_extrapolations**
> List[OrbitExtrapolationOutputDto] retrieve_all_orbit_extrapolations()



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.orbit_extrapolation_output_dto import OrbitExtrapolationOutputDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.OrbitExtrapolationApi(api_client)

    try:
        api_response = api_instance.retrieve_all_orbit_extrapolations()
        print("The response of OrbitExtrapolationApi->retrieve_all_orbit_extrapolations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitExtrapolationApi->retrieve_all_orbit_extrapolations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrbitExtrapolationOutputDto]**](OrbitExtrapolationOutputDto.md)

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

# **run_orbit_extrapolation**
> OrbitExtrapolationResultDto run_orbit_extrapolation(orbit_extrapolation_input_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.orbit_extrapolation_input_dto import OrbitExtrapolationInputDto
from spacetower_python_client.models.orbit_extrapolation_result_dto import OrbitExtrapolationResultDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.OrbitExtrapolationApi(api_client)
    orbit_extrapolation_input_dto = spacetower_python_client.OrbitExtrapolationInputDto() # OrbitExtrapolationInputDto | 

    try:
        api_response = api_instance.run_orbit_extrapolation(orbit_extrapolation_input_dto)
        print("The response of OrbitExtrapolationApi->run_orbit_extrapolation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitExtrapolationApi->run_orbit_extrapolation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orbit_extrapolation_input_dto** | [**OrbitExtrapolationInputDto**](OrbitExtrapolationInputDto.md)|  | 

### Return type

[**OrbitExtrapolationResultDto**](OrbitExtrapolationResultDto.md)

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

