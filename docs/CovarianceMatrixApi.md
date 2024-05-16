# fds_api_gen_client.CovarianceMatrixApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_covariance_matrix**](CovarianceMatrixApi.md#create_covariance_matrix) | **POST** /covariance-matrix | 
[**create_diagonal_covariance_matrix**](CovarianceMatrixApi.md#create_diagonal_covariance_matrix) | **POST** /covariance-matrix/diagonal | 
[**delete1**](CovarianceMatrixApi.md#delete1) | **DELETE** /covariance-matrix/{id} | 
[**retrieve2**](CovarianceMatrixApi.md#retrieve2) | **GET** /covariance-matrix/{id} | 
[**retrieve_all10**](CovarianceMatrixApi.md#retrieve_all10) | **GET** /covariance-matrices | 


# **create_covariance_matrix**
> object create_covariance_matrix(full_covariance_matrix_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.full_covariance_matrix_dto import FullCovarianceMatrixDto
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
    api_instance = fds_api_gen_client.CovarianceMatrixApi(api_client)
    full_covariance_matrix_dto = fds_api_gen_client.FullCovarianceMatrixDto() # FullCovarianceMatrixDto | 

    try:
        api_response = api_instance.create_covariance_matrix(full_covariance_matrix_dto)
        print("The response of CovarianceMatrixApi->create_covariance_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CovarianceMatrixApi->create_covariance_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_covariance_matrix_dto** | [**FullCovarianceMatrixDto**](FullCovarianceMatrixDto.md)|  | 

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

# **create_diagonal_covariance_matrix**
> object create_diagonal_covariance_matrix(diagonal_covariance_matrix_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.diagonal_covariance_matrix_dto import DiagonalCovarianceMatrixDto
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
    api_instance = fds_api_gen_client.CovarianceMatrixApi(api_client)
    diagonal_covariance_matrix_dto = fds_api_gen_client.DiagonalCovarianceMatrixDto() # DiagonalCovarianceMatrixDto | 

    try:
        api_response = api_instance.create_diagonal_covariance_matrix(diagonal_covariance_matrix_dto)
        print("The response of CovarianceMatrixApi->create_diagonal_covariance_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CovarianceMatrixApi->create_diagonal_covariance_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagonal_covariance_matrix_dto** | [**DiagonalCovarianceMatrixDto**](DiagonalCovarianceMatrixDto.md)|  | 

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

# **delete1**
> delete1(id)



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
    api_instance = fds_api_gen_client.CovarianceMatrixApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete1(id)
    except Exception as e:
        print("Exception when calling CovarianceMatrixApi->delete1: %s\n" % e)
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

# **retrieve2**
> object retrieve2(id)



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
    api_instance = fds_api_gen_client.CovarianceMatrixApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve2(id)
        print("The response of CovarianceMatrixApi->retrieve2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CovarianceMatrixApi->retrieve2: %s\n" % e)
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

# **retrieve_all10**
> List[FullCovarianceMatrixDto] retrieve_all10()



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.full_covariance_matrix_dto import FullCovarianceMatrixDto
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
    api_instance = fds_api_gen_client.CovarianceMatrixApi(api_client)

    try:
        api_response = api_instance.retrieve_all10()
        print("The response of CovarianceMatrixApi->retrieve_all10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CovarianceMatrixApi->retrieve_all10: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FullCovarianceMatrixDto]**](FullCovarianceMatrixDto.md)

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

