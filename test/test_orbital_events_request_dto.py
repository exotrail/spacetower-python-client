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

from fds_api_gen_client.models.orbital_events_request_dto import OrbitalEventsRequestDto

class TestOrbitalEventsRequestDto(unittest.TestCase):
    """OrbitalEventsRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbitalEventsRequestDto:
        """Test OrbitalEventsRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrbitalEventsRequestDto`
        """
        model = OrbitalEventsRequestDto()
        if include_optional:
            return OrbitalEventsRequestDto(
                events_type = [
                    'NODE'
                    ],
                id = '',
                start_date = ''
            )
        else:
            return OrbitalEventsRequestDto(
                events_type = [
                    'NODE'
                    ],
        )
        """

    def testOrbitalEventsRequestDto(self):
        """Test OrbitalEventsRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()