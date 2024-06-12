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

from spacetower_python_client.models.sensor_event_request_dto import SensorEventRequestDto

class TestSensorEventRequestDto(unittest.TestCase):
    """SensorEventRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SensorEventRequestDto:
        """Test SensorEventRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SensorEventRequestDto`
        """
        model = SensorEventRequestDto()
        if include_optional:
            return SensorEventRequestDto(
                ephemerides_step = 1.337,
                events_type = [
                    'SUN_IN_FOV'
                    ],
                id = '',
                sensor_axis_in_spacecraft_frame = [
                    1.337
                    ],
                sensor_field_of_view_half_angle = 1.337,
                start_date = ''
            )
        else:
            return SensorEventRequestDto(
                ephemerides_step = 1.337,
                events_type = [
                    'SUN_IN_FOV'
                    ],
                sensor_axis_in_spacecraft_frame = [
                    1.337
                    ],
                sensor_field_of_view_half_angle = 1.337,
        )
        """

    def testSensorEventRequestDto(self):
        """Test SensorEventRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
