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

from spacetower_python_client.models.create_ukf_orbit_determination_configuration200_response import CreateUkfOrbitDeterminationConfiguration200Response

class TestCreateUkfOrbitDeterminationConfiguration200Response(unittest.TestCase):
    """CreateUkfOrbitDeterminationConfiguration200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUkfOrbitDeterminationConfiguration200Response:
        """Test CreateUkfOrbitDeterminationConfiguration200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUkfOrbitDeterminationConfiguration200Response`
        """
        model = CreateUkfOrbitDeterminationConfiguration200Response()
        if include_optional:
            return CreateUkfOrbitDeterminationConfiguration200Response(
                alpha = 1.337,
                beta = 1.337,
                id = '',
                kappa = 1.337,
                noise_provider_type = 'BASIC',
                outlier_manager_settings = spacetower_python_client.models.outlier_manager_settings_dto.OutlierManagerSettingsDto(
                    outlier_manager_scale = 1.337, 
                    outliers_manager_warmup = 56, ),
                process_noise_matrix_id = ''
            )
        else:
            return CreateUkfOrbitDeterminationConfiguration200Response(
                alpha = 1.337,
                beta = 1.337,
                kappa = 1.337,
                noise_provider_type = 'BASIC',
                process_noise_matrix_id = '',
        )
        """

    def testCreateUkfOrbitDeterminationConfiguration200Response(self):
        """Test CreateUkfOrbitDeterminationConfiguration200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
