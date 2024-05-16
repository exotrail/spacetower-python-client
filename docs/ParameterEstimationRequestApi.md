# fds_api_gen_client.ParameterEstimationRequestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_drag_coefficient_estimation_request**](ParameterEstimationRequestApi.md#create_drag_coefficient_estimation_request) | **POST** /parameter-estimation-request/drag-coefficient | 
[**create_reflectivity_coefficient_estimation_request**](ParameterEstimationRequestApi.md#create_reflectivity_coefficient_estimation_request) | **POST** /parameter-estimation-request/reflectivity-coefficient | 
[**create_thrust_vector_estimation_request**](ParameterEstimationRequestApi.md#create_thrust_vector_estimation_request) | **POST** /parameter-estimation-request/thrust-vector | 
[**delete_parameter_estimation_request**](ParameterEstimationRequestApi.md#delete_parameter_estimation_request) | **DELETE** /parameter-estimation-request/{id} | 
[**retrieve_all1**](ParameterEstimationRequestApi.md#retrieve_all1) | **GET** /parameter-estimation-request/all | 
[**retrieve_parameter_estimation_request_by_id**](ParameterEstimationRequestApi.md#retrieve_parameter_estimation_request_by_id) | **GET** /parameter-estimation-request/{id} | 


# **create_drag_coefficient_estimation_request**
> object create_drag_coefficient_estimation_request(drag_coefficient_estimation_request_input_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.drag_coefficient_estimation_request_input_dto import DragCoefficientEstimationRequestInputDto
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
    api_instance = fds_api_gen_client.ParameterEstimationRequestApi(api_client)
    drag_coefficient_estimation_request_input_dto = fds_api_gen_client.DragCoefficientEstimationRequestInputDto() # DragCoefficientEstimationRequestInputDto | 

    try:
        api_response = api_instance.create_drag_coefficient_estimation_request(drag_coefficient_estimation_request_input_dto)
        print("The response of ParameterEstimationRequestApi->create_drag_coefficient_estimation_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParameterEstimationRequestApi->create_drag_coefficient_estimation_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drag_coefficient_estimation_request_input_dto** | [**DragCoefficientEstimationRequestInputDto**](DragCoefficientEstimationRequestInputDto.md)|  | 

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

# **create_reflectivity_coefficient_estimation_request**
> object create_reflectivity_coefficient_estimation_request(reflectivity_coefficient_estimation_request_input_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.reflectivity_coefficient_estimation_request_input_dto import ReflectivityCoefficientEstimationRequestInputDto
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
    api_instance = fds_api_gen_client.ParameterEstimationRequestApi(api_client)
    reflectivity_coefficient_estimation_request_input_dto = fds_api_gen_client.ReflectivityCoefficientEstimationRequestInputDto() # ReflectivityCoefficientEstimationRequestInputDto | 

    try:
        api_response = api_instance.create_reflectivity_coefficient_estimation_request(reflectivity_coefficient_estimation_request_input_dto)
        print("The response of ParameterEstimationRequestApi->create_reflectivity_coefficient_estimation_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParameterEstimationRequestApi->create_reflectivity_coefficient_estimation_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reflectivity_coefficient_estimation_request_input_dto** | [**ReflectivityCoefficientEstimationRequestInputDto**](ReflectivityCoefficientEstimationRequestInputDto.md)|  | 

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

# **create_thrust_vector_estimation_request**
> object create_thrust_vector_estimation_request(thrust_vector_estimation_request_input_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.thrust_vector_estimation_request_input_dto import ThrustVectorEstimationRequestInputDto
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
    api_instance = fds_api_gen_client.ParameterEstimationRequestApi(api_client)
    thrust_vector_estimation_request_input_dto = fds_api_gen_client.ThrustVectorEstimationRequestInputDto() # ThrustVectorEstimationRequestInputDto | 

    try:
        api_response = api_instance.create_thrust_vector_estimation_request(thrust_vector_estimation_request_input_dto)
        print("The response of ParameterEstimationRequestApi->create_thrust_vector_estimation_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParameterEstimationRequestApi->create_thrust_vector_estimation_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thrust_vector_estimation_request_input_dto** | [**ThrustVectorEstimationRequestInputDto**](ThrustVectorEstimationRequestInputDto.md)|  | 

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

# **delete_parameter_estimation_request**
> delete_parameter_estimation_request(id)



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
    api_instance = fds_api_gen_client.ParameterEstimationRequestApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_parameter_estimation_request(id)
    except Exception as e:
        print("Exception when calling ParameterEstimationRequestApi->delete_parameter_estimation_request: %s\n" % e)
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

# **retrieve_all1**
> List[object] retrieve_all1()



### Example


```python
import fds_api_gen_client
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.ParameterEstimationRequestApi(api_client)

    try:
        api_response = api_instance.retrieve_all1()
        print("The response of ParameterEstimationRequestApi->retrieve_all1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParameterEstimationRequestApi->retrieve_all1: %s\n" % e)
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

# **retrieve_parameter_estimation_request_by_id**
> object retrieve_parameter_estimation_request_by_id(id)



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
    api_instance = fds_api_gen_client.ParameterEstimationRequestApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_parameter_estimation_request_by_id(id)
        print("The response of ParameterEstimationRequestApi->retrieve_parameter_estimation_request_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParameterEstimationRequestApi->retrieve_parameter_estimation_request_by_id: %s\n" % e)
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

