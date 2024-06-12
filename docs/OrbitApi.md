# spacetower_python_client.OrbitApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cartesian_orbit**](OrbitApi.md#create_cartesian_orbit) | **POST** /orbit/cartesian | 
[**create_circular_orbit**](OrbitApi.md#create_circular_orbit) | **POST** /orbit/circular | 
[**create_equinoctial_orbit**](OrbitApi.md#create_equinoctial_orbit) | **POST** /orbit/equinoctial | 
[**create_keplerian_orbit**](OrbitApi.md#create_keplerian_orbit) | **POST** /orbit/keplerian | 
[**delete_orbit**](OrbitApi.md#delete_orbit) | **DELETE** /orbit/{id} | 
[**retrieve_all2**](OrbitApi.md#retrieve_all2) | **GET** /orbits | 
[**retrieve_orbit_by_id**](OrbitApi.md#retrieve_orbit_by_id) | **GET** /orbit/{id} | 


# **create_cartesian_orbit**
> object create_cartesian_orbit(cartesian_orbit_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.cartesian_orbit_dto import CartesianOrbitDto
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
    api_instance = spacetower_python_client.OrbitApi(api_client)
    cartesian_orbit_dto = spacetower_python_client.CartesianOrbitDto() # CartesianOrbitDto | 

    try:
        api_response = api_instance.create_cartesian_orbit(cartesian_orbit_dto)
        print("The response of OrbitApi->create_cartesian_orbit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitApi->create_cartesian_orbit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cartesian_orbit_dto** | [**CartesianOrbitDto**](CartesianOrbitDto.md)|  | 

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

# **create_circular_orbit**
> object create_circular_orbit(circular_orbit_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.circular_orbit_dto import CircularOrbitDto
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
    api_instance = spacetower_python_client.OrbitApi(api_client)
    circular_orbit_dto = spacetower_python_client.CircularOrbitDto() # CircularOrbitDto | 

    try:
        api_response = api_instance.create_circular_orbit(circular_orbit_dto)
        print("The response of OrbitApi->create_circular_orbit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitApi->create_circular_orbit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **circular_orbit_dto** | [**CircularOrbitDto**](CircularOrbitDto.md)|  | 

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

# **create_equinoctial_orbit**
> object create_equinoctial_orbit(equinoctial_orbit_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.equinoctial_orbit_dto import EquinoctialOrbitDto
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
    api_instance = spacetower_python_client.OrbitApi(api_client)
    equinoctial_orbit_dto = spacetower_python_client.EquinoctialOrbitDto() # EquinoctialOrbitDto | 

    try:
        api_response = api_instance.create_equinoctial_orbit(equinoctial_orbit_dto)
        print("The response of OrbitApi->create_equinoctial_orbit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitApi->create_equinoctial_orbit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **equinoctial_orbit_dto** | [**EquinoctialOrbitDto**](EquinoctialOrbitDto.md)|  | 

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

# **create_keplerian_orbit**
> object create_keplerian_orbit(keplerian_orbit_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.keplerian_orbit_dto import KeplerianOrbitDto
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
    api_instance = spacetower_python_client.OrbitApi(api_client)
    keplerian_orbit_dto = spacetower_python_client.KeplerianOrbitDto() # KeplerianOrbitDto | 

    try:
        api_response = api_instance.create_keplerian_orbit(keplerian_orbit_dto)
        print("The response of OrbitApi->create_keplerian_orbit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitApi->create_keplerian_orbit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keplerian_orbit_dto** | [**KeplerianOrbitDto**](KeplerianOrbitDto.md)|  | 

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

# **delete_orbit**
> delete_orbit(id)



### Example


```python
import spacetower_python_client
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
    api_instance = spacetower_python_client.OrbitApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_orbit(id)
    except Exception as e:
        print("Exception when calling OrbitApi->delete_orbit: %s\n" % e)
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

# **retrieve_all2**
> List[object] retrieve_all2()



### Example


```python
import spacetower_python_client
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
    api_instance = spacetower_python_client.OrbitApi(api_client)

    try:
        api_response = api_instance.retrieve_all2()
        print("The response of OrbitApi->retrieve_all2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitApi->retrieve_all2: %s\n" % e)
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

# **retrieve_orbit_by_id**
> object retrieve_orbit_by_id(id)



### Example


```python
import spacetower_python_client
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
    api_instance = spacetower_python_client.OrbitApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_orbit_by_id(id)
        print("The response of OrbitApi->retrieve_orbit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitApi->retrieve_orbit_by_id: %s\n" % e)
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

