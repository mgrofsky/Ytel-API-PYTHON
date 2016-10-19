# -*- coding: utf-8 -*-

"""
    message360.controllers.usage_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 10/18/2016
"""

from .base_controller import *



class UsageController(BaseController):

    """A Controller to access Endpoints in the message360 API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def create_list_usage(self,
                          product_code,
                          start_date,
                          end_date,
                          response_type = 'json'):
        """Does a POST request to /usage/listusage.{ResponseType}.

        Get all usage 

        Args:
            product_code (string): Product Code
            start_date (string): Start Usage Date
            end_date (string): End Usage Date
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
        if product_code == None:
            raise ValueError("Required parameter 'product_code' cannot be None.")
        elif start_date == None:
            raise ValueError("Required parameter 'start_date' cannot be None.")
        elif end_date == None:
            raise ValueError("Required parameter 'end_date' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/usage/listusage.{ResponseType}'

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
            'ProductCode': product_code,
            'startDate': start_date,
            'endDate': end_date
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


