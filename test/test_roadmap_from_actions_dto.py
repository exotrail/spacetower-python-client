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

from fds_api_gen_client.models.roadmap_from_actions_dto import RoadmapFromActionsDto

class TestRoadmapFromActionsDto(unittest.TestCase):
    """RoadmapFromActionsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoadmapFromActionsDto:
        """Test RoadmapFromActionsDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoadmapFromActionsDto`
        """
        model = RoadmapFromActionsDto()
        if include_optional:
            return RoadmapFromActionsDto(
                final_date = '',
                id = '',
                initial_date = '',
                roadmap_action_ids = [
                    ''
                    ]
            )
        else:
            return RoadmapFromActionsDto(
                final_date = '',
                initial_date = '',
                roadmap_action_ids = [
                    ''
                    ],
        )
        """

    def testRoadmapFromActionsDto(self):
        """Test RoadmapFromActionsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
