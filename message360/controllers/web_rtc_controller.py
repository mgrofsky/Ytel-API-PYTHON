# -*- coding: utf-8 -*-

"""
    message360.controllers.web_rtc_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 12/12/2016
"""

from .base_controller import *

class WebRTCController(BaseController):

    """A Controller to access Endpoints in the message360 API."""
    

    def create_check_funds(self,
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
        self.validate_parameters(account_sid = options.get("account_sid"),
                                 auth_token = options.get("auth_token"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/webrtc/checkFunds.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'account_sid': options.get('account_sid', None),
            'auth_token': options.get('auth_token', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_authenticate_number(self,
                                   options=dict()):
        """Does a POST request to /webrtc/authenticateNumber.json.

        Authenticate a message360 number for use

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- Phone number to authenticate for
                        use
                    account_sid -- string -- Your message360 Account SID
                    auth_token -- string -- Your message360 token

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(phone_number = options.get("phone_number"),
                                 account_sid = options.get("account_sid"),
                                 auth_token = options.get("auth_token"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/webrtc/authenticateNumber.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'phone_number': options.get('phone_number', None),
            'account_sid': options.get('account_sid', None),
            'auth_token': options.get('auth_token', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_token(self,
                     options=dict()):
        """Does a POST request to /webrtc/createToken.json.

        message360 webrtc

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
        self.validate_parameters(account_sid = options.get("account_sid"),
                                 auth_token = options.get("auth_token"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/webrtc/createToken.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'account_sid': options.get('account_sid', None),
            'auth_token': options.get('auth_token', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body
