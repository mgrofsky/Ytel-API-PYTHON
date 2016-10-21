# -*- coding: utf-8 -*-

"""
    message360.controllers.phone_number_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 10/21/2016
"""

from .base_controller import *



class PhoneNumberController(BaseController):

    """A Controller to access Endpoints in the message360 API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def create_available_phone_number(self,
                                      number_type,
                                      area_code,
                                      page_size = None,
                                      response_type = 'json'):
        """Does a POST request to /incomingphone/availablenumber.{ResponseType}.

        Available Phone Number

        Args:
            number_type (string): Number type either SMS,Voice or all
            area_code (string): Phone Number Area Code
            page_size (int, optional): Page Size
            response_type (string, optional): Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if number_type == None:
            raise ValueError("Required parameter 'number_type' cannot be None.")
        elif area_code == None:
            raise ValueError("Required parameter 'area_code' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/availablenumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': response_type
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'message360-api'
        }

        # Prepare form parameters
        _form_parameters = {
            'NumberType': number_type,
            'AreaCode': area_code,
            'PageSize': page_size
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body



    def create_list_number(self,
                           page = None,
                           page_size = None,
                           number_type = None,
                           friendly_name = None,
                           response_type = 'json'):
        """Does a POST request to /incomingphone/listnumber.{ResponseType}.

        List Account's Phone number details

        Args:
            page (int, optional): Which page of the overall response will be
                returned. Zero indexed
            page_size (int, optional): Number of individual resources listed
                in the response per page
            number_type (string, optional): TODO: type description here.
                Example: 
            friendly_name (string, optional): TODO: type description here.
                Example: 
            response_type (string, optional): Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/listnumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': response_type
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'message360-api'
        }

        # Prepare form parameters
        _form_parameters = {
            'Page': page,
            'PageSize': page_size,
            'NumberType': number_type,
            'FriendlyName': friendly_name
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body



    def create_release_number(self,
                              phone_number,
                              response_type = 'json'):
        """Does a POST request to /incomingphone/releasenumber.{ResponseType}.

        Release number from account

        Args:
            phone_number (string): Phone number to be relase
            response_type (string, optional): Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if phone_number == None:
            raise ValueError("Required parameter 'phone_number' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/releasenumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': response_type
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'message360-api'
        }

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': phone_number
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body



    def create_buy_number(self,
                          phone_number,
                          response_type = 'json'):
        """Does a POST request to /incomingphone/buynumber.{ResponseType}.

        Buy Phone Number 

        Args:
            phone_number (string): Phone number to be purchase
            response_type (string, optional): Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if phone_number == None:
            raise ValueError("Required parameter 'phone_number' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/buynumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': response_type
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'message360-api'
        }

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': phone_number
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body



    def create_view_number_details(self,
                                   phone_number,
                                   response_type = 'json'):
        """Does a POST request to /incomingphone/viewnumber.{ResponseType}.

        Get Phone Number Details

        Args:
            phone_number (string): Get Phone number Detail
            response_type (string, optional): Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if phone_number == None:
            raise ValueError("Required parameter 'phone_number' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/viewnumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': response_type
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'message360-api'
        }

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': phone_number
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body



    def update_phone_number(self,
                            phone_number,
                            friendly_name = None,
                            voice_url = None,
                            voice_method = None,
                            voice_fallback_url = None,
                            voice_fallback_method = None,
                            hangup_callback = None,
                            hangup_callback_method = None,
                            heartbeat_url = None,
                            heartbeat_method = None,
                            sms_url = None,
                            sms_method = None,
                            sms_fallback_url = None,
                            sms_fallback_method = None,
                            response_type = 'json'):
        """Does a POST request to /incomingphone/updatenumber.{ResponseType}.

        Update Phone Number Details

        Args:
            phone_number (string): TODO: type description here. Example: 
            friendly_name (string, optional): TODO: type description here.
                Example: 
            voice_url (string, optional): URL requested once the call
                connects
            voice_method (HttpMethod, optional): TODO: type description here.
                Example: 
            voice_fallback_url (string, optional): URL requested if the voice
                URL is not available
            voice_fallback_method (HttpMethod, optional): TODO: type
                description here. Example: 
            hangup_callback (string, optional): TODO: type description here.
                Example: 
            hangup_callback_method (HttpMethod, optional): TODO: type
                description here. Example: 
            heartbeat_url (string, optional): URL requested once the call
                connects
            heartbeat_method (HttpMethod, optional): URL that can be requested
                every 60 seconds during the call to notify of elapsed time
            sms_url (string, optional): URL requested when an SMS is received
            sms_method (HttpMethod, optional): TODO: type description here.
                Example: 
            sms_fallback_url (string, optional): URL requested once the call
                connects
            sms_fallback_method (HttpMethod, optional): URL requested if the
                sms URL is not available
            response_type (string, optional): Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if phone_number == None:
            raise ValueError("Required parameter 'phone_number' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/updatenumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': response_type
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'message360-api'
        }

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'VoiceUrl': voice_url,
            'VoiceMethod': voice_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceFallbackMethod': voice_fallback_method,
            'HangupCallback': hangup_callback,
            'HangupCallbackMethod': hangup_callback_method,
            'HeartbeatUrl': heartbeat_url,
            'HeartbeatMethod': heartbeat_method,
            'SmsUrl': sms_url,
            'SmsMethod': sms_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsFallbackMethod': sms_fallback_method
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _response.raw_body


