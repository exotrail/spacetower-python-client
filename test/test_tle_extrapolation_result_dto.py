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

from fds_api_gen_client.models.tle_extrapolation_result_dto import TleExtrapolationResultDto

class TestTleExtrapolationResultDto(unittest.TestCase):
    """TleExtrapolationResultDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TleExtrapolationResultDto:
        """Test TleExtrapolationResultDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TleExtrapolationResultDto`
        """
        model = TleExtrapolationResultDto()
        if include_optional:
            return TleExtrapolationResultDto(
                id = '',
                orbits = [
                    fds_api_gen_client.models.initial_orbit.initialOrbit()
                    ],
                tle_extrapolation = fds_api_gen_client.models.tle_extrapolation_dto.TleExtrapolationDto(
                    dates = [
                        ''
                        ], 
                    initial_tle = fds_api_gen_client.models.tle.TLE(
                        line1 = '', 
                        line2 = '', ), )
            )
        else:
            return TleExtrapolationResultDto(
        )
        """

    def testTleExtrapolationResultDto(self):
        """Test TleExtrapolationResultDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
