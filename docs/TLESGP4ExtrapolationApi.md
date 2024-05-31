# spacetower_python_client.TLESGP4ExtrapolationApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extrapolate_tle**](TLESGP4ExtrapolationApi.md#extrapolate_tle) | **POST** /tle-extrapolation | 
[**get_tle_extrapolation**](TLESGP4ExtrapolationApi.md#get_tle_extrapolation) | **GET** /tle-extrapolation/{id} | 
[**get_tle_extrapolation_result**](TLESGP4ExtrapolationApi.md#get_tle_extrapolation_result) | **GET** /tle-extrapolation/result/{id} | 
[**get_tle_extrapolation_result_by_extrapolation_id**](TLESGP4ExtrapolationApi.md#get_tle_extrapolation_result_by_extrapolation_id) | **GET** /tle-extrapolation/{id}/results | 
[**retrieve_all_tle_extrapolations**](TLESGP4ExtrapolationApi.md#retrieve_all_tle_extrapolations) | **GET** /tle-extrapolations | 


# **extrapolate_tle**
> TleExtrapolationResultDto extrapolate_tle(tle_extrapolation_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.tle_extrapolation_dto import TleExtrapolationDto
from spacetower_python_client.models.tle_extrapolation_result_dto import TleExtrapolationResultDto
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
    api_instance = spacetower_python_client.TLESGP4ExtrapolationApi(api_client)
    tle_extrapolation_dto = spacetower_python_client.TleExtrapolationDto() # TleExtrapolationDto | 

    try:
        api_response = api_instance.extrapolate_tle(tle_extrapolation_dto)
        print("The response of TLESGP4ExtrapolationApi->extrapolate_tle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TLESGP4ExtrapolationApi->extrapolate_tle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tle_extrapolation_dto** | [**TleExtrapolationDto**](TleExtrapolationDto.md)|  | 

### Return type

[**TleExtrapolationResultDto**](TleExtrapolationResultDto.md)

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

# **get_tle_extrapolation**
> TleExtrapolationDto get_tle_extrapolation(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.tle_extrapolation_dto import TleExtrapolationDto
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
    api_instance = spacetower_python_client.TLESGP4ExtrapolationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_tle_extrapolation(id)
        print("The response of TLESGP4ExtrapolationApi->get_tle_extrapolation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TLESGP4ExtrapolationApi->get_tle_extrapolation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TleExtrapolationDto**](TleExtrapolationDto.md)

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

# **get_tle_extrapolation_result**
> TleExtrapolationResultDto get_tle_extrapolation_result(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.tle_extrapolation_result_dto import TleExtrapolationResultDto
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
    api_instance = spacetower_python_client.TLESGP4ExtrapolationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_tle_extrapolation_result(id)
        print("The response of TLESGP4ExtrapolationApi->get_tle_extrapolation_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TLESGP4ExtrapolationApi->get_tle_extrapolation_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TleExtrapolationResultDto**](TleExtrapolationResultDto.md)

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

# **get_tle_extrapolation_result_by_extrapolation_id**
> List[TleExtrapolationResultDto] get_tle_extrapolation_result_by_extrapolation_id(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.tle_extrapolation_result_dto import TleExtrapolationResultDto
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
    api_instance = spacetower_python_client.TLESGP4ExtrapolationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_tle_extrapolation_result_by_extrapolation_id(id)
        print("The response of TLESGP4ExtrapolationApi->get_tle_extrapolation_result_by_extrapolation_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TLESGP4ExtrapolationApi->get_tle_extrapolation_result_by_extrapolation_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[TleExtrapolationResultDto]**](TleExtrapolationResultDto.md)

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

# **retrieve_all_tle_extrapolations**
> List[TleExtrapolationDto] retrieve_all_tle_extrapolations()



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.tle_extrapolation_dto import TleExtrapolationDto
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
    api_instance = spacetower_python_client.TLESGP4ExtrapolationApi(api_client)

    try:
        api_response = api_instance.retrieve_all_tle_extrapolations()
        print("The response of TLESGP4ExtrapolationApi->retrieve_all_tle_extrapolations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TLESGP4ExtrapolationApi->retrieve_all_tle_extrapolations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TleExtrapolationDto]**](TleExtrapolationDto.md)

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

