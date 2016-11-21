# -*- coding: utf-8 -*-

"""
    tests.controllers.test_account_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 11/21/2016
"""

import jsonpickle
from .controller_test_base import *

class AccountControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(AccountControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.account

    # Sample test case to show you how to view your account information.
    def test_test_view_account(self):
        # Parameters for the API call
        options = {}
        options['date'] = None
        options['response_type'] = None

        # Perform the API call through the SDK function
        result = self.controller.create_view_account(options)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'
        
        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


