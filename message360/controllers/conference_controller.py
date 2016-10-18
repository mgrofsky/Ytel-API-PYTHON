# -*- coding: utf-8 -*-

"""
    message360.controllers.conference_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 10/18/2016
"""

from .base_controller import *



class ConferenceController(BaseController):

    """A Controller to access Endpoints in the message360 API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def create_view_participant(self,
                                conference_sid,
                                participant_sid,
                                response_type = 'json'):
        """Does a POST request to /conferences/viewparticipant.{ResponseType}.

        View Participant

        Args:
            conference_sid (string): unique conference sid
            participant_sid (string): TODO: type description here. Example: 
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
        if conference_sid == None:
            raise ValueError("Required parameter 'conference_sid' cannot be None.")
        elif participant_sid == None:
            raise ValueError("Required parameter 'participant_sid' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/conferences/viewparticipant.{ResponseType}'

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
            'ConferenceSid': conference_sid,
            'ParticipantSid': participant_sid
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



    def create_list_participant(self,
                                conference_sid,
                                page = None,
                                pagesize = None,
                                muted = None,
                                deaf = None,
                                response_type = 'json'):
        """Does a POST request to /conferences/listparticipant.{ResponseType}.

        List Participant

        Args:
            conference_sid (string): unique conference sid
            page (int, optional): page number
            pagesize (int, optional): TODO: type description here. Example: 
            muted (bool, optional): TODO: type description here. Example: 
            deaf (bool, optional): TODO: type description here. Example: 
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
        if conference_sid == None:
            raise ValueError("Required parameter 'conference_sid' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/conferences/listparticipant.{ResponseType}'

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
            'ConferenceSid': conference_sid,
            'Page': page,
            'Pagesize': pagesize,
            'Muted': muted,
            'Deaf': deaf
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



    def add_participant(self,
                        conferencesid,
                        participantnumber,
                        tocountrycode,
                        muted = None,
                        deaf = None,
                        response_type = 'json'):
        """Does a POST request to /conferences/addParticipant.{ResponseType}.

        Add Participant in conference 

        Args:
            conferencesid (string): Unique Conference Sid
            participantnumber (string): Particiant Number
            tocountrycode (int): TODO: type description here. Example: 
            muted (bool, optional): TODO: type description here. Example: 
            deaf (bool, optional): TODO: type description here. Example: 
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
        if conferencesid == None:
            raise ValueError("Required parameter 'conferencesid' cannot be None.")
        elif participantnumber == None:
            raise ValueError("Required parameter 'participantnumber' cannot be None.")
        elif tocountrycode == None:
            raise ValueError("Required parameter 'tocountrycode' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/conferences/addParticipant.{ResponseType}'

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
            'conferencesid': conferencesid,
            'participantnumber': participantnumber,
            'tocountrycode': tocountrycode,
            'muted': muted,
            'deaf': deaf
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



    def create_view_conference(self,
                               conferencesid,
                               response_type = 'json'):
        """Does a POST request to /conferences/viewconference.{ResponseType}.

        View Conference

        Args:
            conferencesid (string): The unique identifier of each conference
                resource
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
        if conferencesid == None:
            raise ValueError("Required parameter 'conferencesid' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/conferences/viewconference.{ResponseType}'

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
            'conferencesid': conferencesid
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



    def create_list_conference(self,
                               page = None,
                               page_size = None,
                               friendly_name = None,
                               status = None,
                               date_created = None,
                               date_updated = None,
                               response_type = 'json'):
        """Does a POST request to /conferences/listconference.{ResponseType}.

        List Conference

        Args:
            page (int, optional): Which page of the overall response will be
                returned. Zero indexed
            page_size (int, optional): Number of individual resources listed
                in the response per page
            friendly_name (string, optional): Only return conferences with the
                specified FriendlyName
            status (InterruptedCallStatusEnum, optional): TODO: type
                description here. Example: 
            date_created (string, optional): TODO: type description here.
                Example: 
            date_updated (string, optional): TODO: type description here.
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
        _query_builder += '/conferences/listconference.{ResponseType}'

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
            'FriendlyName': friendly_name,
            'Status': status,
            'DateCreated': date_created,
            'DateUpdated': date_updated
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


