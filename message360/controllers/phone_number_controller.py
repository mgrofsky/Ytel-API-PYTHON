# -*- coding: utf-8 -*-

"""
    message360.controllers.phone_number_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 11/21/2016
"""

from .base_controller import *

class PhoneNumberController(BaseController):

    """A Controller to access Endpoints in the message360 API."""

    def create_available_phone_number(self,
                                      options=dict()):
        """Does a POST request to /incomingphone/availablenumber.{ResponseType}.

        Available Phone Number

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    number_type -- string -- Number type either SMS,Voice or
                        all
                    area_code -- string -- Phone Number Area Code
                    page_size -- int -- Page Size
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(number_type = options.get("number_type"),
                                 area_code = options.get("area_code"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/availablenumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'NumberType': options.get('number_type', None),
            'AreaCode': options.get('area_code', None),
            'PageSize': options.get('page_size', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_list_number(self,
                           options=dict()):
        """Does a POST request to /incomingphone/listnumber.{ResponseType}.

        List Account's Phone number details

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- int -- Which page of the overall response will be
                        returned. Zero indexed
                    page_size -- int -- Number of individual resources listed
                        in the response per page
                    number_type -- string -- TODO: type description here.
                        Example: 
                    friendly_name -- string -- TODO: type description here.
                        Example: 
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/listnumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Page': options.get('page', None),
            'PageSize': options.get('page_size', None),
            'NumberType': options.get('number_type', None),
            'FriendlyName': options.get('friendly_name', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_view_number_details(self,
                                   options=dict()):
        """Does a POST request to /incomingphone/viewnumber.{ResponseType}.

        Get Phone Number Details

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- Get Phone number Detail
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(phone_number = options.get("phone_number"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/viewnumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': options.get('phone_number', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_release_number(self,
                              options=dict()):
        """Does a POST request to /incomingphone/releasenumber.{ResponseType}.

        Release number from account

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- Phone number to be relase
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(phone_number = options.get("phone_number"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/releasenumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': options.get('phone_number', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_buy_number(self,
                          options=dict()):
        """Does a POST request to /incomingphone/buynumber.{ResponseType}.

        Buy Phone Number 

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- Phone number to be purchase
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(phone_number = options.get("phone_number"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/buynumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': options.get('phone_number', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def update_phone_number(self,
                            options=dict()):
        """Does a POST request to /incomingphone/updatenumber.{ResponseType}.

        Update Phone Number Details

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- TODO: type description here.
                        Example: 
                    friendly_name -- string -- TODO: type description here.
                        Example: 
                    voice_url -- string -- URL requested once the call
                        connects
                    voice_method -- HttpAction -- TODO: type description here.
                        Example: 
                    voice_fallback_url -- string -- URL requested if the voice
                        URL is not available
                    voice_fallback_method -- HttpAction -- TODO: type
                        description here. Example: 
                    hangup_callback -- string -- TODO: type description here.
                        Example: 
                    hangup_callback_method -- HttpAction -- TODO: type
                        description here. Example: 
                    heartbeat_url -- string -- URL requested once the call
                        connects
                    heartbeat_method -- HttpAction -- URL that can be
                        requested every 60 seconds during the call to notify
                        of elapsed time
                    sms_url -- string -- URL requested when an SMS is
                        received
                    sms_method -- HttpAction -- TODO: type description here.
                        Example: 
                    sms_fallback_url -- string -- URL requested once the call
                        connects
                    sms_fallback_method -- HttpAction -- URL requested if the
                        sms URL is not available
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(phone_number = options.get("phone_number"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/incomingphone/updatenumber.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': options.get('phone_number', None),
            'FriendlyName': options.get('friendly_name', None),
            'VoiceUrl': options.get('voice_url', None),
            'VoiceMethod': options.get('voice_method', None),
            'VoiceFallbackUrl': options.get('voice_fallback_url', None),
            'VoiceFallbackMethod': options.get('voice_fallback_method', None),
            'HangupCallback': options.get('hangup_callback', None),
            'HangupCallbackMethod': options.get('hangup_callback_method', None),
            'HeartbeatUrl': options.get('heartbeat_url', None),
            'HeartbeatMethod': options.get('heartbeat_method', None),
            'SmsUrl': options.get('sms_url', None),
            'SmsMethod': options.get('sms_method', None),
            'SmsFallbackUrl': options.get('sms_fallback_url', None),
            'SmsFallbackMethod': options.get('sms_fallback_method', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body


