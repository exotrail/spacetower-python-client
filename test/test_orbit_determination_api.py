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

from fds_api_gen_client.api.orbit_determination_api import OrbitDeterminationApi


class TestOrbitDeterminationApi(unittest.TestCase):
    """OrbitDeterminationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrbitDeterminationApi()

    def tearDown(self) -> None:
        pass

    def test_get_orbit_determination(self) -> None:
        """Test case for get_orbit_determination

        """
        pass

    def test_get_orbit_determination_result(self) -> None:
        """Test case for get_orbit_determination_result

        """
        pass

    def test_get_orbit_determination_result_by_determination_id(self) -> None:
        """Test case for get_orbit_determination_result_by_determination_id

        """
        pass

    def test_retrieve_all_orbit_determinations(self) -> None:
        """Test case for retrieve_all_orbit_determinations

        """
        pass

    def test_run_ukf_orbit_determination(self) -> None:
        """Test case for run_ukf_orbit_determination

        """
        pass


if __name__ == '__main__':
    unittest.main()
