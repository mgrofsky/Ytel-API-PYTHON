# -*- coding: utf-8 -*-

"""
    message_360.controllers.web_rtc_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class WebRTCController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def check_funds(self,
                    options=dict()):
        """Does a POST request to /webrtc/checkFunds.json.

        TODO: type endpoint description here.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    account_sid -- string -- Your message360 Account SID
                    auth_token -- string -- Your message360 Token

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(account_sid=options.get("account_sid"),
                                 auth_token=options.get("auth_token"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/webrtc/checkFunds.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'account_sid': options.get('account_sid', None),
            'auth_token': options.get('auth_token', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_token(self,
                     options=dict()):
        """Does a POST request to /webrtc/agentLogin.json.

        message360 webrtc

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    account_sid -- string -- Your message360 Account SID
                    auth_token -- string -- Your message360 Token
                    username -- string -- WebRTC username authentication
                    password -- string -- WebRTC password authentication

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(account_sid=options.get("account_sid"),
                                 auth_token=options.get("auth_token"),
                                 username=options.get("username"),
                                 password=options.get("password"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/webrtc/agentLogin.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'account_sid': options.get('account_sid', None),
            'auth_token': options.get('auth_token', None),
            'username': options.get('username', None),
            'password': options.get('password', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
