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

from fds_api_gen_client.models.orbit_extrapolation_input_dto import OrbitExtrapolationInputDto

class TestOrbitExtrapolationInputDto(unittest.TestCase):
    """OrbitExtrapolationInputDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbitExtrapolationInputDto:
        """Test OrbitExtrapolationInputDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrbitExtrapolationInputDto`
        """
        model = OrbitExtrapolationInputDto()
        if include_optional:
            return OrbitExtrapolationInputDto(
                events_request_ids = [
                    ''
                    ],
                extrapolation_duration = 1.337,
                initial_orbital_state_id = '',
                measurements_request_id = '',
                orbit_data_message_request_id = '',
                roadmap_id = ''
            )
        else:
            return OrbitExtrapolationInputDto(
                extrapolation_duration = 1.337,
                initial_orbital_state_id = '',
        )
        """

    def testOrbitExtrapolationInputDto(self):
        """Test OrbitExtrapolationInputDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
