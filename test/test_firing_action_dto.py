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

from spacetower_python_client.models.firing_action_dto import FiringActionDto

class TestFiringActionDto(unittest.TestCase):
    """FiringActionDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FiringActionDto:
        """Test FiringActionDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FiringActionDto`
        """
        model = FiringActionDto()
        if include_optional:
            return FiringActionDto(
                firing_attitude = 'PROGRADE',
                firing_duration = 1.337,
                id = '',
                post_firing_attitude = 'PROGRADE',
                start_firing = '',
                warm_up_attitude = 'PROGRADE',
                warm_up_duration = 1.337
            )
        else:
            return FiringActionDto(
                firing_attitude = 'PROGRADE',
                firing_duration = 1.337,
                post_firing_attitude = 'PROGRADE',
                start_firing = '',
                warm_up_duration = 1.337,
        )
        """

    def testFiringActionDto(self):
        """Test FiringActionDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
