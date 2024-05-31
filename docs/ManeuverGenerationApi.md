# spacetower_python_client.ManeuverGenerationApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_maneuver_generation**](ManeuverGenerationApi.md#get_maneuver_generation) | **GET** /maneuver-generation/{id} | 
[**get_maneuver_generation_result**](ManeuverGenerationApi.md#get_maneuver_generation_result) | **GET** /maneuver-generation/result/{id} | 
[**get_maneuver_generation_result_by_request_id**](ManeuverGenerationApi.md#get_maneuver_generation_result_by_request_id) | **GET** /maneuver-generation/{id}/results | 
[**retrieve_all_maneuver_generations**](ManeuverGenerationApi.md#retrieve_all_maneuver_generations) | **GET** /maneuver-generations | 
[**run_maneuver_generation**](ManeuverGenerationApi.md#run_maneuver_generation) | **POST** /maneuver-generation | 


# **get_maneuver_generation**
> ManeuverGenerationOutputDto get_maneuver_generation(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.maneuver_generation_output_dto import ManeuverGenerationOutputDto
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
    api_instance = spacetower_python_client.ManeuverGenerationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_maneuver_generation(id)
        print("The response of ManeuverGenerationApi->get_maneuver_generation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManeuverGenerationApi->get_maneuver_generation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ManeuverGenerationOutputDto**](ManeuverGenerationOutputDto.md)

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

# **get_maneuver_generation_result**
> ManeuverGenerationResultDto get_maneuver_generation_result(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.maneuver_generation_result_dto import ManeuverGenerationResultDto
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
    api_instance = spacetower_python_client.ManeuverGenerationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_maneuver_generation_result(id)
        print("The response of ManeuverGenerationApi->get_maneuver_generation_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManeuverGenerationApi->get_maneuver_generation_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ManeuverGenerationResultDto**](ManeuverGenerationResultDto.md)

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

# **get_maneuver_generation_result_by_request_id**
> List[ManeuverGenerationResultDto] get_maneuver_generation_result_by_request_id(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.maneuver_generation_result_dto import ManeuverGenerationResultDto
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
    api_instance = spacetower_python_client.ManeuverGenerationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_maneuver_generation_result_by_request_id(id)
        print("The response of ManeuverGenerationApi->get_maneuver_generation_result_by_request_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManeuverGenerationApi->get_maneuver_generation_result_by_request_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[ManeuverGenerationResultDto]**](ManeuverGenerationResultDto.md)

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

# **retrieve_all_maneuver_generations**
> List[ManeuverGenerationOutputDto] retrieve_all_maneuver_generations()



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.maneuver_generation_output_dto import ManeuverGenerationOutputDto
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
    api_instance = spacetower_python_client.ManeuverGenerationApi(api_client)

    try:
        api_response = api_instance.retrieve_all_maneuver_generations()
        print("The response of ManeuverGenerationApi->retrieve_all_maneuver_generations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManeuverGenerationApi->retrieve_all_maneuver_generations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ManeuverGenerationOutputDto]**](ManeuverGenerationOutputDto.md)

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

# **run_maneuver_generation**
> ManeuverGenerationResultDto run_maneuver_generation(maneuver_generation_input_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.maneuver_generation_input_dto import ManeuverGenerationInputDto
from spacetower_python_client.models.maneuver_generation_result_dto import ManeuverGenerationResultDto
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
    api_instance = spacetower_python_client.ManeuverGenerationApi(api_client)
    maneuver_generation_input_dto = spacetower_python_client.ManeuverGenerationInputDto() # ManeuverGenerationInputDto | 

    try:
        api_response = api_instance.run_maneuver_generation(maneuver_generation_input_dto)
        print("The response of ManeuverGenerationApi->run_maneuver_generation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManeuverGenerationApi->run_maneuver_generation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maneuver_generation_input_dto** | [**ManeuverGenerationInputDto**](ManeuverGenerationInputDto.md)|  | 

### Return type

[**ManeuverGenerationResultDto**](ManeuverGenerationResultDto.md)

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

