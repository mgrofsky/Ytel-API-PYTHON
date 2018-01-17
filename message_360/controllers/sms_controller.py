# -*- coding: utf-8 -*-

"""
    message_360.controllers.sms_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class SMSController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def send_sms(self,
                 options=dict()):
        """Does a POST request to /sms/sendsms.{ResponseType}.

        Send an SMS from a message360 number

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    mfrom -- string -- The 10-digit SMS-enabled message360
                        number (E.164 format) in which the message is sent.
                    to -- string -- The 10-digit phone number (E.164 format)
                        that will receive the message.
                    body -- string -- The body message that is to be sent in
                        the text.
                    response_type -- string -- Response type format xml or
                        json
                    method -- HttpActionEnum -- Specifies the HTTP method used
                        to request the required URL once SMS sent.
                    message_status_callback -- string -- URL that can be
                        requested to receive notification when SMS has Sent. A
                        set of default parameters will be sent here once the
                        SMS is finished.
                    smartsms -- bool -- Check's 'to' number can receive sms or
                        not using Carrier API, if wireless = true then text
                        sms is sent, else wireless = false then call is
                        recieved to end user with audible message.
                    delivery_status -- bool -- Delivery reports are a method
                        to tell your system if the message has arrived on the
                        destination phone.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(mfrom=options.get("mfrom"),
                                 to=options.get("to"),
                                 body=options.get("body"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/sms/sendsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'From': options.get('mfrom', None),
            'To': options.get('to', None),
            'Body': options.get('body', None),
            'Method': options.get('method', None),
            'MessageStatusCallback': options.get('message_status_callback', None),
            'Smartsms': options.get('smartsms', None),
            'DeliveryStatus': options.get('delivery_status', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_sms(self,
                 options=dict()):
        """Does a POST request to /sms/viewsms.{ResponseType}.

        Retrieve a single SMS message object by its SmsSid.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    message_sid -- string -- The unique identifier for a sms
                        message.
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
        _query_builder += '/sms/viewsms.{ResponseType}'
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

    def list_sms(self,
                 options=dict()):
        """Does a POST request to /sms/listsms.{ResponseType}.

        Retrieve a list of Outbound SMS message objects.

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
                    page_size -- int -- Number of individual resources listed
                        in the response per page
                    mfrom -- string -- Filter SMS message objects from this
                        valid 10-digit phone number (E.164 format).
                    to -- string -- Filter SMS message objects to this valid
                        10-digit phone number (E.164 format).
                    date_sent -- string -- Only list SMS messages sent in the
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
        _query_builder += '/sms/listsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Page': options.get('page', None),
            'PageSize': options.get('page_size', None),
            'From': options.get('mfrom', None),
            'To': options.get('to', None),
            'DateSent': options.get('date_sent', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_inbound_sms(self,
                         options=dict()):
        """Does a POST request to /sms/getinboundsms.{ResponseType}.

        Retrieve a list of Inbound SMS message objects.

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
                    page_size -- int -- The count of objects to return per
                        page.
                    mfrom -- string -- Filter SMS message objects from this
                        valid 10-digit phone number (E.164 format).
                    to -- string -- Filter SMS message objects to this valid
                        10-digit phone number (E.164 format).
                    date_sent -- string -- Filter sms message objects by this
                        date.

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
        _query_builder += '/sms/getinboundsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Page': options.get('page', None),
            'PageSize': options.get('page_size', None),
            'From': options.get('mfrom', None),
            'To': options.get('to', None),
            'DateSent': options.get('date_sent', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_detail_sms(self,
                        options=dict()):
        """Does a POST request to /sms/viewdetailsms.{ResponseType}.

        Retrieve a single SMS message object with details by its SmsSid.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    message_sid -- string -- The unique identifier for a sms
                        message.
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
        _query_builder += '/sms/viewdetailsms.{ResponseType}'
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
