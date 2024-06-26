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

from spacetower_python_client.models.battery_dto import BatteryDto

class TestBatteryDto(unittest.TestCase):
    """BatteryDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatteryDto:
        """Test BatteryDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatteryDto`
        """
        model = BatteryDto()
        if include_optional:
            return BatteryDto(
                depth_of_discharge = 0,
                id = '',
                initial_charge = 0,
                minimum_charge_for_firing = 0,
                nominal_capacity = 0
            )
        else:
            return BatteryDto(
                depth_of_discharge = 0,
                initial_charge = 0,
                minimum_charge_for_firing = 0,
                nominal_capacity = 0,
        )
        """

    def testBatteryDto(self):
        """Test BatteryDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
