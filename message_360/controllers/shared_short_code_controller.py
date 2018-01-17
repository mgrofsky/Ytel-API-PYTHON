# -*- coding: utf-8 -*-

"""
    message_360.controllers.shared_short_code_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class SharedShortCodeController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def view_template(self,
                      options=dict()):
        """Does a POST request to /template/view.{ResponseType}.

        View a Shared ShortCode Template

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    template_id -- uuid|string -- The unique identifier for a
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
        self.validate_parameters(template_id=options.get("template_id"),
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
            'TemplateId': options.get('template_id', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_shared_shortcodes(self,
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
        self.validate_parameters(messagesid=options.get("messagesid"),
                                 response_type=options.get("response_type"))

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

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_outbound_shared_shortcodes(self,
                                        options=dict()):
        """Does a POST request to /shortcode/listsms.{ResponseType}.

        List ShortCode Messages

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
                    shortcode -- string -- Only list messages sent from this
                        Short Code
                    to -- string -- Only list messages sent to this number
                    datesent -- string -- Only list SMS messages sent in the
                        specified date range

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
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'Shortcode': options.get('shortcode', None),
            'to': options.get('to', None),
            'datesent': options.get('datesent', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_inbound_shared_shortcodes(self,
                                       options=dict()):
        """Does a POST request to /shortcode/getinboundsms.{ResponseType}.

        List All Inbound ShortCode

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
                    mfrom -- string -- From Number to Inbound ShortCode
                    shortcode -- string -- Only list messages sent to this
                        Short Code
                    datecreated -- string -- Only list messages sent with the
                        specified date

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
        _query_parameters = {
            'Datecreated': options.get('datecreated', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'from': options.get('mfrom', None),
            'Shortcode': options.get('shortcode', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def send_shared_shortcode(self,
                              options=dict()):
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
                    to -- string -- A valid 10-digit number that should
                        receive the message
                    templateid -- uuid|string -- The unique identifier for the
                        template used for the message
                    response_type -- string -- Response type format xml or
                        json
                    data -- string -- format of your data, example:
                        {companyname}:test,{otpcode}:1234
                    method -- HttpActionEnum -- Specifies the HTTP method used
                        to request the required URL once the Short Code
                        message is sent.
                    message_status_callback -- string -- URL that can be
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
                                 templateid=options.get("templateid"),
                                 response_type=options.get("response_type"),
                                 data=options.get("data"))

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
            'to': options.get('to', None),
            'templateid': options.get('templateid', None),
            'data': options.get('data', None),
            'Method': options.get('method', None),
            'MessageStatusCallback': options.get('message_status_callback', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_templates(self,
                       options=dict()):
        """Does a POST request to /template/lists.{ResponseType}.

        List Shortcode Templates by Type

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    mtype -- string -- The type (category) of template Valid
                        values: marketing, authorization
                    page -- int -- The page count to retrieve from the total
                        results in the collection. Page indexing starts at 1.
                    pagesize -- int -- The count of objects to return per
                        page.
                    shortcode -- string -- Only list templates of type

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
        _query_builder += '/template/lists.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'type': options.get('mtype', None),
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'Shortcode': options.get('shortcode', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_keyword(self,
                     options=dict()):
        """Does a POST request to /keyword/view.{ResponseType}.

        View a set of properties for a single keyword.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    keywordid -- string -- The unique identifier of each
                        keyword
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
        self.validate_parameters(keywordid=options.get("keywordid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/keyword/view.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Keywordid': options.get('keywordid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_keyword(self,
                     options=dict()):
        """Does a POST request to /keyword/lists.{ResponseType}.

        Retrieve a list of keywords associated with your message360 account.

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
                    keyword -- string -- Only list keywords of keyword
                    shortcode -- int -- Only list keywords of shortcode

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
        _query_builder += '/keyword/lists.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'Keyword': options.get('keyword', None),
            'Shortcode': options.get('shortcode', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_assignement(self,
                         options=dict()):
        """Does a POST request to /shortcode/viewshortcode.{ResponseType}.

        The response returned here contains all resource properties associated
        with the given Shortcode.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    shortcode -- string -- List of valid Shortcode to your
                        message360 account
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
        _query_builder += '/shortcode/viewshortcode.{ResponseType}'
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

    def list_assignment(self,
                        options=dict()):
        """Does a POST request to /shortcode/listshortcode.{ResponseType}.

        Retrieve a list of shortcode assignment associated with your
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
                    shortcode -- string -- Only list keywords of shortcode

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
        _query_builder += '/shortcode/listshortcode.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_parameters = {
            'Shortcode': options.get('shortcode', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
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

    def update_assignment(self,
                          options=dict()):
        """Does a POST request to /shortcode/updateshortcode.{ResponseType}.

        TODO: type endpoint description here.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    shortcode -- string -- List of valid shortcode to your
                        message360 account
                    response_type -- string -- Response type format xml or
                        json
                    friendly_name -- string -- User generated name of the
                        shortcode
                    callback_url -- string -- URL that can be requested to
                        receive notification when call has ended. A set of
                        default parameters will be sent here once the call is
                        finished.
                    callback_method -- HttpActionEnum -- Specifies the HTTP
                        method used to request the required StatusCallBackUrl
                        once call connects.
                    fallback_url -- string -- URL used if any errors occur
                        during execution of InboundXML or at initial request
                        of the required Url provided with the POST.
                    fallback_url_method -- HttpActionEnum -- Specifies the
                        HTTP method used to request the required FallbackUrl
                        once call connects.

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
        _query_builder += '/shortcode/updateshortcode.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Shortcode': options.get('shortcode', None),
            'FriendlyName': options.get('friendly_name', None),
            'CallbackUrl': options.get('callback_url', None),
            'CallbackMethod': options.get('callback_method', None),
            'FallbackUrl': options.get('fallback_url', None),
            'FallbackUrlMethod': options.get('fallback_url_method', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
