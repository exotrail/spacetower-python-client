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

from spacetower_python_client.models.cartesian_orbit_dto import CartesianOrbitDto

class TestCartesianOrbitDto(unittest.TestCase):
    """CartesianOrbitDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CartesianOrbitDto:
        """Test CartesianOrbitDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CartesianOrbitDto`
        """
        model = CartesianOrbitDto()
        if include_optional:
            return CartesianOrbitDto(
                var_date = '',
                frame = 'EME2000',
                id = '',
                position_x = 1.337,
                position_y = 1.337,
                position_z = 1.337,
                velocity_x = 1.337,
                velocity_y = 1.337,
                velocity_z = 1.337
            )
        else:
            return CartesianOrbitDto(
                var_date = '',
                frame = 'EME2000',
                position_x = 1.337,
                position_y = 1.337,
                position_z = 1.337,
                velocity_x = 1.337,
                velocity_y = 1.337,
                velocity_z = 1.337,
        )
        """

    def testCartesianOrbitDto(self):
        """Test CartesianOrbitDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
