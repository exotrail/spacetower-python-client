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

from fds_api_gen_client.models.ukf_orbit_determination_input_dto import UkfOrbitDeterminationInputDto

class TestUkfOrbitDeterminationInputDto(unittest.TestCase):
    """UkfOrbitDeterminationInputDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UkfOrbitDeterminationInputDto:
        """Test UkfOrbitDeterminationInputDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UkfOrbitDeterminationInputDto`
        """
        model = UkfOrbitDeterminationInputDto()
        if include_optional:
            return UkfOrbitDeterminationInputDto(
                configuration_id = '',
                initial_orbital_state_id = '',
                parameter_estimation_request_ids = [
                    ''
                    ],
                roadmap_id = '',
                telemetry_id = ''
            )
        else:
            return UkfOrbitDeterminationInputDto(
                configuration_id = '',
                initial_orbital_state_id = '',
                telemetry_id = '',
        )
        """

    def testUkfOrbitDeterminationInputDto(self):
        """Test UkfOrbitDeterminationInputDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
