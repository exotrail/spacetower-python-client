# coding: utf-8

# flake8: noqa

"""
    FDS API

    API for Flight Dynamics System

    The version of the OpenAPI document: 1.0.0
    Contact: contact@exotrail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from spacetower_python_client.api.battery_api import BatteryApi
from spacetower_python_client.api.covariance_matrix_api import CovarianceMatrixApi
from spacetower_python_client.api.ephemeris_request_controller_api import EphemerisRequestControllerApi
from spacetower_python_client.api.events_request_api import EventsRequestApi
from spacetower_python_client.api.ground_station_api import GroundStationApi
from spacetower_python_client.api.maneuver_generation_api import ManeuverGenerationApi
from spacetower_python_client.api.maneuver_strategy_api import ManeuverStrategyApi
from spacetower_python_client.api.measurements_request_api import MeasurementsRequestApi
from spacetower_python_client.api.orbit_api import OrbitApi
from spacetower_python_client.api.orbit_data_message_request_api import OrbitDataMessageRequestApi
from spacetower_python_client.api.orbit_determination_api import OrbitDeterminationApi
from spacetower_python_client.api.orbit_determination_configuration_api import OrbitDeterminationConfigurationApi
from spacetower_python_client.api.orbit_extrapolation_api import OrbitExtrapolationApi
from spacetower_python_client.api.orbital_state_api import OrbitalStateApi
from spacetower_python_client.api.parameter_estimation_request_api import ParameterEstimationRequestApi
from spacetower_python_client.api.propagation_context_api import PropagationContextApi
from spacetower_python_client.api.roadmap_api import RoadmapApi
from spacetower_python_client.api.roadmap_action_api import RoadmapActionApi
from spacetower_python_client.api.solar_array_api import SolarArrayApi
from spacetower_python_client.api.spacecraft_api import SpacecraftApi
from spacetower_python_client.api.tlesgp4_extrapolation_api import TLESGP4ExtrapolationApi
from spacetower_python_client.api.telemetry_api import TelemetryApi
from spacetower_python_client.api.thruster_api import ThrusterApi

# import ApiClient
from spacetower_python_client.api_response import ApiResponse
from spacetower_python_client.api_client import ApiClient
from spacetower_python_client.configuration import Configuration
from spacetower_python_client.exceptions import OpenApiException
from spacetower_python_client.exceptions import ApiTypeError
from spacetower_python_client.exceptions import ApiValueError
from spacetower_python_client.exceptions import ApiKeyError
from spacetower_python_client.exceptions import ApiAttributeError
from spacetower_python_client.exceptions import ApiException

# import models into sdk package
from spacetower_python_client.models.attitude_action_dto import AttitudeActionDto
from spacetower_python_client.models.battery_dto import BatteryDto
from spacetower_python_client.models.box_spacecraft_input_dto import BoxSpacecraftInputDto
from spacetower_python_client.models.cartesian_orbit_dto import CartesianOrbitDto
from spacetower_python_client.models.chemical_thruster_dto import ChemicalThrusterDto
from spacetower_python_client.models.circular_orbit_dto import CircularOrbitDto
from spacetower_python_client.models.create_ukf_orbit_determination_configuration200_response import CreateUkfOrbitDeterminationConfiguration200Response
from spacetower_python_client.models.diagonal_covariance_matrix_dto import DiagonalCovarianceMatrixDto
from spacetower_python_client.models.drag_coefficient_estimation_request_input_dto import DragCoefficientEstimationRequestInputDto
from spacetower_python_client.models.electrical_thruster_dto import ElectricalThrusterDto
from spacetower_python_client.models.ephemeris_dto import EphemerisDto
from spacetower_python_client.models.ephemeris_request_dto import EphemerisRequestDto
from spacetower_python_client.models.equinoctial_orbit_dto import EquinoctialOrbitDto
from spacetower_python_client.models.estimated_parameter_dto import EstimatedParameterDto
from spacetower_python_client.models.firing_action_dto import FiringActionDto
from spacetower_python_client.models.firing_analysis_dto import FiringAnalysisDto
from spacetower_python_client.models.firing_analysis_report_dto import FiringAnalysisReportDto
from spacetower_python_client.models.full_covariance_matrix_dto import FullCovarianceMatrixDto
from spacetower_python_client.models.gps_nmea_measurements_request_dto import GpsNmeaMeasurementsRequestDto
from spacetower_python_client.models.gps_nmea_raw_telemetry_dto import GpsNmeaRawTelemetryDto
from spacetower_python_client.models.gps_nmea_telemetry_dto import GpsNmeaTelemetryDto
from spacetower_python_client.models.gps_pv_measurements_request_dto import GpsPvMeasurementsRequestDto
from spacetower_python_client.models.gps_pv_telemetry_dto import GpsPvTelemetryDto
from spacetower_python_client.models.ground_station_dto import GroundStationDto
from spacetower_python_client.models.keplerian_orbit_dto import KeplerianOrbitDto
from spacetower_python_client.models.maneuver_generation_input_dto import ManeuverGenerationInputDto
from spacetower_python_client.models.maneuver_generation_log_dto import ManeuverGenerationLogDto
from spacetower_python_client.models.maneuver_generation_output_dto import ManeuverGenerationOutputDto
from spacetower_python_client.models.maneuver_generation_report_dto import ManeuverGenerationReportDto
from spacetower_python_client.models.maneuver_generation_result_dto import ManeuverGenerationResultDto
from spacetower_python_client.models.maneuver_strategy_dto import ManeuverStrategyDto
from spacetower_python_client.models.oem_request_dto import OemRequestDto
from spacetower_python_client.models.optical_measurements_request_dto import OpticalMeasurementsRequestDto
from spacetower_python_client.models.optical_telemetry_dto import OpticalTelemetryDto
from spacetower_python_client.models.orbit_determination_in_depth_results_dto import OrbitDeterminationInDepthResultsDto
from spacetower_python_client.models.orbit_determination_log_dto import OrbitDeterminationLogDto
from spacetower_python_client.models.orbit_determination_report_dto import OrbitDeterminationReportDto
from spacetower_python_client.models.orbit_determination_residual_statistics_dto import OrbitDeterminationResidualStatisticsDto
from spacetower_python_client.models.orbit_determination_result_dto import OrbitDeterminationResultDto
from spacetower_python_client.models.orbit_extrapolation_input_dto import OrbitExtrapolationInputDto
from spacetower_python_client.models.orbit_extrapolation_log_dto import OrbitExtrapolationLogDto
from spacetower_python_client.models.orbit_extrapolation_output_dto import OrbitExtrapolationOutputDto
from spacetower_python_client.models.orbit_extrapolation_result_dto import OrbitExtrapolationResultDto
from spacetower_python_client.models.orbital_events_request_dto import OrbitalEventsRequestDto
from spacetower_python_client.models.orbital_state_creation_request_dto import OrbitalStateCreationRequestDto
from spacetower_python_client.models.orbital_state_dto import OrbitalStateDto
from spacetower_python_client.models.outlier_manager_settings_dto import OutlierManagerSettingsDto
from spacetower_python_client.models.propagation_context_dto import PropagationContextDto
from spacetower_python_client.models.quaternion_action_dto import QuaternionActionDto
from spacetower_python_client.models.radar_measurements_request_dto import RadarMeasurementsRequestDto
from spacetower_python_client.models.radar_telemetry_dto import RadarTelemetryDto
from spacetower_python_client.models.reflectivity_coefficient_estimation_request_input_dto import ReflectivityCoefficientEstimationRequestInputDto
from spacetower_python_client.models.residual_dto import ResidualDto
from spacetower_python_client.models.roadmap_from_actions_dto import RoadmapFromActionsDto
from spacetower_python_client.models.sensor_event_request_dto import SensorEventRequestDto
from spacetower_python_client.models.smoothed_keplerian_elements_dto import SmoothedKeplerianElementsDto
from spacetower_python_client.models.solar_array_dto import SolarArrayDto
from spacetower_python_client.models.spherical_spacecraft_dto import SphericalSpacecraftDto
from spacetower_python_client.models.station_visibility_events_request_dto import StationVisibilityEventsRequestDto
from spacetower_python_client.models.tle import TLE
from spacetower_python_client.models.thrust_vector_estimation_request_input_dto import ThrustVectorEstimationRequestInputDto
from spacetower_python_client.models.tle_extrapolation_dto import TleExtrapolationDto
from spacetower_python_client.models.tle_extrapolation_result_dto import TleExtrapolationResultDto
from spacetower_python_client.models.ukf_orbit_determination_configuration_dto import UkfOrbitDeterminationConfigurationDto
from spacetower_python_client.models.ukf_orbit_determination_input_dto import UkfOrbitDeterminationInputDto