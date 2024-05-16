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

from fds_api_gen_client.models.circular_orbit_dto import CircularOrbitDto

class TestCircularOrbitDto(unittest.TestCase):
    """CircularOrbitDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CircularOrbitDto:
        """Test CircularOrbitDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CircularOrbitDto`
        """
        model = CircularOrbitDto()
        if include_optional:
            return CircularOrbitDto(
                argument_of_latitude = 1.337,
                var_date = '',
                eccentricity_vector_x = 1.337,
                eccentricity_vector_y = 1.337,
                frame = 'EME2000',
                id = '',
                inclination = 1.337,
                mean_osc_type = 'MEAN',
                position_angle_type = 'TRUE',
                raan = 1.337,
                semi_major_axis = 1.337
            )
        else:
            return CircularOrbitDto(
                argument_of_latitude = 1.337,
                var_date = '',
                eccentricity_vector_x = 1.337,
                eccentricity_vector_y = 1.337,
                frame = 'EME2000',
                inclination = 1.337,
                mean_osc_type = 'MEAN',
                position_angle_type = 'TRUE',
                raan = 1.337,
                semi_major_axis = 1.337,
        )
        """

    def testCircularOrbitDto(self):
        """Test CircularOrbitDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()