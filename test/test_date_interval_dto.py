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

from spacetower_python_client.models.date_interval_dto import DateIntervalDto

class TestDateIntervalDto(unittest.TestCase):
    """DateIntervalDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DateIntervalDto:
        """Test DateIntervalDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DateIntervalDto`
        """
        model = DateIntervalDto()
        if include_optional:
            return DateIntervalDto(
                end = '',
                start = ''
            )
        else:
            return DateIntervalDto(
        )
        """

    def testDateIntervalDto(self):
        """Test DateIntervalDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
