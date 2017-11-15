# -*- coding: utf-8 -*-

"""
    message_360.controllers.short_code_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class ShortCodeController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def send_dedicated_shortcode(self,
                                 options=dict()):
        """Does a POST request to /shortcode/senddedicatedsms.{ResponseType}.

        TODO: type endpoint description here.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    shortcode -- int -- Your dedicated shortcode
                    to -- float -- The number to send your SMS to
                    body -- string -- The body of your message
                    response_type -- string -- Response type format xml or
                        json
                    method -- HttpActionEnum -- Callback status method, POST
                        or GET
                    messagestatuscallback -- string -- Callback url for SMS
                        status

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(shortcode=options.get("shortcode"),
                                 to=options.get("to"),
                                 body=options.get("body"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/shortcode/senddedicatedsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'shortcode': options.get('shortcode', None),
            'to': options.get('to', None),
            'body': options.get('body', None),
            'method': options.get('method', None),
            'messagestatuscallback': options.get('messagestatuscallback', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_shortcode(self,
                       options=dict()):
        """Does a POST request to /shortcode/viewsms..{ResponseType}.

        View a single Sms Short Code message.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    message_sid -- string -- The unique identifier for the sms
                        resource
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
        self.validate_parameters(message_sid=options.get("message_sid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/shortcode/viewsms..{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'MessageSid': options.get('message_sid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_shortcode(self,
                       options=dict()):
        """Does a POST request to /shortcode/listsms.{ResponseType}.

        Retrieve a list of Short Code message objects.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    shortcode -- string -- Only list messages sent from this
                        Short Code
                    to -- string -- Only list messages sent to this number
                    date_sent -- string -- Only list messages sent with the
                        specified date
                    page -- int -- The page count to retrieve from the total
                        results in the collection. Page indexing starts at 1.
                    page_size -- int -- The count of objects to return per
                        page.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/shortcode/listsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Shortcode': options.get('shortcode', None),
            'To': options.get('to', None),
            'DateSent': options.get('date_sent', None),
            'Page': options.get('page', None),
            'PageSize': options.get('page_size', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_inbound_shortcode(self,
                               options=dict()):
        """Does a POST request to /shortcode/getinboundsms.{ResponseType}.

        Retrive a list of inbound Sms Short Code messages associated with your
        message360 account.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    page -- int -- Which page of the overall response will be
                        returned. Zero indexed
                    page_size -- int -- Number of individual resources listed
                        in the response per page
                    mfrom -- string -- Only list SMS messages sent from this
                        number
                    shortcode -- string -- Only list SMS messages sent to
                        Shortcode
                    date_received -- string -- Only list SMS messages sent in
                        the specified date MAKE REQUEST

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/shortcode/getinboundsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Page': options.get('page', None),
            'PageSize': options.get('page_size', None),
            'From': options.get('mfrom', None),
            'Shortcode': options.get('shortcode', None),
            'DateReceived': options.get('date_received', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
