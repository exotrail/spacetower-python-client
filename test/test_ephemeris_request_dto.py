# coding: utf-8

"""
    FDS API

    API for Flight Dynamics System

    The version of the OpenAPI document: 1.0.6
    Contact: contact@exotrail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from spacetower_python_client.models.ephemeris_request_dto import EphemerisRequestDto

class TestEphemerisRequestDto(unittest.TestCase):
    """EphemerisRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EphemerisRequestDto:
        """Test EphemerisRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EphemerisRequestDto`
        """
        model = EphemerisRequestDto()
        if include_optional:
            return EphemerisRequestDto(
                ephemeris_types = [
                    'CARTESIAN'
                    ],
                id = '',
                step = 0
            )
        else:
            return EphemerisRequestDto(
                ephemeris_types = [
                    'CARTESIAN'
                    ],
                step = 0,
        )
        """

    def testEphemerisRequestDto(self):
        """Test EphemerisRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
