# -*- coding: utf-8 -*-

"""
    message_360.controllers.phone_number_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class PhoneNumberController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def available_phone_number(self,
                               options=dict()):
        """Does a POST request to /incomingphone/availablenumber.{ResponseType}.

        Retrieve a list of available phone numbers that can be purchased and
        used for your message360 account.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    numbertype -- NumberTypeEnum -- Number type either
                        SMS,Voice or all
                    areacode -- string -- Specifies the area code for the
                        returned list of available numbers. Only available for
                        North American numbers.
                    response_type -- string -- Response type format xml or
                        json
                    pagesize -- int -- The count of objects to return.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(numbertype=options.get("numbertype"),
                                 areacode=options.get("areacode"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/incomingphone/availablenumber.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'numbertype': options.get('numbertype', None),
            'areacode': options.get('areacode', None),
            'pagesize': options.get('pagesize', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_number_details(self,
                            options=dict()):
        """Does a POST request to /incomingphone/viewnumber.{ResponseType}.

        Retrieve the details for a phone number by its number.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- A valid message360 10-digit
                        phone number (E.164 format).
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
        self.validate_parameters(phone_number=options.get("phone_number"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/incomingphone/viewnumber.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': options.get('phone_number', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def release_number(self,
                       options=dict()):
        """Does a POST request to /incomingphone/releasenumber.{ResponseType}.

        Remove a purchased message360 number from your account.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- A valid 10-digit message360
                        number (E.164 format).
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
        self.validate_parameters(phone_number=options.get("phone_number"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/incomingphone/releasenumber.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': options.get('phone_number', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def buy_number(self,
                   options=dict()):
        """Does a POST request to /incomingphone/buynumber.{ResponseType}.

        Purchase a phone number to be used with your message360 account

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- A valid 10-digit message360
                        number (E.164 format).
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
        self.validate_parameters(phone_number=options.get("phone_number"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/incomingphone/buynumber.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': options.get('phone_number', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def mass_release_number(self,
                            options=dict()):
        """Does a POST request to /incomingphone/massreleasenumber.{ResponseType}.

        Remove a purchased message360 number from your account.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- A valid message360 comma
                        separated numbers (E.164 format).
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
        self.validate_parameters(phone_number=options.get("phone_number"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/incomingphone/massreleasenumber.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': options.get('phone_number', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def update_phone_number(self,
                            options=dict()):
        """Does a POST request to /incomingphone/updatenumber.{ResponseType}.

        Update properties for a message360 number that has been purchased for
        your account. Refer to the parameters list for the list of properties
        that can be updated.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- A valid message360 number (E.164
                        format).
                    voice_url -- string -- URL requested once the call
                        connects
                    response_type -- string -- Response type format xml or
                        json
                    friendly_name -- string -- Phone number friendly name
                        description
                    voice_method -- HttpActionEnum -- Post or Get
                    voice_fallback_url -- string -- URL requested if the voice
                        URL is not available
                    voice_fallback_method -- HttpActionEnum -- Post or Get
                    hangup_callback -- string -- callback url after a hangup
                        occurs
                    hangup_callback_method -- HttpActionEnum -- Post or Get
                    heartbeat_url -- string -- URL requested once the call
                        connects
                    heartbeat_method -- HttpActionEnum -- URL that can be
                        requested every 60 seconds during the call to notify
                        of elapsed time
                    sms_url -- string -- URL requested when an SMS is
                        received
                    sms_method -- HttpActionEnum -- Post or Get
                    sms_fallback_url -- string -- URL used if any errors occur
                        during execution of InboundXML from an SMS or at
                        initial request of the SmsUrl.
                    sms_fallback_method -- HttpActionEnum -- The HTTP method
                        message360 will use when URL requested if the SmsUrl
                        is not available.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(phone_number=options.get("phone_number"),
                                 voice_url=options.get("voice_url"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/incomingphone/updatenumber.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': options.get('phone_number', None),
            'VoiceUrl': options.get('voice_url', None),
            'FriendlyName': options.get('friendly_name', None),
            'VoiceMethod': options.get('voice_method', None),
            'VoiceFallbackUrl': options.get('voice_fallback_url', None),
            'VoiceFallbackMethod': options.get('voice_fallback_method', None),
            'HangupCallback': options.get('hangup_callback', None),
            'HangupCallbackMethod': options.get('hangup_callback_method', None),
            'HeartbeatUrl': options.get('heartbeat_url', None),
            'HeartbeatMethod': options.get('heartbeat_method', None),
            'SmsUrl': options.get('sms_url', None),
            'SmsMethod': options.get('sms_method', None),
            'SmsFallbackUrl': options.get('sms_fallback_url', None),
            'SmsFallbackMethod': options.get('sms_fallback_method', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_number(self,
                    options=dict()):
        """Does a POST request to /incomingphone/listnumber.{ResponseType}.

        Retrieve a list of purchased phones numbers associated with your
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
                        returned. Page indexing starts at 1.
                    page_size -- int -- The page count to retrieve from the
                        total results in the collection. Page indexing starts
                        at 1.
                    number_type -- NumberTypeEnum -- The capability supported
                        by the number.Number type either SMS,Voice or all
                    friendly_name -- string -- A human-readable label added to
                        the number object.

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
        _query_builder += '/incomingphone/listnumber.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Page': options.get('page', None),
            'PageSize': options.get('page_size', None),
            'NumberType': options.get('number_type', None),
            'FriendlyName': options.get('friendly_name', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def mass_update_number(self,
                           options=dict()):
        """Does a POST request to /incomingphone/massupdatenumber.{ResponseType}.

        Update properties for a message360 numbers that has been purchased for
        your account. Refer to the parameters list for the list of properties
        that can be updated.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phone_number -- string -- A valid comma(,) separated
                        message360 numbers. (E.164 format).
                    voice_url -- string -- The URL returning InboundXML
                        incoming calls should execute when connected.
                    response_type -- string -- Response type format xml or
                        json
                    friendly_name -- string -- A human-readable value for
                        labeling the number.
                    voice_method -- HttpActionEnum -- Specifies the HTTP
                        method used to request the VoiceUrl once incoming call
                        connects.
                    voice_fallback_url -- string -- URL used if any errors
                        occur during execution of InboundXML on a call or at
                        initial request of the voice url
                    voice_fallback_method -- HttpActionEnum -- Specifies the
                        HTTP method used to request the VoiceFallbackUrl once
                        incoming call connects.
                    hangup_callback -- string -- URL that can be requested to
                        receive notification when and how incoming call has
                        ended.
                    hangup_callback_method -- HttpActionEnum -- The HTTP
                        method message360 will use when requesting the
                        HangupCallback URL.
                    heartbeat_url -- string -- URL that can be used to monitor
                        the phone number.
                    heartbeat_method -- HttpActionEnum -- The HTTP method
                        message360 will use when requesting the HeartbeatUrl.
                    sms_url -- string -- URL requested when an SMS is
                        received.
                    sms_method -- HttpActionEnum -- The HTTP method message360
                        will use when requesting the SmsUrl.
                    sms_fallback_url -- string -- URL used if any errors occur
                        during execution of InboundXML from an SMS or at
                        initial request of the SmsUrl.
                    sms_fallback_method -- HttpActionEnum -- The HTTP method
                        message360 will use when URL requested if the SmsUrl
                        is not available.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(phone_number=options.get("phone_number"),
                                 voice_url=options.get("voice_url"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/incomingphone/massupdatenumber.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'PhoneNumber': options.get('phone_number', None),
            'VoiceUrl': options.get('voice_url', None),
            'FriendlyName': options.get('friendly_name', None),
            'VoiceMethod': options.get('voice_method', None),
            'VoiceFallbackUrl': options.get('voice_fallback_url', None),
            'VoiceFallbackMethod': options.get('voice_fallback_method', None),
            'HangupCallback': options.get('hangup_callback', None),
            'HangupCallbackMethod': options.get('hangup_callback_method', None),
            'HeartbeatUrl': options.get('heartbeat_url', None),
            'HeartbeatMethod': options.get('heartbeat_method', None),
            'SmsUrl': options.get('sms_url', None),
            'SmsMethod': options.get('sms_method', None),
            'SmsFallbackUrl': options.get('sms_fallback_url', None),
            'SmsFallbackMethod': options.get('sms_fallback_method', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def get_did_score_number(self,
                             options=dict()):
        """Does a POST request to /incomingphone/getdidscore.{ResponseType}.

        Get DID Score Number

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phonenumber -- string -- Specifies the multiple phone
                        numbers for check updated spamscore .
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
        self.validate_parameters(phonenumber=options.get("phonenumber"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/incomingphone/getdidscore.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Phonenumber': options.get('phonenumber', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def bulk_buy_number(self,
                        options=dict()):
        """Does a POST request to /incomingphone/bulkbuy.{ResponseType}.

        Purchase a selected number of DID's from specific area codes to be
        used with your message360 account.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    number_type -- NumberTypeEnum -- The capability the number
                        supports.
                    area_code -- string -- Specifies the area code for the
                        returned list of available numbers. Only available for
                        North American numbers.
                    quantity -- string -- A positive integer that tells how
                        many number you want to buy at a time.
                    response_type -- string -- Response type format xml or
                        json
                    leftover -- string -- If desired quantity is unavailable
                        purchase what is available .

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(number_type=options.get("number_type"),
                                 area_code=options.get("area_code"),
                                 quantity=options.get("quantity"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/incomingphone/bulkbuy.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'NumberType': options.get('number_type', None),
            'AreaCode': options.get('area_code', None),
            'Quantity': options.get('quantity', None),
            'Leftover': options.get('leftover', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def transfer_number(self,
                        options=dict()):
        """Does a POST request to /incomingphone/transferphonenumbers.{ResponseType}.

        Transfer phone number that has been purchased for from one account to
        another account.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phonenumber -- string -- A valid 10-digit message360
                        number (E.164 format).
                    fromaccountsid -- string -- A specific Accountsid from
                        where Number is getting transfer.
                    toaccountsid -- string -- A specific Accountsid to which
                        Number is getting transfer.
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
        self.validate_parameters(phonenumber=options.get("phonenumber"),
                                 fromaccountsid=options.get("fromaccountsid"),
                                 toaccountsid=options.get("toaccountsid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/incomingphone/transferphonenumbers.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'phonenumber': options.get('phonenumber', None),
            'fromaccountsid': options.get('fromaccountsid', None),
            'toaccountsid': options.get('toaccountsid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
