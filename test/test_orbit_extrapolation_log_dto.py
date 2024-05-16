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

from fds_api_gen_client.models.orbit_extrapolation_log_dto import OrbitExtrapolationLogDto

class TestOrbitExtrapolationLogDto(unittest.TestCase):
    """OrbitExtrapolationLogDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbitExtrapolationLogDto:
        """Test OrbitExtrapolationLogDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrbitExtrapolationLogDto`
        """
        model = OrbitExtrapolationLogDto()
        if include_optional:
            return OrbitExtrapolationLogDto(
                computation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                computation_status = 'COMPUTATION_FAILURE',
                error_messages = [
                    ''
                    ],
                id = ''
            )
        else:
            return OrbitExtrapolationLogDto(
        )
        """

    def testOrbitExtrapolationLogDto(self):
        """Test OrbitExtrapolationLogDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()