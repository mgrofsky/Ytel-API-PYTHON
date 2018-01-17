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
        """Does a POST request to /dedicatedshortcode/sendsms.{ResponseType}.

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
                    method -- HttpActionEnum -- Specifies the HTTP method used
                        to request the required URL once the Short Code
                        message is sent.GET or POST
                    messagestatuscallback -- string -- URL that can be
                        requested to receive notification when Short Code
                        message was sent.

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
        _query_builder += '/dedicatedshortcode/sendsms.{ResponseType}'
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
        """Does a POST request to /dedicatedshortcode/getinboundsms.{ResponseType}.

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
                    page -- int -- The page count to retrieve from the total
                        results in the collection. Page indexing starts at 1.
                    pagesize -- int -- Number of individual resources listed
                        in the response per page
                    mfrom -- string -- Only list SMS messages sent from this
                        number
                    shortcode -- string -- Only list SMS messages sent to
                        Shortcode
                    datecreated -- string -- Only list SMS messages sent in
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
        _query_builder += '/dedicatedshortcode/getinboundsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'From': options.get('mfrom', None),
            'Shortcode': options.get('shortcode', None),
            'Datecreated': options.get('datecreated', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_dedicated_shortcode_assignment(self,
                                            options=dict()):
        """Does a POST request to /dedicatedshortcode/viewshortcode.{ResponseType}.

        Retrieve a single Short Code object by its shortcode assignment.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    shortcode -- string -- List of valid Dedicated Short Code
                        to your message360 account
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
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/dedicatedshortcode/viewshortcode.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Shortcode': options.get('shortcode', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def update_dedicated_short_code_assignment(self,
                                               options=dict()):
        """Does a POST request to /dedicatedshortcode/updateshortcode.{ResponseType}.

        Update a dedicated shortcode.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    shortcode -- string -- List of valid dedicated shortcode
                        to your message360 account.
                    response_type -- string -- Response type format xml or
                        json
                    friendly_name -- string -- User generated name of the
                        dedicated shortcode.
                    callback_method -- string -- Specifies the HTTP method
                        used to request the required StatusCallBackUrl once
                        call connects.
                    callback_url -- string -- URL that can be requested to
                        receive notification when call has ended. A set of
                        default parameters will be sent here once the call is
                        finished.
                    fallback_method -- string -- Specifies the HTTP method
                        used to request the required FallbackUrl once call
                        connects.
                    fallback_url -- string -- URL used if any errors occur
                        during execution of InboundXML or at initial request
                        of the required Url provided with the POST.

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
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/dedicatedshortcode/updateshortcode.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Shortcode': options.get('shortcode', None),
            'FriendlyName': options.get('friendly_name', None),
            'CallbackMethod': options.get('callback_method', None),
            'CallbackUrl': options.get('callback_url', None),
            'FallbackMethod': options.get('fallback_method', None),
            'FallbackUrl': options.get('fallback_url', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_short_code_assignment(self,
                                   options=dict()):
        """Does a POST request to /dedicatedshortcode/listshortcode.{ResponseType}.

        Retrieve a list of Short Code assignment associated with your
        message360 account.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    shortcode -- string -- Only list Short Code Assignment
                        sent from this Short Code
                    page -- string -- The page count to retrieve from the
                        total results in the collection. Page indexing starts
                        at 1.
                    pagesize -- string -- The count of objects to return per
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
        _query_builder += '/dedicatedshortcode/listshortcode.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Shortcode': options.get('shortcode', None),
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
