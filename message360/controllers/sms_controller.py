# -*- coding: utf-8 -*-

"""
    message360.controllers.sms_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 12/12/2016
"""

from .base_controller import *

class SMSController(BaseController):

    """A Controller to access Endpoints in the message360 API."""
    

    def create_view_sms(self,
                        options=dict()):
        """Does a POST request to /sms/viewsms.{ResponseType}.

        View Particular SMS

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
        self.validate_parameters(messagesid = options.get("messagesid"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/sms/viewsms.{ResponseType}'
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

    def create_list_inbound_sms(self,
                                options=dict()):
        """Does a POST request to /sms/getInboundsms.{ResponseType}.

        List All Inbound SMS

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- int -- Which page of the overall response will be
                        returned. Zero indexed
                    pagesize -- string -- Number of individual resources
                        listed in the response per page
                    mfrom -- string -- From Number to Inbound SMS
                    to -- string -- To Number to get Inbound SMS
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
        _query_builder += '/sms/getInboundsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'from': options.get('mfrom', None),
            'to': options.get('to', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_list_sms(self,
                        options=dict()):
        """Does a POST request to /sms/listsms.{ResponseType}.

        List All SMS

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
        _query_builder += '/sms/listsms.{ResponseType}'
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

    def create_send_sms(self,
                        options=dict()):
        """Does a POST request to /sms/sendsms.{ResponseType}.

        Send an SMS from a message360 number

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    fromcountrycode -- int -- From Country Code
                    mfrom -- string -- SMS enabled Message360 number to send
                        this message from
                    tocountrycode -- int -- To country code
                    to -- string -- Number to send the SMS to
                    body -- string -- Text Message To Send
                    method -- HttpAction -- Specifies the HTTP method used to
                        request the required URL once SMS sent.
                    messagestatuscallback -- string -- URL that can be
                        requested to receive notification when SMS has Sent. A
                        set of default parameters will be sent here once the
                        SMS is finished.
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
        self.validate_parameters(fromcountrycode = options.get("fromcountrycode"),
                                 mfrom = options.get("mfrom"),
                                 tocountrycode = options.get("tocountrycode"),
                                 to = options.get("to"),
                                 body = options.get("body"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/sms/sendsms.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'fromcountrycode': options.get('fromcountrycode', None),
            'from': options.get('mfrom', None),
            'tocountrycode': options.get('tocountrycode', None),
            'to': options.get('to', None),
            'body': options.get('body', None),
            'method': options.get('method', None),
            'messagestatuscallback': options.get('messagestatuscallback', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body
