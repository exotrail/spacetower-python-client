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

from spacetower_python_client.models.spherical_spacecraft_dto import SphericalSpacecraftDto

class TestSphericalSpacecraftDto(unittest.TestCase):
    """SphericalSpacecraftDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SphericalSpacecraftDto:
        """Test SphericalSpacecraftDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SphericalSpacecraftDto`
        """
        model = SphericalSpacecraftDto()
        if include_optional:
            return SphericalSpacecraftDto(
                drag_coefficient = 1.337,
                id = '',
                platform_mass = 1.337,
                reflection_coefficient = 1.337,
                spherical_cross_section = 1.337
            )
        else:
            return SphericalSpacecraftDto(
                drag_coefficient = 1.337,
                platform_mass = 1.337,
                spherical_cross_section = 1.337,
        )
        """

    def testSphericalSpacecraftDto(self):
        """Test SphericalSpacecraftDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
