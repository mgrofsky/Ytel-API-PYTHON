# -*- coding: utf-8 -*-

"""
    message360.controllers.short_code_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class ShortCodeController(BaseController):

    """A Controller to access Endpoints in the message360 API."""


    def create_view_template(self,
                             options=dict()):
        """Does a POST request to /template/view.{ResponseType}.

        View a Shared ShortCode Template

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    templateid -- uuid|string -- The unique identifier for a
                        template object
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
        self.validate_parameters(templateid=options.get("templateid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/template/view.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'templateid': options.get('templateid', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_send_short_code(self,
                               options=dict(),
                               _optional_form_parameters=None):
        """Does a POST request to /shortcode/sendsms.{ResponseType}.

        Send an SMS from a message360 ShortCode

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    shortcode -- string -- The Short Code number that is the
                        sender of this message
                    tocountrycode -- string -- The country code for sending
                        this message
                    to -- string -- A valid 10-digit number that should
                        receive the message+
                    templateid -- uuid|string -- The unique identifier for the
                        template used for the message
                    method -- string -- Specifies the HTTP method used to
                        request the required URL once the Short Code message
                        is sent.
                    message_status_callback -- string -- URL that can be
                        requested to receive notification when Short Code
                        message was sent.
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
        self.validate_parameters(shortcode=options.get("shortcode"),
                                 tocountrycode=options.get("tocountrycode"),
                                 to=options.get("to"),
                                 templateid=options.get("templateid"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/shortcode/sendsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'shortcode': options.get('shortcode', None),
            'tocountrycode': options.get('tocountrycode', None),
            'to': options.get('to', None),
            'templateid': options.get('templateid', None),
            'Method': options.get('method', None),
            'MessageStatusCallback': options.get('message_status_callback', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)
        if _form_parameters != None and _optional_form_parameters != None:
            _form_parameters.update(APIHelper.form_encode_parameters(_optional_form_parameters))

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_list_inbound_short_code(self,
                                       options=dict()):
        """Does a POST request to /shortcode/getinboundsms.{ResponseType}.

        List All Inbound ShortCode

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- int -- Which page of the overall response will be
                        returned. Zero indexed
                    pagesize -- int -- Number of individual resources listed
                        in the response per page
                    mfrom -- string -- From Number to Inbound ShortCode
                    shortcode -- string -- Only list messages sent to this
                        Short Code
                    date_received -- string -- Only list messages sent with
                        the specified date
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

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/shortcode/getinboundsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)
        _query_parameters = {
            'DateReceived': options.get('date_received', None)
        }

        # Prepare form parameters
        _form_parameters = {
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'from': options.get('mfrom', None),
            'Shortcode': options.get('shortcode', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, query_parameters=_query_parameters, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_list_short_code(self,
                               options=dict()):
        """Does a POST request to /shortcode/listsms.{ResponseType}.

        List ShortCode Messages

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- int -- Which page of the overall response will be
                        returned. Zero indexed
                    pagesize -- int -- Number of individual resources listed
                        in the response per page
                    mfrom -- string -- Messages sent from this number
                    to -- string -- Messages sent to this number
                    datesent -- string -- Only list SMS messages sent in the
                        specified date range
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

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/shortcode/listsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'from': options.get('mfrom', None),
            'to': options.get('to', None),
            'datesent': options.get('datesent', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_list_templates(self,
                              options=dict()):
        """Does a POST request to /template/lists.{ResponseType}.

        List Shortcode Templates by Type

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    mtype -- string -- The type (category) of template Valid
                        values: marketing, authorization
                    page -- int -- The page count to retrieve from the total
                        results in the collection. Page indexing starts at 1.
                    pagesize -- int -- The count of objects to return per
                        page.
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

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/template/lists.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'type': options.get('mtype', None),
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_view_short_code(self,
                               options=dict()):
        """Does a POST request to /shortcode/viewsms.{ResponseType}.

        View a ShortCode Message

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    messagesid -- string -- Message sid
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
        self.validate_parameters(messagesid=options.get("messagesid"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/shortcode/viewsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'messagesid': options.get('messagesid', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
