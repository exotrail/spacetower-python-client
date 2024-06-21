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

from spacetower_python_client.models.keplerian_orbit_dto import KeplerianOrbitDto

class TestKeplerianOrbitDto(unittest.TestCase):
    """KeplerianOrbitDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeplerianOrbitDto:
        """Test KeplerianOrbitDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeplerianOrbitDto`
        """
        model = KeplerianOrbitDto()
        if include_optional:
            return KeplerianOrbitDto(
                anomaly = 1.337,
                argument_of_perigee = 1.337,
                var_date = '',
                eccentricity = 1.337,
                frame = 'EME2000',
                id = '',
                inclination = 1.337,
                mean_osc_type = 'MEAN',
                position_angle_type = 'TRUE',
                raan = 1.337,
                semi_major_axis = 1.337
            )
        else:
            return KeplerianOrbitDto(
                anomaly = 1.337,
                argument_of_perigee = 1.337,
                var_date = '',
                eccentricity = 1.337,
                frame = 'EME2000',
                inclination = 1.337,
                mean_osc_type = 'MEAN',
                position_angle_type = 'TRUE',
                raan = 1.337,
                semi_major_axis = 1.337,
        )
        """

    def testKeplerianOrbitDto(self):
        """Test KeplerianOrbitDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
