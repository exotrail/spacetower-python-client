# coding: utf-8

"""
    FDS API

    API for Flight Dynamics System

    The version of the OpenAPI document: 1.1.0
    Contact: contact@exotrail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from spacetower_python_client.models.firing_analysis_report_dto import FiringAnalysisReportDto

class TestFiringAnalysisReportDto(unittest.TestCase):
    """FiringAnalysisReportDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FiringAnalysisReportDto:
        """Test FiringAnalysisReportDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FiringAnalysisReportDto`
        """
        model = FiringAnalysisReportDto()
        if include_optional:
            return FiringAnalysisReportDto(
                failed_analyses_dates = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                number_of_failed_analyses = 56,
                number_of_pending_analyses = 56,
                number_of_processed_analyses = 56,
                pending_analyses_dates = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                processed_analyses = [
                    spacetower_python_client.models.firing_analysis_dto.FiringAnalysisDto(
                        argument_of_perigee_delta = 1.337, 
                        date = '', 
                        eccentricity_delta = 1.337, 
                        estimated_acceleration = 1.337, 
                        estimated_thrust = 1.337, 
                        estimated_thrust_tnw_direction = [
                            1.337
                            ], 
                        id = '', 
                        inclination_delta = 1.337, 
                        raan_delta = 1.337, 
                        semi_major_axis_delta = 1.337, 
                        smoothed_keplerian_elements_after_firing = spacetower_python_client.models.smoothed_keplerian_elements_dto.SmoothedKeplerianElementsDto(
                            argument_of_perigee = 1.337, 
                            argument_of_perigee_standard_deviation = 1.337, 
                            eccentricity = 1.337, 
                            eccentricity_standard_deviation = 1.337, 
                            id = '', 
                            inclination = 1.337, 
                            inclination_standard_deviation = 1.337, 
                            raan = 1.337, 
                            raan_standard_deviation = 1.337, 
                            semi_major_axis = 1.337, 
                            semi_major_axis_standard_deviation = 1.337, ), 
                        smoothed_keplerian_elements_before_firing = spacetower_python_client.models.smoothed_keplerian_elements_dto.SmoothedKeplerianElementsDto(
                            argument_of_perigee = 1.337, 
                            argument_of_perigee_standard_deviation = 1.337, 
                            eccentricity = 1.337, 
                            eccentricity_standard_deviation = 1.337, 
                            id = '', 
                            inclination = 1.337, 
                            inclination_standard_deviation = 1.337, 
                            raan = 1.337, 
                            raan_standard_deviation = 1.337, 
                            semi_major_axis = 1.337, 
                            semi_major_axis_standard_deviation = 1.337, ), 
                        status = 'PROCESSED', )
                    ]
            )
        else:
            return FiringAnalysisReportDto(
        )
        """

    def testFiringAnalysisReportDto(self):
        """Test FiringAnalysisReportDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
