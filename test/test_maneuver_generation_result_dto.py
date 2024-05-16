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

from fds_api_gen_client.models.maneuver_generation_result_dto import ManeuverGenerationResultDto

class TestManeuverGenerationResultDto(unittest.TestCase):
    """ManeuverGenerationResultDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManeuverGenerationResultDto:
        """Test ManeuverGenerationResultDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManeuverGenerationResultDto`
        """
        model = ManeuverGenerationResultDto()
        if include_optional:
            return ManeuverGenerationResultDto(
                id = '',
                maneuver_generation = fds_api_gen_client.models.maneuver_generation_dto.ManeuverGenerationDto(
                    delta_eccentricity = 1.337, 
                    delta_inclination = 1.337, 
                    delta_semi_major_axis = 1.337, 
                    id = '', 
                    initial_orbit = fds_api_gen_client.models.initial_orbit.initialOrbit(), 
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
                    spacecraft = fds_api_gen_client.models.spacecraft.spacecraft(), 
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
                        thrust_arcs_position = 'ASCENDING_AND_DESCENDING_NODES', ), ),
                maneuver_generation_log = fds_api_gen_client.models.maneuver_generation_log_dto.ManeuverGenerationLogDto(
                    computation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    computation_status = 'COMPUTATION_FAILURE', 
                    error_messages = [
                        ''
                        ], 
                    id = '', ),
                report = fds_api_gen_client.models.maneuver_generation_report_dto.ManeuverGenerationReportDto(
                    average_thrust_duration = 1.337, 
                    final_duty_cycle = 1.337, 
                    number_of_period = 1.337, 
                    orbital_states = [
                        fds_api_gen_client.models.orbital_state_dto.OrbitalStateDto(
                            covariance_matrix_id = '', 
                            creation_date = '', 
                            fitted_tle = fds_api_gen_client.models.tle.TLE(
                                line1 = '', 
                                line2 = '', ), 
                            id = '', 
                            mean_orbit_id = '', 
                            osculating_orbit_id = '', 
                            propagation_context_id = '', 
                            source = 'ORBIT_DETERMINATION', 
                            spacecraft_id = '', )
                        ], 
                    simulation_duration = 1.337, 
                    thruster_duty_cycle = 1.337, 
                    total_burns_duration = 1.337, 
                    total_consumption = 1.337, 
                    total_delta_v = 1.337, 
                    total_impulse = 1.337, 
                    total_number_of_burns = 56, 
                    total_warmup_duty_cycle = 1.337, ),
                roadmap = None
            )
        else:
            return ManeuverGenerationResultDto(
        )
        """

    def testManeuverGenerationResultDto(self):
        """Test ManeuverGenerationResultDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()