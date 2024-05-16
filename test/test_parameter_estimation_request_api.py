# coding: utf-8

"""
    FDS API

    API for Flight Dynamics System

    The version of the OpenAPI document: 1.0.0
    Contact: contact@exotrail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from spacetower_python_client.api.parameter_estimation_request_api import ParameterEstimationRequestApi


class TestParameterEstimationRequestApi(unittest.TestCase):
    """ParameterEstimationRequestApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ParameterEstimationRequestApi()

    def tearDown(self) -> None:
        pass

    def test_create_drag_coefficient_estimation_request(self) -> None:
        """Test case for create_drag_coefficient_estimation_request

        """
        pass

    def test_create_reflectivity_coefficient_estimation_request(self) -> None:
        """Test case for create_reflectivity_coefficient_estimation_request

        """
        pass

    def test_create_thrust_vector_estimation_request(self) -> None:
        """Test case for create_thrust_vector_estimation_request

        """
        pass

    def test_delete_parameter_estimation_request(self) -> None:
        """Test case for delete_parameter_estimation_request

        """
        pass

    def test_retrieve_all1(self) -> None:
        """Test case for retrieve_all1

        """
        pass

    def test_retrieve_parameter_estimation_request_by_id(self) -> None:
        """Test case for retrieve_parameter_estimation_request_by_id

        """
        pass


if __name__ == '__main__':
    unittest.main()
