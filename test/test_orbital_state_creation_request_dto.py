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

from spacetower_python_client.models.orbital_state_creation_request_dto import OrbitalStateCreationRequestDto

class TestOrbitalStateCreationRequestDto(unittest.TestCase):
    """OrbitalStateCreationRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbitalStateCreationRequestDto:
        """Test OrbitalStateCreationRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrbitalStateCreationRequestDto`
        """
        model = OrbitalStateCreationRequestDto()
        if include_optional:
            return OrbitalStateCreationRequestDto(
                covariance_matrix_id = '',
                orbit_id = '',
                propagation_context_id = '',
                spacecraft_id = '',
                tle = spacetower_python_client.models.tle.TLE(
                    line1 = '', 
                    line2 = '', )
            )
        else:
            return OrbitalStateCreationRequestDto(
                propagation_context_id = '',
                spacecraft_id = '',
        )
        """

    def testOrbitalStateCreationRequestDto(self):
        """Test OrbitalStateCreationRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
