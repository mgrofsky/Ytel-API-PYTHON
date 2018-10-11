# -*- coding: utf-8 -*-

"""
    ytelapiv3

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from ytelapiv3.api_helper import APIHelper


class EmailControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(EmailControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.email

    # Retrieve a list of emails that have been blocked.
    def test_test_blocked_emails(self):
        # Parameters for the API call
        offset = None
        limit = None

        # Perform the API call through the SDK function
        result = self.controller.create_blocked_emails(offset, limit)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Retrieve a list of emails that are on the spam list.
    def test_test_spam_emails(self):
        # Parameters for the API call
        offset = None
        limit = None

        # Perform the API call through the SDK function
        result = self.controller.create_spam_emails(offset, limit)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Retrieve a list of emails that have bounced.
    def test_test_bounced_emails(self):
        # Parameters for the API call
        offset = None
        limit = None

        # Perform the API call through the SDK function
        result = self.controller.create_bounced_emails(offset, limit)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Retrieve a list of invalid email addresses.
    def test_test_invalid_emails(self):
        # Parameters for the API call
        offset = None
        limit = None

        # Perform the API call through the SDK function
        result = self.controller.create_invalid_emails(offset, limit)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Retrieve a list of email addresses from the unsubscribe list.
    def test_test_list_unsubscribed_emails(self):
        # Parameters for the API call
        offset = None
        limit = None

        # Perform the API call through the SDK function
        result = self.controller.create_list_unsubscribed_emails(offset, limit)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

