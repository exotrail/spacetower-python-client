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

from spacetower_python_client.models.chemical_thruster_dto import ChemicalThrusterDto

class TestChemicalThrusterDto(unittest.TestCase):
    """ChemicalThrusterDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChemicalThrusterDto:
        """Test ChemicalThrusterDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChemicalThrusterDto`
        """
        model = ChemicalThrusterDto()
        if include_optional:
            return ChemicalThrusterDto(
                id = '',
                impulse = 1.337,
                maximum_thrust_duration = 1.337,
                propellant_mass = 1.337,
                thrust = 1.337,
                thruster_axis_in_satellite_frame = [
                    1.337
                    ],
                thruster_isp = 1.337,
                thruster_total_mass = 1.337,
                warm_up_duration = 1.337
            )
        else:
            return ChemicalThrusterDto(
                impulse = 1.337,
                maximum_thrust_duration = 1.337,
                propellant_mass = 1.337,
                thrust = 1.337,
                thruster_axis_in_satellite_frame = [
                    1.337
                    ],
                thruster_isp = 1.337,
                thruster_total_mass = 1.337,
                warm_up_duration = 1.337,
        )
        """

    def testChemicalThrusterDto(self):
        """Test ChemicalThrusterDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
