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

from fds_api_gen_client.models.maneuver_generation_dto import ManeuverGenerationDto

class TestManeuverGenerationDto(unittest.TestCase):
    """ManeuverGenerationDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManeuverGenerationDto:
        """Test ManeuverGenerationDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManeuverGenerationDto`
        """
        model = ManeuverGenerationDto()
        if include_optional:
            return ManeuverGenerationDto(
                delta_eccentricity = 1.337,
                delta_inclination = 1.337,
                delta_semi_major_axis = 1.337,
                id = '',
                initial_orbit = None,
                maximum_duration = 1.337,
                orbital_states_required = 'NONE',
                propagation_context = fds_api_gen_client.models.propagation_context_dto.PropagationContextDto(
                    atmosphere_type = 'HARRIS_PRIESTER', 
                    earth_potential_deg = 2, 
                    earth_potential_ord = 56, 
                    id = '', 
                    integrator_max_step = 0.001, 
                    integrator_min_step = 0.001, 
                    integrator_type = 'DORMAND_PRINCE_853', 
                    perturbations = [
                        'EARTH_POTENTIAL'
                        ], 
                    solar_flux = 1.337, ),
                quaternion_step = 1.337,
                spacecraft = None,
                strategy = fds_api_gen_client.models.maneuver_strategy_dto.ManeuverStrategyDto(
                    id = '', 
                    number_of_rest_orbits = 56, 
                    number_of_shift_orbits = 56, 
                    number_of_thrust_orbits = 56, 
                    orbital_duty_cycle = 1.337, 
                    stop_thrust_at_eclipse = True, 
                    thrust_arc_definition = 'DUTY_CYCLE', 
                    thrust_arc_duration = 1.337, 
                    thrust_arcs_number = 'ONE', 
                    thrust_arcs_position = 'ASCENDING_AND_DESCENDING_NODES', )
            )
        else:
            return ManeuverGenerationDto(
        )
        """

    def testManeuverGenerationDto(self):
        """Test ManeuverGenerationDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
