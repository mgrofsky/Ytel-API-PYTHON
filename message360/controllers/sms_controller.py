# -*- coding: utf-8 -*-

"""
    message360.controllers.sms_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 10/21/2016
"""

from .base_controller import *



class SMSController(BaseController):

    """A Controller to access Endpoints in the message360 API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def create_send_sms(self,
                        fromcountrycode,
                        mfrom,
                        tocountrycode,
                        to,
                        body,
                        method = None,
                        messagestatuscallback = None,
                        response_type = 'json'):
        """Does a POST request to /sms/sendsms.{ResponseType}.

        Send an SMS from a message360 number

        Args:
            fromcountrycode (int): From Country Code
            mfrom (string): SMS enabled Message360 number to send this message
                from
            tocountrycode (int): To country code
            to (string): Number to send the SMS to
            body (string): Text Message To Send
            method (HttpMethod, optional): Specifies the HTTP method used to
                request the required URL once SMS sent.
            messagestatuscallback (string, optional): URL that can be
                requested to receive notification when SMS has Sent. A set of
                default parameters will be sent here once the SMS is
                finished.
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
        if fromcountrycode == None:
            raise ValueError("Required parameter 'fromcountrycode' cannot be None.")
        elif mfrom == None:
            raise ValueError("Required parameter 'mfrom' cannot be None.")
        elif tocountrycode == None:
            raise ValueError("Required parameter 'tocountrycode' cannot be None.")
        elif to == None:
            raise ValueError("Required parameter 'to' cannot be None.")
        elif body == None:
            raise ValueError("Required parameter 'body' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/sms/sendsms.{ResponseType}'

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
            'fromcountrycode': fromcountrycode,
            'from': mfrom,
            'tocountrycode': tocountrycode,
            'to': to,
            'body': body,
            'method': method,
            'messagestatuscallback': messagestatuscallback
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



    def create_view_sms(self,
                        messagesid,
                        response_type = 'json'):
        """Does a POST request to /sms/viewsms.{ResponseType}.

        View Particular SMS

        Args:
            messagesid (string): Message sid
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
        if messagesid == None:
            raise ValueError("Required parameter 'messagesid' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/sms/viewsms.{ResponseType}'

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
            'messagesid': messagesid
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



    def create_list_sms(self,
                        page = None,
                        pagesize = None,
                        mfrom = None,
                        to = None,
                        datesent = None,
                        response_type = 'json'):
        """Does a POST request to /sms/listsms.{ResponseType}.

        List All SMS

        Args:
            page (int, optional): Which page of the overall response will be
                returned. Zero indexed
            pagesize (int, optional): Number of individual resources listed in
                the response per page
            mfrom (string, optional): Messages sent from this number
            to (string, optional): Messages sent to this number
            datesent (string, optional): Only list SMS messages sent in the
                specified date range
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
        _query_builder += '/sms/listsms.{ResponseType}'

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
            'page': page,
            'pagesize': pagesize,
            'from': mfrom,
            'to': to,
            'datesent': datesent
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



    def create_list_inbound_sms(self,
                                page = None,
                                pagesize = None,
                                mfrom = None,
                                to = None,
                                response_type = 'json'):
        """Does a POST request to /sms/getInboundsms.{ResponseType}.

        List All Inbound SMS

        Args:
            page (int, optional): Which page of the overall response will be
                returned. Zero indexed
            pagesize (string, optional): Number of individual resources listed
                in the response per page
            mfrom (string, optional): From Number to Inbound SMS
            to (string, optional): To Number to get Inbound SMS
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
        _query_builder += '/sms/getInboundsms.{ResponseType}'

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
            'page': page,
            'pagesize': pagesize,
            'from': mfrom,
            'to': to
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


