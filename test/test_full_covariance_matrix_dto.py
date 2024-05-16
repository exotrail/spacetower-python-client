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

from spacetower_python_client.models.full_covariance_matrix_dto import FullCovarianceMatrixDto

class TestFullCovarianceMatrixDto(unittest.TestCase):
    """FullCovarianceMatrixDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FullCovarianceMatrixDto:
        """Test FullCovarianceMatrixDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FullCovarianceMatrixDto`
        """
        model = FullCovarianceMatrixDto()
        if include_optional:
            return FullCovarianceMatrixDto(
                var_date = '',
                frame = 'EME2000',
                id = '',
                matrix = [
                    [
                        1.337
                        ]
                    ],
                orbit_type = 'CARTESIAN'
            )
        else:
            return FullCovarianceMatrixDto(
                frame = 'EME2000',
                matrix = [
                    [
                        1.337
                        ]
                    ],
                orbit_type = 'CARTESIAN',
        )
        """

    def testFullCovarianceMatrixDto(self):
        """Test FullCovarianceMatrixDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
