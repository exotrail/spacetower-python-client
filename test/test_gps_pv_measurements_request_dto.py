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

from fds_api_gen_client.models.gps_pv_measurements_request_dto import GpsPvMeasurementsRequestDto

class TestGpsPvMeasurementsRequestDto(unittest.TestCase):
    """GpsPvMeasurementsRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GpsPvMeasurementsRequestDto:
        """Test GpsPvMeasurementsRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GpsPvMeasurementsRequestDto`
        """
        model = GpsPvMeasurementsRequestDto()
        if include_optional:
            return GpsPvMeasurementsRequestDto(
                frame = 'GTOD',
                generation_step = 56,
                id = '',
                position_standard_deviation = 1.337,
                velocity_standard_deviation = 1.337
            )
        else:
            return GpsPvMeasurementsRequestDto(
                frame = 'GTOD',
                generation_step = 56,
                position_standard_deviation = 1.337,
                velocity_standard_deviation = 1.337,
        )
        """

    def testGpsPvMeasurementsRequestDto(self):
        """Test GpsPvMeasurementsRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
