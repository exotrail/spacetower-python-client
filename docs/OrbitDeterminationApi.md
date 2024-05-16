# fds_api_gen_client.OrbitDeterminationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_orbit_determination**](OrbitDeterminationApi.md#get_orbit_determination) | **GET** /determination/{id} | 
[**get_orbit_determination_result**](OrbitDeterminationApi.md#get_orbit_determination_result) | **GET** /determination/result/{id} | 
[**get_orbit_determination_result_by_determination_id**](OrbitDeterminationApi.md#get_orbit_determination_result_by_determination_id) | **GET** /determination/{id}/results | 
[**retrieve_all_orbit_determinations**](OrbitDeterminationApi.md#retrieve_all_orbit_determinations) | **GET** /determinations | 
[**run_ukf_orbit_determination**](OrbitDeterminationApi.md#run_ukf_orbit_determination) | **POST** /determination/ukf | 


# **get_orbit_determination**
> object get_orbit_determination(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = fds_api_gen_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.OrbitDeterminationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_orbit_determination(id)
        print("The response of OrbitDeterminationApi->get_orbit_determination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDeterminationApi->get_orbit_determination: %s\n" % e)
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

# **get_orbit_determination_result**
> OrbitDeterminationResultDto get_orbit_determination_result(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.orbit_determination_result_dto import OrbitDeterminationResultDto
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = fds_api_gen_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.OrbitDeterminationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_orbit_determination_result(id)
        print("The response of OrbitDeterminationApi->get_orbit_determination_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDeterminationApi->get_orbit_determination_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrbitDeterminationResultDto**](OrbitDeterminationResultDto.md)

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

# **get_orbit_determination_result_by_determination_id**
> List[OrbitDeterminationResultDto] get_orbit_determination_result_by_determination_id(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.orbit_determination_result_dto import OrbitDeterminationResultDto
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = fds_api_gen_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.OrbitDeterminationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_orbit_determination_result_by_determination_id(id)
        print("The response of OrbitDeterminationApi->get_orbit_determination_result_by_determination_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDeterminationApi->get_orbit_determination_result_by_determination_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[OrbitDeterminationResultDto]**](OrbitDeterminationResultDto.md)

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

# **retrieve_all_orbit_determinations**
> List[object] retrieve_all_orbit_determinations()



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = fds_api_gen_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.OrbitDeterminationApi(api_client)

    try:
        api_response = api_instance.retrieve_all_orbit_determinations()
        print("The response of OrbitDeterminationApi->retrieve_all_orbit_determinations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDeterminationApi->retrieve_all_orbit_determinations: %s\n" % e)
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

# **run_ukf_orbit_determination**
> OrbitDeterminationResultDto run_ukf_orbit_determination(ukf_orbit_determination_input_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.orbit_determination_result_dto import OrbitDeterminationResultDto
from fds_api_gen_client.models.ukf_orbit_determination_input_dto import UkfOrbitDeterminationInputDto
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = fds_api_gen_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.OrbitDeterminationApi(api_client)
    ukf_orbit_determination_input_dto = fds_api_gen_client.UkfOrbitDeterminationInputDto() # UkfOrbitDeterminationInputDto | 

    try:
        api_response = api_instance.run_ukf_orbit_determination(ukf_orbit_determination_input_dto)
        print("The response of OrbitDeterminationApi->run_ukf_orbit_determination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDeterminationApi->run_ukf_orbit_determination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ukf_orbit_determination_input_dto** | [**UkfOrbitDeterminationInputDto**](UkfOrbitDeterminationInputDto.md)|  | 

### Return type

[**OrbitDeterminationResultDto**](OrbitDeterminationResultDto.md)

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

