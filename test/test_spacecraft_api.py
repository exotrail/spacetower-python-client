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

from spacetower_python_client.api.spacecraft_api import SpacecraftApi


class TestSpacecraftApi(unittest.TestCase):
    """SpacecraftApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SpacecraftApi()

    def tearDown(self) -> None:
        pass

    def test_create_box_spacecraft(self) -> None:
        """Test case for create_box_spacecraft

        """
        pass

    def test_create_spherical_spacecraft(self) -> None:
        """Test case for create_spherical_spacecraft

        """
        pass

    def test_delete_spacecraft(self) -> None:
        """Test case for delete_spacecraft

        """
        pass

    def test_retrieve_all(self) -> None:
        """Test case for retrieve_all

        """
        pass

    def test_retrieve_spacecraft(self) -> None:
        """Test case for retrieve_spacecraft

        """
        pass


if __name__ == '__main__':
    unittest.main()
