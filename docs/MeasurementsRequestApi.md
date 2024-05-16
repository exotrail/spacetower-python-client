# spacetower_python_client.MeasurementsRequestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gps_measurements_request**](MeasurementsRequestApi.md#create_gps_measurements_request) | **POST** /measurements/requests/gps-pv | 
[**create_gps_nmea_measurements_request**](MeasurementsRequestApi.md#create_gps_nmea_measurements_request) | **POST** /measurements/requests/gps-nmea | 
[**create_optical_measurements_request**](MeasurementsRequestApi.md#create_optical_measurements_request) | **POST** /measurements/requests/optical | 
[**create_radar_measurements_request**](MeasurementsRequestApi.md#create_radar_measurements_request) | **POST** /measurements/requests/radar | 
[**delete_measurements_request**](MeasurementsRequestApi.md#delete_measurements_request) | **DELETE** /measurements/requests/{id} | 
[**retrieve_all6**](MeasurementsRequestApi.md#retrieve_all6) | **GET** /measurements/requests | 
[**retrieve_measurements_request_by_id**](MeasurementsRequestApi.md#retrieve_measurements_request_by_id) | **GET** /measurements/requests/{id} | 


# **create_gps_measurements_request**
> object create_gps_measurements_request(gps_pv_measurements_request_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.gps_pv_measurements_request_dto import GpsPvMeasurementsRequestDto
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
    api_instance = spacetower_python_client.MeasurementsRequestApi(api_client)
    gps_pv_measurements_request_dto = spacetower_python_client.GpsPvMeasurementsRequestDto() # GpsPvMeasurementsRequestDto | 

    try:
        api_response = api_instance.create_gps_measurements_request(gps_pv_measurements_request_dto)
        print("The response of MeasurementsRequestApi->create_gps_measurements_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasurementsRequestApi->create_gps_measurements_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gps_pv_measurements_request_dto** | [**GpsPvMeasurementsRequestDto**](GpsPvMeasurementsRequestDto.md)|  | 

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

# **create_gps_nmea_measurements_request**
> object create_gps_nmea_measurements_request(gps_nmea_measurements_request_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.gps_nmea_measurements_request_dto import GpsNmeaMeasurementsRequestDto
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
    api_instance = spacetower_python_client.MeasurementsRequestApi(api_client)
    gps_nmea_measurements_request_dto = spacetower_python_client.GpsNmeaMeasurementsRequestDto() # GpsNmeaMeasurementsRequestDto | 

    try:
        api_response = api_instance.create_gps_nmea_measurements_request(gps_nmea_measurements_request_dto)
        print("The response of MeasurementsRequestApi->create_gps_nmea_measurements_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasurementsRequestApi->create_gps_nmea_measurements_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gps_nmea_measurements_request_dto** | [**GpsNmeaMeasurementsRequestDto**](GpsNmeaMeasurementsRequestDto.md)|  | 

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

# **create_optical_measurements_request**
> object create_optical_measurements_request(optical_measurements_request_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.optical_measurements_request_dto import OpticalMeasurementsRequestDto
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
    api_instance = spacetower_python_client.MeasurementsRequestApi(api_client)
    optical_measurements_request_dto = spacetower_python_client.OpticalMeasurementsRequestDto() # OpticalMeasurementsRequestDto | 

    try:
        api_response = api_instance.create_optical_measurements_request(optical_measurements_request_dto)
        print("The response of MeasurementsRequestApi->create_optical_measurements_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasurementsRequestApi->create_optical_measurements_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optical_measurements_request_dto** | [**OpticalMeasurementsRequestDto**](OpticalMeasurementsRequestDto.md)|  | 

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

# **create_radar_measurements_request**
> object create_radar_measurements_request(radar_measurements_request_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.radar_measurements_request_dto import RadarMeasurementsRequestDto
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
    api_instance = spacetower_python_client.MeasurementsRequestApi(api_client)
    radar_measurements_request_dto = spacetower_python_client.RadarMeasurementsRequestDto() # RadarMeasurementsRequestDto | 

    try:
        api_response = api_instance.create_radar_measurements_request(radar_measurements_request_dto)
        print("The response of MeasurementsRequestApi->create_radar_measurements_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasurementsRequestApi->create_radar_measurements_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radar_measurements_request_dto** | [**RadarMeasurementsRequestDto**](RadarMeasurementsRequestDto.md)|  | 

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

# **delete_measurements_request**
> delete_measurements_request(id)



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
    api_instance = spacetower_python_client.MeasurementsRequestApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_measurements_request(id)
    except Exception as e:
        print("Exception when calling MeasurementsRequestApi->delete_measurements_request: %s\n" % e)
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

# **retrieve_all6**
> List[object] retrieve_all6()



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
    api_instance = spacetower_python_client.MeasurementsRequestApi(api_client)

    try:
        api_response = api_instance.retrieve_all6()
        print("The response of MeasurementsRequestApi->retrieve_all6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasurementsRequestApi->retrieve_all6: %s\n" % e)
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

# **retrieve_measurements_request_by_id**
> object retrieve_measurements_request_by_id(id)



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
    api_instance = spacetower_python_client.MeasurementsRequestApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_measurements_request_by_id(id)
        print("The response of MeasurementsRequestApi->retrieve_measurements_request_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasurementsRequestApi->retrieve_measurements_request_by_id: %s\n" % e)
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

