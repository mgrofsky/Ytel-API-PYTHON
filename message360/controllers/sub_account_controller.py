# -*- coding: utf-8 -*-

"""
    message360.controllers.sub_account_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 12/02/2016
"""

from .base_controller import *

class SubAccountController(BaseController):

    """A Controller to access Endpoints in the message360 API."""

    def create_sub_account(self,
                           options=dict()):
        """Does a POST request to /user/createsubaccount.{ResponseType}.

        Create Sub account

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    firstname -- string -- TODO: type description here.
                        Example: 
                    lastname -- string -- TODO: type description here.
                        Example: 
                    email -- string -- TODO: type description here. Example: 
                    response_type -- string -- ResponseType Format either json
                        or xml

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(firstname = options.get("firstname"),
                                 lastname = options.get("lastname"),
                                 email = options.get("email"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/user/createsubaccount.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'firstname': options.get('firstname', None),
            'lastname': options.get('lastname', None),
            'email': options.get('email', None)
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



    def create_suspend_sub_account(self,
                                   options=dict()):
        """Does a POST request to /user/subaccountactivation.{ResponseType}.

        Suspend or unsuspend

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    subaccountsid -- string -- TODO: type description here.
                        Example: 
                    activate -- ActivateStatus -- TODO: type description here.
                        Example: 
                    response_type -- string -- TODO: type description here.
                        Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(subaccountsid = options.get("subaccountsid"),
                                 activate = options.get("activate"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/user/subaccountactivation.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'subaccountsid': options.get('subaccountsid', None),
            'activate': options.get('activate', None)
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



    def create_delete_merge_sub_account(self,
                                        options=dict()):
        """Does a POST request to /user/deletesubaccount.{ResponseType}.

        Delete or Merge Sub account

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    subaccountsid -- string -- TODO: type description here.
                        Example: 
                    mergenumber -- MergeNumberStatus -- TODO: type description
                        here. Example: 
                    response_type -- string -- Response type format either
                        json or xml

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(subaccountsid = options.get("subaccountsid"),
                                 mergenumber = options.get("mergenumber"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/user/deletesubaccount.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'subaccountsid': options.get('subaccountsid', None),
            'mergenumber': options.get('mergenumber', None)
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


