# coding: utf-8

"""
    FDS API

    API for Flight Dynamics System

    The version of the OpenAPI document: 0.1.2
    Contact: contact@exotrail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fds_api_gen_client.models.orbit_determination_result_dto import OrbitDeterminationResultDto

class TestOrbitDeterminationResultDto(unittest.TestCase):
    """OrbitDeterminationResultDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbitDeterminationResultDto:
        """Test OrbitDeterminationResultDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrbitDeterminationResultDto`
        """
        model = OrbitDeterminationResultDto()
        if include_optional:
            return OrbitDeterminationResultDto(
                id = '',
                orbit_determination = None,
                orbit_determination_in_depth_results = fds_api_gen_client.models.orbit_determination_in_depth_results_dto.OrbitDeterminationInDepthResultsDto(
                    covariance_matrices = [
                        fds_api_gen_client.models.covariance_matrix_dto.CovarianceMatrixDto()
                        ], 
                    estimated_drag_coefficients = [
                        fds_api_gen_client.models.estimated_parameter_dto.EstimatedParameterDto(
                            date = '', 
                            id = '', 
                            value = 1.337, )
                        ], 
                    estimated_reflectivity_coefficients = [
                        fds_api_gen_client.models.estimated_parameter_dto.EstimatedParameterDto(
                            date = '', 
                            id = '', 
                            value = 1.337, )
                        ], 
                    mean_orbits = [
                        fds_api_gen_client.models.initial_orbit.initialOrbit()
                        ], 
                    osculating_orbits = [
                        fds_api_gen_client.models.initial_orbit.initialOrbit()
                        ], ),
                orbit_determination_log = fds_api_gen_client.models.orbit_determination_log_dto.OrbitDeterminationLogDto(
                    computation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    computation_status = 'COMPUTATION_FAILURE', 
                    error_messages = [
                        ''
                        ], 
                    id = '', ),
                orbit_determination_report = fds_api_gen_client.models.orbit_determination_report_dto.OrbitDeterminationReportDto(
                    estimated_states = [
                        fds_api_gen_client.models.orbital_state_dto.OrbitalStateDto(
                            covariance_matrix_id = '', 
                            creation_date = '', 
                            fitted_tle = fds_api_gen_client.models.tle.TLE(
                                line1 = '', 
                                line2 = '', ), 
                            id = '', 
                            mean_orbit_id = '', 
                            osculating_orbit_id = '', 
                            propagation_context_id = '', 
                            source = 'ORBIT_DETERMINATION', 
                            spacecraft_id = '', )
                        ], 
                    number_of_rejected_measurements = 56, 
                    number_of_used_measurements = 56, 
                    residuals_statistics = [
                        fds_api_gen_client.models.orbit_determination_residual_statistics_dto.OrbitDeterminationResidualStatisticsDto(
                            field = 'GPS_NMEA', 
                            id = '', 
                            mean = 1.337, 
                            median = 1.337, 
                            residuals = [
                                fds_api_gen_client.models.residual_dto.ResidualDto(
                                    date = '', 
                                    id = '', 
                                    value = 1.337, )
                                ], 
                            standard_deviation = 1.337, )
                        ], ),
                status = 'SUCCESS'
            )
        else:
            return OrbitDeterminationResultDto(
        )
        """

    def testOrbitDeterminationResultDto(self):
        """Test OrbitDeterminationResultDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
