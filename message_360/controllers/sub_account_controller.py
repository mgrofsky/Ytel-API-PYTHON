# -*- coding: utf-8 -*-

"""
    message_360.controllers.sub_account_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class SubAccountController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def delete_sub_account(self,
                           options=dict()):
        """Does a POST request to /user/deletesubaccount.{ResponseType}.

        Delete sub account or merge numbers into parent

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    sub_account_sid -- string -- The SubaccountSid to be
                        deleted
                    merge_number -- MergeNumberStatusEnum -- 0 to delete or 1
                        to merge numbers to parent account.
                    response_type -- string -- Response type format xml or
                        json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(sub_account_sid=options.get("sub_account_sid"),
                                 merge_number=options.get("merge_number"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/user/deletesubaccount.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'SubAccountSID': options.get('sub_account_sid', None),
            'MergeNumber': options.get('merge_number', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def suspend_sub_account(self,
                            options=dict()):
        """Does a POST request to /user/subaccountactivation.{ResponseType}.

        Suspend or unsuspend

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    sub_account_sid -- string -- The SubaccountSid to be
                        activated or suspended
                    activate -- ActivateStatusEnum -- 0 to suspend or 1 to
                        activate
                    response_type -- string -- TODO: type description here.
                        Example: json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(sub_account_sid=options.get("sub_account_sid"),
                                 activate=options.get("activate"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/user/subaccountactivation.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'SubAccountSID': options.get('sub_account_sid', None),
            'Activate': options.get('activate', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_sub_account(self,
                           options=dict()):
        """Does a POST request to /user/createsubaccount.{ResponseType}.

        Create a sub user account under the parent account

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    first_name -- string -- Sub account user first name
                    last_name -- string -- sub account user last name
                    email -- string -- Sub account email address
                    friendly_name -- string -- Descriptive name of the sub
                        account
                    password -- string -- The password of the sub account. 
                        Please make sure to make as password that is at least
                        8 characters long, contain a symbol, uppercase and a
                        number.
                    response_type -- string -- Response type format xml or
                        json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(first_name=options.get("first_name"),
                                 last_name=options.get("last_name"),
                                 email=options.get("email"),
                                 friendly_name=options.get("friendly_name"),
                                 password=options.get("password"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/user/createsubaccount.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'FirstName': options.get('first_name', None),
            'LastName': options.get('last_name', None),
            'Email': options.get('email', None),
            'FriendlyName': options.get('friendly_name', None),
            'Password': options.get('password', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
