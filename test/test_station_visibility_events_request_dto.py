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

from fds_api_gen_client.models.station_visibility_events_request_dto import StationVisibilityEventsRequestDto

class TestStationVisibilityEventsRequestDto(unittest.TestCase):
    """StationVisibilityEventsRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StationVisibilityEventsRequestDto:
        """Test StationVisibilityEventsRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StationVisibilityEventsRequestDto`
        """
        model = StationVisibilityEventsRequestDto()
        if include_optional:
            return StationVisibilityEventsRequestDto(
                ground_station_ids = [
                    ''
                    ],
                id = '',
                start_date = ''
            )
        else:
            return StationVisibilityEventsRequestDto(
                ground_station_ids = [
                    ''
                    ],
        )
        """

    def testStationVisibilityEventsRequestDto(self):
        """Test StationVisibilityEventsRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()