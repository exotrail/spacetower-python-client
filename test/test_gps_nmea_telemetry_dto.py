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

from spacetower_python_client.models.gps_nmea_telemetry_dto import GpsNmeaTelemetryDto

class TestGpsNmeaTelemetryDto(unittest.TestCase):
    """GpsNmeaTelemetryDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GpsNmeaTelemetryDto:
        """Test GpsNmeaTelemetryDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GpsNmeaTelemetryDto`
        """
        model = GpsNmeaTelemetryDto()
        if include_optional:
            return GpsNmeaTelemetryDto(
                altitude_standard_deviation = 1.337,
                dates = [
                    ''
                    ],
                ground_speed_standard_deviation = 1.337,
                id = '',
                latitude_standard_deviation = 1.337,
                longitude_standard_deviation = 1.337,
                measurements = [
                    [
                        1.337
                        ]
                    ]
            )
        else:
            return GpsNmeaTelemetryDto(
                altitude_standard_deviation = 1.337,
                dates = [
                    ''
                    ],
                ground_speed_standard_deviation = 1.337,
                latitude_standard_deviation = 1.337,
                longitude_standard_deviation = 1.337,
                measurements = [
                    [
                        1.337
                        ]
                    ],
        )
        """

    def testGpsNmeaTelemetryDto(self):
        """Test GpsNmeaTelemetryDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
