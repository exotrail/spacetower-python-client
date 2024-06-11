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

from spacetower_python_client.models.diagonal_covariance_matrix_dto import DiagonalCovarianceMatrixDto

class TestDiagonalCovarianceMatrixDto(unittest.TestCase):
    """DiagonalCovarianceMatrixDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiagonalCovarianceMatrixDto:
        """Test DiagonalCovarianceMatrixDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiagonalCovarianceMatrixDto`
        """
        model = DiagonalCovarianceMatrixDto()
        if include_optional:
            return DiagonalCovarianceMatrixDto(
                var_date = '',
                diagonal = [
                    1.337
                    ],
                frame = 'EME2000',
                id = '',
                orbit_type = 'CARTESIAN'
            )
        else:
            return DiagonalCovarianceMatrixDto(
                diagonal = [
                    1.337
                    ],
                frame = 'EME2000',
                orbit_type = 'CARTESIAN',
        )
        """

    def testDiagonalCovarianceMatrixDto(self):
        """Test DiagonalCovarianceMatrixDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
