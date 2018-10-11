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


class AreaMailControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(AreaMailControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.area_mail

    # Retrieve a list of AreaMail objects.
    def test_test_list_area_mails(self):
        # Parameters for the API call
        page = None
        pagesize = None
        areamailsid = None
        date_created = None

        # Perform the API call through the SDK function
        result = self.controller.create_list_area_mails(page, pagesize, areamailsid, date_created)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

