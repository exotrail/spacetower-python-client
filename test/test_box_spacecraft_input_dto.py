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

from spacetower_python_client.models.box_spacecraft_input_dto import BoxSpacecraftInputDto

class TestBoxSpacecraftInputDto(unittest.TestCase):
    """BoxSpacecraftInputDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BoxSpacecraftInputDto:
        """Test BoxSpacecraftInputDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BoxSpacecraftInputDto`
        """
        model = BoxSpacecraftInputDto()
        if include_optional:
            return BoxSpacecraftInputDto(
                battery_id = '',
                drag_coefficient = 1.337,
                id = '',
                max_angular_acceleration = 1.337,
                max_angular_velocity = 1.337,
                platform_mass = 1.337,
                reflection_coefficient = 1.337,
                solar_array_id = '',
                spacecraft_length_x = 1.337,
                spacecraft_length_y = 1.337,
                spacecraft_length_z = 1.337,
                thruster_id = ''
            )
        else:
            return BoxSpacecraftInputDto(
                battery_id = '',
                drag_coefficient = 1.337,
                max_angular_acceleration = 1.337,
                max_angular_velocity = 1.337,
                platform_mass = 1.337,
                solar_array_id = '',
                spacecraft_length_x = 1.337,
                spacecraft_length_y = 1.337,
                spacecraft_length_z = 1.337,
                thruster_id = '',
        )
        """

    def testBoxSpacecraftInputDto(self):
        """Test BoxSpacecraftInputDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
