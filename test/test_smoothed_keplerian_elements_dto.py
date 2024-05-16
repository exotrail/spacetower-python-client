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

from fds_api_gen_client.models.smoothed_keplerian_elements_dto import SmoothedKeplerianElementsDto

class TestSmoothedKeplerianElementsDto(unittest.TestCase):
    """SmoothedKeplerianElementsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmoothedKeplerianElementsDto:
        """Test SmoothedKeplerianElementsDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SmoothedKeplerianElementsDto`
        """
        model = SmoothedKeplerianElementsDto()
        if include_optional:
            return SmoothedKeplerianElementsDto(
                argument_of_perigee = 1.337,
                argument_of_perigee_standard_deviation = 1.337,
                eccentricity = 1.337,
                eccentricity_standard_deviation = 1.337,
                id = '',
                inclination = 1.337,
                inclination_standard_deviation = 1.337,
                raan = 1.337,
                raan_standard_deviation = 1.337,
                semi_major_axis = 1.337,
                semi_major_axis_standard_deviation = 1.337
            )
        else:
            return SmoothedKeplerianElementsDto(
        )
        """

    def testSmoothedKeplerianElementsDto(self):
        """Test SmoothedKeplerianElementsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
