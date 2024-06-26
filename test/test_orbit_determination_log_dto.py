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

from spacetower_python_client.models.orbit_determination_log_dto import OrbitDeterminationLogDto

class TestOrbitDeterminationLogDto(unittest.TestCase):
    """OrbitDeterminationLogDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbitDeterminationLogDto:
        """Test OrbitDeterminationLogDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrbitDeterminationLogDto`
        """
        model = OrbitDeterminationLogDto()
        if include_optional:
            return OrbitDeterminationLogDto(
                computation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                computation_status = 'COMPUTATION_FAILURE',
                error_messages = [
                    ''
                    ],
                id = ''
            )
        else:
            return OrbitDeterminationLogDto(
        )
        """

    def testOrbitDeterminationLogDto(self):
        """Test OrbitDeterminationLogDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
