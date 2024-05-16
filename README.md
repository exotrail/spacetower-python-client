# spacetower-python-client
API for Flight Dynamics System

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import spacetower_python_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import spacetower_python_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = spacetower_python_client.BatteryApi(api_client)
    battery_dto = spacetower_python_client.BatteryDto() # BatteryDto | 

    try:
        api_response = api_instance.create_battery(battery_dto)
        print("The response of BatteryApi->create_battery:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatteryApi->create_battery: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BatteryApi* | [**create_battery**](docs/BatteryApi.md#create_battery) | **POST** /battery | 
*BatteryApi* | [**delete_battery**](docs/BatteryApi.md#delete_battery) | **DELETE** /battery/{id} | 
*BatteryApi* | [**retrieve_all_batteries**](docs/BatteryApi.md#retrieve_all_batteries) | **GET** /batteries | 
*BatteryApi* | [**retrieve_battery**](docs/BatteryApi.md#retrieve_battery) | **GET** /battery/{id} | 
*CovarianceMatrixApi* | [**create_covariance_matrix**](docs/CovarianceMatrixApi.md#create_covariance_matrix) | **POST** /covariance-matrix | 
*CovarianceMatrixApi* | [**create_diagonal_covariance_matrix**](docs/CovarianceMatrixApi.md#create_diagonal_covariance_matrix) | **POST** /covariance-matrix/diagonal | 
*CovarianceMatrixApi* | [**delete1**](docs/CovarianceMatrixApi.md#delete1) | **DELETE** /covariance-matrix/{id} | 
*CovarianceMatrixApi* | [**retrieve2**](docs/CovarianceMatrixApi.md#retrieve2) | **GET** /covariance-matrix/{id} | 
*CovarianceMatrixApi* | [**retrieve_all10**](docs/CovarianceMatrixApi.md#retrieve_all10) | **GET** /covariance-matrices | 
*EphemerisRequestControllerApi* | [**create_ephemeris_request**](docs/EphemerisRequestControllerApi.md#create_ephemeris_request) | **POST** /ephemeris-request | 
*EphemerisRequestControllerApi* | [**delete**](docs/EphemerisRequestControllerApi.md#delete) | **DELETE** /ephemeris-request/{id} | 
*EphemerisRequestControllerApi* | [**retrieve1**](docs/EphemerisRequestControllerApi.md#retrieve1) | **GET** /ephemeris-request/{id} | 
*EphemerisRequestControllerApi* | [**retrieve_all9**](docs/EphemerisRequestControllerApi.md#retrieve_all9) | **GET** /ephemeris-requests | 
*EventsRequestApi* | [**create_event_request**](docs/EventsRequestApi.md#create_event_request) | **POST** /events/request/orbital | 
*EventsRequestApi* | [**create_sensor_event_request**](docs/EventsRequestApi.md#create_sensor_event_request) | **POST** /events/request/sensor | 
*EventsRequestApi* | [**create_station_visibility_event_request**](docs/EventsRequestApi.md#create_station_visibility_event_request) | **POST** /events/request/station-visibility | 
*EventsRequestApi* | [**delete_event_request**](docs/EventsRequestApi.md#delete_event_request) | **DELETE** /events/request/{id} | 
*EventsRequestApi* | [**retrieve_all8**](docs/EventsRequestApi.md#retrieve_all8) | **GET** /events/requests | 
*EventsRequestApi* | [**retrieve_events_request**](docs/EventsRequestApi.md#retrieve_events_request) | **GET** /events/request/{id} | 
*GroundStationApi* | [**create_ground_station**](docs/GroundStationApi.md#create_ground_station) | **POST** /station | 
*GroundStationApi* | [**delete_ground_station**](docs/GroundStationApi.md#delete_ground_station) | **DELETE** /station/{id} | 
*GroundStationApi* | [**retrieve_all_stations**](docs/GroundStationApi.md#retrieve_all_stations) | **GET** /stations | 
*GroundStationApi* | [**retrieve_ground_station**](docs/GroundStationApi.md#retrieve_ground_station) | **GET** /station/{id} | 
*ManeuverGenerationApi* | [**get_maneuver_generation**](docs/ManeuverGenerationApi.md#get_maneuver_generation) | **GET** /maneuver-generation/{id} | 
*ManeuverGenerationApi* | [**get_maneuver_generation_result**](docs/ManeuverGenerationApi.md#get_maneuver_generation_result) | **GET** /maneuver-generation/result/{id} | 
*ManeuverGenerationApi* | [**get_maneuver_generation_result_by_request_id**](docs/ManeuverGenerationApi.md#get_maneuver_generation_result_by_request_id) | **GET** /maneuver-generation/{id}/results | 
*ManeuverGenerationApi* | [**retrieve_all_maneuver_generations**](docs/ManeuverGenerationApi.md#retrieve_all_maneuver_generations) | **GET** /maneuver-generations | 
*ManeuverGenerationApi* | [**run_maneuver_generation**](docs/ManeuverGenerationApi.md#run_maneuver_generation) | **POST** /maneuver-generation | 
*ManeuverStrategyApi* | [**create_maneuver_strategy**](docs/ManeuverStrategyApi.md#create_maneuver_strategy) | **POST** /maneuver-strategy | 
*ManeuverStrategyApi* | [**delete_manoeuvre_strategy**](docs/ManeuverStrategyApi.md#delete_manoeuvre_strategy) | **DELETE** /maneuver-strategy/{id} | 
*ManeuverStrategyApi* | [**retrieve_all7**](docs/ManeuverStrategyApi.md#retrieve_all7) | **GET** /maneuver-strategies | 
*ManeuverStrategyApi* | [**retrieve_manoeuvre_strategy_by_id**](docs/ManeuverStrategyApi.md#retrieve_manoeuvre_strategy_by_id) | **GET** /maneuver-strategy/{id} | 
*MeasurementsRequestApi* | [**create_gps_measurements_request**](docs/MeasurementsRequestApi.md#create_gps_measurements_request) | **POST** /measurements/requests/gps-pv | 
*MeasurementsRequestApi* | [**create_gps_nmea_measurements_request**](docs/MeasurementsRequestApi.md#create_gps_nmea_measurements_request) | **POST** /measurements/requests/gps-nmea | 
*MeasurementsRequestApi* | [**create_optical_measurements_request**](docs/MeasurementsRequestApi.md#create_optical_measurements_request) | **POST** /measurements/requests/optical | 
*MeasurementsRequestApi* | [**create_radar_measurements_request**](docs/MeasurementsRequestApi.md#create_radar_measurements_request) | **POST** /measurements/requests/radar | 
*MeasurementsRequestApi* | [**delete_measurements_request**](docs/MeasurementsRequestApi.md#delete_measurements_request) | **DELETE** /measurements/requests/{id} | 
*MeasurementsRequestApi* | [**retrieve_all6**](docs/MeasurementsRequestApi.md#retrieve_all6) | **GET** /measurements/requests | 
*MeasurementsRequestApi* | [**retrieve_measurements_request_by_id**](docs/MeasurementsRequestApi.md#retrieve_measurements_request_by_id) | **GET** /measurements/requests/{id} | 
*OrbitApi* | [**create_cartesian_orbit**](docs/OrbitApi.md#create_cartesian_orbit) | **POST** /orbit/cartesian | 
*OrbitApi* | [**create_circular_orbit**](docs/OrbitApi.md#create_circular_orbit) | **POST** /orbit/circular | 
*OrbitApi* | [**create_equinoctial_orbit**](docs/OrbitApi.md#create_equinoctial_orbit) | **POST** /orbit/equinoctial | 
*OrbitApi* | [**create_keplerian_orbit**](docs/OrbitApi.md#create_keplerian_orbit) | **POST** /orbit/keplerian | 
*OrbitApi* | [**delete_orbit**](docs/OrbitApi.md#delete_orbit) | **DELETE** /orbit/{id} | 
*OrbitApi* | [**retrieve_all2**](docs/OrbitApi.md#retrieve_all2) | **GET** /orbits | 
*OrbitApi* | [**retrieve_orbit_by_id**](docs/OrbitApi.md#retrieve_orbit_by_id) | **GET** /orbit/{id} | 
*OrbitDataMessageRequestApi* | [**create_oem_request**](docs/OrbitDataMessageRequestApi.md#create_oem_request) | **POST** /orbit-data-message/requests/oem | 
*OrbitDataMessageRequestApi* | [**delete_orbit_data_message_request**](docs/OrbitDataMessageRequestApi.md#delete_orbit_data_message_request) | **DELETE** /orbit-data-message/requests/{id} | 
*OrbitDataMessageRequestApi* | [**retrieve_all4**](docs/OrbitDataMessageRequestApi.md#retrieve_all4) | **GET** /orbit-data-message/requests | 
*OrbitDataMessageRequestApi* | [**retrieve_orbit_data_message_request_by_id**](docs/OrbitDataMessageRequestApi.md#retrieve_orbit_data_message_request_by_id) | **GET** /orbit-data-message/requests/{id} | 
*OrbitDeterminationApi* | [**get_orbit_determination**](docs/OrbitDeterminationApi.md#get_orbit_determination) | **GET** /determination/{id} | 
*OrbitDeterminationApi* | [**get_orbit_determination_result**](docs/OrbitDeterminationApi.md#get_orbit_determination_result) | **GET** /determination/result/{id} | 
*OrbitDeterminationApi* | [**get_orbit_determination_result_by_determination_id**](docs/OrbitDeterminationApi.md#get_orbit_determination_result_by_determination_id) | **GET** /determination/{id}/results | 
*OrbitDeterminationApi* | [**retrieve_all_orbit_determinations**](docs/OrbitDeterminationApi.md#retrieve_all_orbit_determinations) | **GET** /determinations | 
*OrbitDeterminationApi* | [**run_ukf_orbit_determination**](docs/OrbitDeterminationApi.md#run_ukf_orbit_determination) | **POST** /determination/ukf | 
*OrbitDeterminationConfigurationApi* | [**create_ukf_orbit_determination_configuration**](docs/OrbitDeterminationConfigurationApi.md#create_ukf_orbit_determination_configuration) | **POST** /od-configuration/ukf | 
*OrbitDeterminationConfigurationApi* | [**delete_ukf_orbit_determination_configuration**](docs/OrbitDeterminationConfigurationApi.md#delete_ukf_orbit_determination_configuration) | **DELETE** /od-configuration/{id} | 
*OrbitDeterminationConfigurationApi* | [**retrieve_all_orbit_determination_configurations**](docs/OrbitDeterminationConfigurationApi.md#retrieve_all_orbit_determination_configurations) | **GET** /od-configurations | 
*OrbitDeterminationConfigurationApi* | [**retrieve_orbit_determination_configuration_by_id**](docs/OrbitDeterminationConfigurationApi.md#retrieve_orbit_determination_configuration_by_id) | **GET** /od-configuration/{id} | 
*OrbitExtrapolationApi* | [**get_orbit_extrapolation**](docs/OrbitExtrapolationApi.md#get_orbit_extrapolation) | **GET** /extrapolation/{id} | 
*OrbitExtrapolationApi* | [**get_orbit_extrapolation_result**](docs/OrbitExtrapolationApi.md#get_orbit_extrapolation_result) | **GET** /extrapolation/result/{id} | 
*OrbitExtrapolationApi* | [**get_orbit_extrapolation_result_by_extrapolation_id**](docs/OrbitExtrapolationApi.md#get_orbit_extrapolation_result_by_extrapolation_id) | **GET** /extrapolation/{id}/results | 
*OrbitExtrapolationApi* | [**retrieve_all_orbit_extrapolations**](docs/OrbitExtrapolationApi.md#retrieve_all_orbit_extrapolations) | **GET** /extrapolations | 
*OrbitExtrapolationApi* | [**run_orbit_extrapolation**](docs/OrbitExtrapolationApi.md#run_orbit_extrapolation) | **POST** /extrapolation | 
*OrbitalStateApi* | [**create_orbital_state**](docs/OrbitalStateApi.md#create_orbital_state) | **POST** /orbital-state | 
*OrbitalStateApi* | [**delete_orbital_state**](docs/OrbitalStateApi.md#delete_orbital_state) | **DELETE** /orbital-state/{id} | 
*OrbitalStateApi* | [**retrieve_all3**](docs/OrbitalStateApi.md#retrieve_all3) | **GET** /orbital-states | 
*OrbitalStateApi* | [**retrieve_orbital_state_by_id**](docs/OrbitalStateApi.md#retrieve_orbital_state_by_id) | **GET** /orbital-state/{id} | 
*ParameterEstimationRequestApi* | [**create_drag_coefficient_estimation_request**](docs/ParameterEstimationRequestApi.md#create_drag_coefficient_estimation_request) | **POST** /parameter-estimation-request/drag-coefficient | 
*ParameterEstimationRequestApi* | [**create_reflectivity_coefficient_estimation_request**](docs/ParameterEstimationRequestApi.md#create_reflectivity_coefficient_estimation_request) | **POST** /parameter-estimation-request/reflectivity-coefficient | 
*ParameterEstimationRequestApi* | [**create_thrust_vector_estimation_request**](docs/ParameterEstimationRequestApi.md#create_thrust_vector_estimation_request) | **POST** /parameter-estimation-request/thrust-vector | 
*ParameterEstimationRequestApi* | [**delete_parameter_estimation_request**](docs/ParameterEstimationRequestApi.md#delete_parameter_estimation_request) | **DELETE** /parameter-estimation-request/{id} | 
*ParameterEstimationRequestApi* | [**retrieve_all1**](docs/ParameterEstimationRequestApi.md#retrieve_all1) | **GET** /parameter-estimation-request/all | 
*ParameterEstimationRequestApi* | [**retrieve_parameter_estimation_request_by_id**](docs/ParameterEstimationRequestApi.md#retrieve_parameter_estimation_request_by_id) | **GET** /parameter-estimation-request/{id} | 
*PropagationContextApi* | [**create_propagation_context**](docs/PropagationContextApi.md#create_propagation_context) | **POST** /propagation-context | 
*PropagationContextApi* | [**delete_propagation_context**](docs/PropagationContextApi.md#delete_propagation_context) | **DELETE** /propagation-context/{id} | 
*PropagationContextApi* | [**retrieve_all_contexts**](docs/PropagationContextApi.md#retrieve_all_contexts) | **GET** /propagation-contexts | 
*PropagationContextApi* | [**retrieve_context**](docs/PropagationContextApi.md#retrieve_context) | **GET** /propagation-context/{id} | 
*RoadmapApi* | [**create_roadmap**](docs/RoadmapApi.md#create_roadmap) | **POST** /roadmap/from-actions | 
*RoadmapApi* | [**delete_roadmap**](docs/RoadmapApi.md#delete_roadmap) | **DELETE** /roadmap/{id} | 
*RoadmapApi* | [**retrieve_all_roadmaps**](docs/RoadmapApi.md#retrieve_all_roadmaps) | **GET** /roadmaps | 
*RoadmapApi* | [**retrieve_roadmap**](docs/RoadmapApi.md#retrieve_roadmap) | **GET** /roadmap/{id} | 
*RoadmapActionApi* | [**create_attitude_action**](docs/RoadmapActionApi.md#create_attitude_action) | **POST** /roadmap-action/attitude | 
*RoadmapActionApi* | [**create_firing_action**](docs/RoadmapActionApi.md#create_firing_action) | **POST** /roadmap-action/firing | 
*RoadmapActionApi* | [**create_quaternion_action**](docs/RoadmapActionApi.md#create_quaternion_action) | **POST** /roadmap-action/quaternion | 
*RoadmapActionApi* | [**delete_roadmap_action**](docs/RoadmapActionApi.md#delete_roadmap_action) | **DELETE** /roadmap-action/{id} | 
*RoadmapActionApi* | [**retrieve_all_roadmap_actions**](docs/RoadmapActionApi.md#retrieve_all_roadmap_actions) | **GET** /roadmap-actions | 
*RoadmapActionApi* | [**retrieve_roadmap_action**](docs/RoadmapActionApi.md#retrieve_roadmap_action) | **GET** /roadmap-action/{id} | 
*SolarArrayApi* | [**create_solar_array**](docs/SolarArrayApi.md#create_solar_array) | **POST** /solar-array | 
*SolarArrayApi* | [**delete_solar_array**](docs/SolarArrayApi.md#delete_solar_array) | **DELETE** /solar-array/{id} | 
*SolarArrayApi* | [**retrieve_all_solar_arrays**](docs/SolarArrayApi.md#retrieve_all_solar_arrays) | **GET** /solar-arrays | 
*SolarArrayApi* | [**retrieve_solar_array**](docs/SolarArrayApi.md#retrieve_solar_array) | **GET** /solar-array/{id} | 
*SpacecraftApi* | [**create_box_spacecraft**](docs/SpacecraftApi.md#create_box_spacecraft) | **POST** /spacecraft/box | 
*SpacecraftApi* | [**create_spherical_spacecraft**](docs/SpacecraftApi.md#create_spherical_spacecraft) | **POST** /spacecraft/spherical | 
*SpacecraftApi* | [**delete_spacecraft**](docs/SpacecraftApi.md#delete_spacecraft) | **DELETE** /spacecraft/{id} | 
*SpacecraftApi* | [**retrieve_all**](docs/SpacecraftApi.md#retrieve_all) | **GET** /spacecrafts | 
*SpacecraftApi* | [**retrieve_spacecraft**](docs/SpacecraftApi.md#retrieve_spacecraft) | **GET** /spacecraft/{id} | 
*TLESGP4ExtrapolationApi* | [**extrapolate_tle**](docs/TLESGP4ExtrapolationApi.md#extrapolate_tle) | **POST** /tle-extrapolation | 
*TLESGP4ExtrapolationApi* | [**get_tle_extrapolation**](docs/TLESGP4ExtrapolationApi.md#get_tle_extrapolation) | **GET** /tle-extrapolation/{id} | 
*TLESGP4ExtrapolationApi* | [**get_tle_extrapolation_result**](docs/TLESGP4ExtrapolationApi.md#get_tle_extrapolation_result) | **GET** /tle-extrapolation/result/{id} | 
*TLESGP4ExtrapolationApi* | [**get_tle_extrapolation_result_by_extrapolation_id**](docs/TLESGP4ExtrapolationApi.md#get_tle_extrapolation_result_by_extrapolation_id) | **GET** /tle-extrapolation/{id}/results | 
*TLESGP4ExtrapolationApi* | [**retrieve_all_tle_extrapolations**](docs/TLESGP4ExtrapolationApi.md#retrieve_all_tle_extrapolations) | **GET** /tle-extrapolations | 
*TelemetryApi* | [**create_gps_nmea_telemetry**](docs/TelemetryApi.md#create_gps_nmea_telemetry) | **POST** /od-telemetry/gps-nmea | 
*TelemetryApi* | [**create_gps_nmea_telemetry_raw**](docs/TelemetryApi.md#create_gps_nmea_telemetry_raw) | **POST** /od-telemetry/gps-nmea-raw | 
*TelemetryApi* | [**create_gps_pv_telemetry**](docs/TelemetryApi.md#create_gps_pv_telemetry) | **POST** /od-telemetry/gps-pv | 
*TelemetryApi* | [**create_optical_telemetry**](docs/TelemetryApi.md#create_optical_telemetry) | **POST** /od-telemetry/optical | 
*TelemetryApi* | [**create_radar_telemetry**](docs/TelemetryApi.md#create_radar_telemetry) | **POST** /od-telemetry/radar | 
*TelemetryApi* | [**delete_telemetry**](docs/TelemetryApi.md#delete_telemetry) | **DELETE** /od-telemetry/{id} | 
*TelemetryApi* | [**retrieve**](docs/TelemetryApi.md#retrieve) | **GET** /od-telemetry/{id} | 
*TelemetryApi* | [**retrieve_all5**](docs/TelemetryApi.md#retrieve_all5) | **GET** /od-telemetries | 
*ThrusterApi* | [**create_chemical_thruster**](docs/ThrusterApi.md#create_chemical_thruster) | **POST** /thruster/chemical | 
*ThrusterApi* | [**create_electrical_thruster**](docs/ThrusterApi.md#create_electrical_thruster) | **POST** /thruster/electrical | 
*ThrusterApi* | [**delete_thruster**](docs/ThrusterApi.md#delete_thruster) | **DELETE** /thruster/{id} | 
*ThrusterApi* | [**retrieve_all_thrusters**](docs/ThrusterApi.md#retrieve_all_thrusters) | **GET** /thrusters | 
*ThrusterApi* | [**retrieve_thruster**](docs/ThrusterApi.md#retrieve_thruster) | **GET** /thruster/{id} | 


## Documentation For Models

 - [AttitudeActionDto](docs/AttitudeActionDto.md)
 - [BatteryDto](docs/BatteryDto.md)
 - [BoxSpacecraftInputDto](docs/BoxSpacecraftInputDto.md)
 - [CartesianOrbitDto](docs/CartesianOrbitDto.md)
 - [ChemicalThrusterDto](docs/ChemicalThrusterDto.md)
 - [CircularOrbitDto](docs/CircularOrbitDto.md)
 - [CreateUkfOrbitDeterminationConfiguration200Response](docs/CreateUkfOrbitDeterminationConfiguration200Response.md)
 - [DiagonalCovarianceMatrixDto](docs/DiagonalCovarianceMatrixDto.md)
 - [DragCoefficientEstimationRequestInputDto](docs/DragCoefficientEstimationRequestInputDto.md)
 - [ElectricalThrusterDto](docs/ElectricalThrusterDto.md)
 - [EphemerisDto](docs/EphemerisDto.md)
 - [EphemerisRequestDto](docs/EphemerisRequestDto.md)
 - [EquinoctialOrbitDto](docs/EquinoctialOrbitDto.md)
 - [EstimatedParameterDto](docs/EstimatedParameterDto.md)
 - [FiringActionDto](docs/FiringActionDto.md)
 - [FiringAnalysisDto](docs/FiringAnalysisDto.md)
 - [FiringAnalysisReportDto](docs/FiringAnalysisReportDto.md)
 - [FullCovarianceMatrixDto](docs/FullCovarianceMatrixDto.md)
 - [GpsNmeaMeasurementsRequestDto](docs/GpsNmeaMeasurementsRequestDto.md)
 - [GpsNmeaRawTelemetryDto](docs/GpsNmeaRawTelemetryDto.md)
 - [GpsNmeaTelemetryDto](docs/GpsNmeaTelemetryDto.md)
 - [GpsPvMeasurementsRequestDto](docs/GpsPvMeasurementsRequestDto.md)
 - [GpsPvTelemetryDto](docs/GpsPvTelemetryDto.md)
 - [GroundStationDto](docs/GroundStationDto.md)
 - [KeplerianOrbitDto](docs/KeplerianOrbitDto.md)
 - [ManeuverGenerationInputDto](docs/ManeuverGenerationInputDto.md)
 - [ManeuverGenerationLogDto](docs/ManeuverGenerationLogDto.md)
 - [ManeuverGenerationOutputDto](docs/ManeuverGenerationOutputDto.md)
 - [ManeuverGenerationReportDto](docs/ManeuverGenerationReportDto.md)
 - [ManeuverGenerationResultDto](docs/ManeuverGenerationResultDto.md)
 - [ManeuverStrategyDto](docs/ManeuverStrategyDto.md)
 - [OemRequestDto](docs/OemRequestDto.md)
 - [OpticalMeasurementsRequestDto](docs/OpticalMeasurementsRequestDto.md)
 - [OpticalTelemetryDto](docs/OpticalTelemetryDto.md)
 - [OrbitDeterminationInDepthResultsDto](docs/OrbitDeterminationInDepthResultsDto.md)
 - [OrbitDeterminationLogDto](docs/OrbitDeterminationLogDto.md)
 - [OrbitDeterminationReportDto](docs/OrbitDeterminationReportDto.md)
 - [OrbitDeterminationResidualStatisticsDto](docs/OrbitDeterminationResidualStatisticsDto.md)
 - [OrbitDeterminationResultDto](docs/OrbitDeterminationResultDto.md)
 - [OrbitExtrapolationInputDto](docs/OrbitExtrapolationInputDto.md)
 - [OrbitExtrapolationLogDto](docs/OrbitExtrapolationLogDto.md)
 - [OrbitExtrapolationOutputDto](docs/OrbitExtrapolationOutputDto.md)
 - [OrbitExtrapolationResultDto](docs/OrbitExtrapolationResultDto.md)
 - [OrbitalEventsRequestDto](docs/OrbitalEventsRequestDto.md)
 - [OrbitalStateCreationRequestDto](docs/OrbitalStateCreationRequestDto.md)
 - [OrbitalStateDto](docs/OrbitalStateDto.md)
 - [OutlierManagerSettingsDto](docs/OutlierManagerSettingsDto.md)
 - [PropagationContextDto](docs/PropagationContextDto.md)
 - [QuaternionActionDto](docs/QuaternionActionDto.md)
 - [RadarMeasurementsRequestDto](docs/RadarMeasurementsRequestDto.md)
 - [RadarTelemetryDto](docs/RadarTelemetryDto.md)
 - [ReflectivityCoefficientEstimationRequestInputDto](docs/ReflectivityCoefficientEstimationRequestInputDto.md)
 - [ResidualDto](docs/ResidualDto.md)
 - [RoadmapFromActionsDto](docs/RoadmapFromActionsDto.md)
 - [SensorEventRequestDto](docs/SensorEventRequestDto.md)
 - [SmoothedKeplerianElementsDto](docs/SmoothedKeplerianElementsDto.md)
 - [SolarArrayDto](docs/SolarArrayDto.md)
 - [SphericalSpacecraftDto](docs/SphericalSpacecraftDto.md)
 - [StationVisibilityEventsRequestDto](docs/StationVisibilityEventsRequestDto.md)
 - [TLE](docs/TLE.md)
 - [ThrustVectorEstimationRequestInputDto](docs/ThrustVectorEstimationRequestInputDto.md)
 - [TleExtrapolationDto](docs/TleExtrapolationDto.md)
 - [TleExtrapolationResultDto](docs/TleExtrapolationResultDto.md)
 - [UkfOrbitDeterminationConfigurationDto](docs/UkfOrbitDeterminationConfigurationDto.md)
 - [UkfOrbitDeterminationInputDto](docs/UkfOrbitDeterminationInputDto.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

contact@exotrail.com


