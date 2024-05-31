# spacetower_python_client.TelemetryApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gps_nmea_telemetry**](TelemetryApi.md#create_gps_nmea_telemetry) | **POST** /od-telemetry/gps-nmea | 
[**create_gps_nmea_telemetry_raw**](TelemetryApi.md#create_gps_nmea_telemetry_raw) | **POST** /od-telemetry/gps-nmea-raw | 
[**create_gps_pv_telemetry**](TelemetryApi.md#create_gps_pv_telemetry) | **POST** /od-telemetry/gps-pv | 
[**create_optical_telemetry**](TelemetryApi.md#create_optical_telemetry) | **POST** /od-telemetry/optical | 
[**create_radar_telemetry**](TelemetryApi.md#create_radar_telemetry) | **POST** /od-telemetry/radar | 
[**delete_telemetry**](TelemetryApi.md#delete_telemetry) | **DELETE** /od-telemetry/{id} | 
[**retrieve**](TelemetryApi.md#retrieve) | **GET** /od-telemetry/{id} | 
[**retrieve_all5**](TelemetryApi.md#retrieve_all5) | **GET** /od-telemetries | 


# **create_gps_nmea_telemetry**
> object create_gps_nmea_telemetry(gps_nmea_telemetry_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.gps_nmea_telemetry_dto import GpsNmeaTelemetryDto
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
    api_instance = spacetower_python_client.TelemetryApi(api_client)
    gps_nmea_telemetry_dto = spacetower_python_client.GpsNmeaTelemetryDto() # GpsNmeaTelemetryDto | 

    try:
        api_response = api_instance.create_gps_nmea_telemetry(gps_nmea_telemetry_dto)
        print("The response of TelemetryApi->create_gps_nmea_telemetry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryApi->create_gps_nmea_telemetry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gps_nmea_telemetry_dto** | [**GpsNmeaTelemetryDto**](GpsNmeaTelemetryDto.md)|  | 

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

# **create_gps_nmea_telemetry_raw**
> object create_gps_nmea_telemetry_raw(gps_nmea_raw_telemetry_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.gps_nmea_raw_telemetry_dto import GpsNmeaRawTelemetryDto
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
    api_instance = spacetower_python_client.TelemetryApi(api_client)
    gps_nmea_raw_telemetry_dto = spacetower_python_client.GpsNmeaRawTelemetryDto() # GpsNmeaRawTelemetryDto | 

    try:
        api_response = api_instance.create_gps_nmea_telemetry_raw(gps_nmea_raw_telemetry_dto)
        print("The response of TelemetryApi->create_gps_nmea_telemetry_raw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryApi->create_gps_nmea_telemetry_raw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gps_nmea_raw_telemetry_dto** | [**GpsNmeaRawTelemetryDto**](GpsNmeaRawTelemetryDto.md)|  | 

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

# **create_gps_pv_telemetry**
> object create_gps_pv_telemetry(gps_pv_telemetry_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.gps_pv_telemetry_dto import GpsPvTelemetryDto
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
    api_instance = spacetower_python_client.TelemetryApi(api_client)
    gps_pv_telemetry_dto = spacetower_python_client.GpsPvTelemetryDto() # GpsPvTelemetryDto | 

    try:
        api_response = api_instance.create_gps_pv_telemetry(gps_pv_telemetry_dto)
        print("The response of TelemetryApi->create_gps_pv_telemetry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryApi->create_gps_pv_telemetry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gps_pv_telemetry_dto** | [**GpsPvTelemetryDto**](GpsPvTelemetryDto.md)|  | 

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

# **create_optical_telemetry**
> object create_optical_telemetry(optical_telemetry_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.optical_telemetry_dto import OpticalTelemetryDto
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
    api_instance = spacetower_python_client.TelemetryApi(api_client)
    optical_telemetry_dto = spacetower_python_client.OpticalTelemetryDto() # OpticalTelemetryDto | 

    try:
        api_response = api_instance.create_optical_telemetry(optical_telemetry_dto)
        print("The response of TelemetryApi->create_optical_telemetry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryApi->create_optical_telemetry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optical_telemetry_dto** | [**OpticalTelemetryDto**](OpticalTelemetryDto.md)|  | 

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

# **create_radar_telemetry**
> object create_radar_telemetry(radar_telemetry_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.radar_telemetry_dto import RadarTelemetryDto
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
    api_instance = spacetower_python_client.TelemetryApi(api_client)
    radar_telemetry_dto = spacetower_python_client.RadarTelemetryDto() # RadarTelemetryDto | 

    try:
        api_response = api_instance.create_radar_telemetry(radar_telemetry_dto)
        print("The response of TelemetryApi->create_radar_telemetry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryApi->create_radar_telemetry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radar_telemetry_dto** | [**RadarTelemetryDto**](RadarTelemetryDto.md)|  | 

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

# **delete_telemetry**
> delete_telemetry(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
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
    api_instance = spacetower_python_client.TelemetryApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_telemetry(id)
    except Exception as e:
        print("Exception when calling TelemetryApi->delete_telemetry: %s\n" % e)
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

# **retrieve**
> object retrieve(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
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
    api_instance = spacetower_python_client.TelemetryApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve(id)
        print("The response of TelemetryApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryApi->retrieve: %s\n" % e)
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

# **retrieve_all5**
> List[object] retrieve_all5()



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
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
    api_instance = spacetower_python_client.TelemetryApi(api_client)

    try:
        api_response = api_instance.retrieve_all5()
        print("The response of TelemetryApi->retrieve_all5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryApi->retrieve_all5: %s\n" % e)
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

