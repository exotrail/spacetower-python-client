# coding: utf-8

"""
    FDS API

    API for Flight Dynamics System

    The version of the OpenAPI document: 1.0.0
    Contact: contact@exotrail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fds_api_gen_client.models.firing_analysis_dto import FiringAnalysisDto

class TestFiringAnalysisDto(unittest.TestCase):
    """FiringAnalysisDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FiringAnalysisDto:
        """Test FiringAnalysisDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FiringAnalysisDto`
        """
        model = FiringAnalysisDto()
        if include_optional:
            return FiringAnalysisDto(
                argument_of_perigee_delta = 1.337,
                var_date = '',
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
                smoothed_keplerian_elements_after_firing = fds_api_gen_client.models.smoothed_keplerian_elements_dto.SmoothedKeplerianElementsDto(
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
                smoothed_keplerian_elements_before_firing = fds_api_gen_client.models.smoothed_keplerian_elements_dto.SmoothedKeplerianElementsDto(
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
                status = 'PROCESSED'
            )
        else:
            return FiringAnalysisDto(
        )
        """

    def testFiringAnalysisDto(self):
        """Test FiringAnalysisDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()