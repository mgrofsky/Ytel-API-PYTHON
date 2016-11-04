# -*- coding: utf-8 -*-

"""
    message360.controllers.call_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 11/04/2016
"""

from .base_controller import *



class CallController(BaseController):

    """A Controller to access Endpoints in the message360 API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def create_view_call(self,
                         callsid,
                         response_type = 'json'):
        """Does a POST request to /calls/viewcalls.{ResponseType}.

        View Call Response

        Args:
            callsid (string): Call Sid id for particular Call
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
        if callsid == None:
            raise ValueError("Required parameter 'callsid' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/calls/viewcalls.{ResponseType}'

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
            'callsid': callsid
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



    def create_make_call(self,
                         from_country_code,
                         mfrom,
                         to_country_code,
                         to,
                         url,
                         method = None,
                         status_call_back_url = None,
                         status_call_back_method = None,
                         fall_back_url = None,
                         fall_back_method = None,
                         heart_beat_url = None,
                         heart_beat_method = None,
                         timeout = None,
                         play_dtmf = None,
                         hide_caller_id = None,
                         record = None,
                         record_call_back_url = None,
                         record_call_back_method = None,
                         transcribe = None,
                         transcribe_call_back_url = None,
                         if_machine = None,
                         response_type = 'json'):
        """Does a POST request to /calls/makecall.{ResponseType}.

        You can experiment with initiating a call through Message360 and view
        the request response generated when doing so and get the response in
        json

        Args:
            from_country_code (string): from country code
            mfrom (string): This number to display on Caller ID as calling
            to_country_code (string): To cuntry code number
            to (string): To number
            url (string): URL requested once the call connects
            method (HttpAction, optional): Specifies the HTTP method used to
                request the required URL once call connects.
            status_call_back_url (string, optional): specifies the HTTP
                methodlinkclass used to request StatusCallbackUrl.
            status_call_back_method (HttpAction, optional): Specifies the HTTP
                methodlinkclass used to request StatusCallbackUrl.
            fall_back_url (string, optional): URL requested if the initial Url
                parameter fails or encounters an error
            fall_back_method (HttpAction, optional): Specifies the HTTP method
                used to request the required FallbackUrl once call connects.
            heart_beat_url (string, optional): URL that can be requested every
                60 seconds during the call to notify of elapsed tim
            heart_beat_method (bool, optional): Specifies the HTTP method used
                to request HeartbeatUrl.
            timeout (int, optional): Time (in seconds) Message360 should wait
                while the call is ringing before canceling the call
            play_dtmf (string, optional): DTMF Digits to play to the call once
                it connects. 0-9, #, or *
            hide_caller_id (bool, optional): Specifies if the caller id will
                be hidden
            record (bool, optional): Specifies if the call should be recorded
            record_call_back_url (string, optional): Recording parameters will
                be sent here upon completion
            record_call_back_method (HttpAction, optional): Method used to
                request the RecordCallback URL.
            transcribe (bool, optional): Specifies if the call recording
                should be transcribed
            transcribe_call_back_url (string, optional): Transcription
                parameters will be sent here upon completion
            if_machine (IfMachine, optional): How Message360 should handle the
                receiving numbers voicemail machine
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
        if from_country_code == None:
            raise ValueError("Required parameter 'from_country_code' cannot be None.")
        elif mfrom == None:
            raise ValueError("Required parameter 'mfrom' cannot be None.")
        elif to_country_code == None:
            raise ValueError("Required parameter 'to_country_code' cannot be None.")
        elif to == None:
            raise ValueError("Required parameter 'to' cannot be None.")
        elif url == None:
            raise ValueError("Required parameter 'url' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/calls/makecall.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': response_type
        })

        # Process optional query parameters
        _query_parameters = {
            'Method': method
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'message360-api'
        }

        # Prepare form parameters
        _form_parameters = {
            'FromCountryCode': from_country_code,
            'From': mfrom,
            'ToCountryCode': to_country_code,
            'To': to,
            'Url': url,
            'StatusCallBackUrl': status_call_back_url,
            'StatusCallBackMethod': status_call_back_method,
            'FallBackUrl': fall_back_url,
            'FallBackMethod': fall_back_method,
            'HeartBeatUrl': heart_beat_url,
            'HeartBeatMethod': heart_beat_method,
            'Timeout': timeout,
            'PlayDtmf': play_dtmf,
            'HideCallerId': hide_caller_id,
            'Record': record,
            'RecordCallBackUrl': record_call_back_url,
            'RecordCallBackMethod': record_call_back_method,
            'Transcribe': transcribe,
            'TranscribeCallBackUrl': transcribe_call_back_url,
            'IfMachine': if_machine
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, query_parameters=_query_parameters, parameters=_form_parameters, username=Configuration.basic_auth_user_name, password=Configuration.basic_auth_password)

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



    def create_play_audio(self,
                          length,
                          direction,
                          loop,
                          mix,
                          call_sid = None,
                          audio_url = None,
                          response_type = 'json'):
        """Does a POST request to /calls/playaudios.{ResponseType}.

        Play Dtmf and send the Digit

        Args:
            length (int): Time limit in seconds for audio play back
            direction (Direction): The leg of the call audio will be played
                to
            loop (bool): Repeat audio playback indefinitely
            mix (bool): If false, all other audio will be muted
            call_sid (string, optional): The unique identifier of each call
                resource
            audio_url (string, optional): URL to sound that should be played.
                You also can add more than one audio file using semicolons
                e.g.
                http://example.com/audio1.mp3;http://example.com/audio2.wav
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
        if length == None:
            raise ValueError("Required parameter 'length' cannot be None.")
        elif direction == None:
            raise ValueError("Required parameter 'direction' cannot be None.")
        elif loop == None:
            raise ValueError("Required parameter 'loop' cannot be None.")
        elif mix == None:
            raise ValueError("Required parameter 'mix' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/calls/playaudios.{ResponseType}'

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
            'Length': length,
            'Direction': direction,
            'Loop': loop,
            'Mix': mix,
            'CallSid': call_sid,
            'AudioUrl': audio_url
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



    def create_record_call(self,
                           call_sid,
                           record,
                           direction = None,
                           time_limit = None,
                           call_back_url = None,
                           fileformat = None,
                           response_type = 'json'):
        """Does a POST request to /calls/recordcalls.{ResponseType}.

        Record a Call

        Args:
            call_sid (string): The unique identifier of each call resource
            record (bool): Set true to initiate recording or false to
                terminate recording
            direction (Direction, optional): The leg of the call to record
            time_limit (int, optional): Time in seconds the recording duration
                should not exceed
            call_back_url (string, optional): URL consulted after the
                recording completes
            fileformat (AudioFormat, optional): Format of the recording file.
                Can be .mp3 or .wav
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
        if call_sid == None:
            raise ValueError("Required parameter 'call_sid' cannot be None.")
        elif record == None:
            raise ValueError("Required parameter 'record' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/calls/recordcalls.{ResponseType}'

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
            'CallSid': call_sid,
            'Record': record,
            'Direction': direction,
            'TimeLimit': time_limit,
            'CallBackUrl': call_back_url,
            'Fileformat': fileformat
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



    def create_voice_effect(self,
                            call_sid,
                            audio_direction = None,
                            pitch_semi_tones = None,
                            pitch_octaves = None,
                            pitch = None,
                            rate = None,
                            tempo = None,
                            response_type = 'json'):
        """Does a POST request to /calls/voiceeffect.{ResponseType}.

        Voice Effect

        Args:
            call_sid (string): TODO: type description here. Example: 
            audio_direction (AudioDirection, optional): TODO: type description
                here. Example: 
            pitch_semi_tones (float, optional): value between -14 and 14
            pitch_octaves (float, optional): value between -1 and 1
            pitch (float, optional): value greater than 0
            rate (float, optional): value greater than 0
            tempo (float, optional): value greater than 0
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
        if call_sid == None:
            raise ValueError("Required parameter 'call_sid' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/calls/voiceeffect.{ResponseType}'

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
            'CallSid': call_sid,
            'AudioDirection': audio_direction,
            'PitchSemiTones': pitch_semi_tones,
            'PitchOctaves': pitch_octaves,
            'Pitch': pitch,
            'Rate': rate,
            'Tempo': tempo
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



    def create_send_digit(self,
                          call_sid,
                          play_dtmf,
                          play_dtmf_direction = None,
                          response_type = 'json'):
        """Does a POST request to /calls/senddigits.{ResponseType}.

        Play Dtmf and send the Digit

        Args:
            call_sid (string): The unique identifier of each call resource
            play_dtmf (string): DTMF digits to play to the call. 0-9, #, *, W,
                or w
            play_dtmf_direction (Direction, optional): The leg of the call
                DTMF digits should be sent to
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
        if call_sid == None:
            raise ValueError("Required parameter 'call_sid' cannot be None.")
        elif play_dtmf == None:
            raise ValueError("Required parameter 'play_dtmf' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/calls/senddigits.{ResponseType}'

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
            'CallSid': call_sid,
            'PlayDtmf': play_dtmf,
            'PlayDtmfDirection': play_dtmf_direction
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



    def create_interrupted_call(self,
                                call_sid,
                                url = None,
                                method = None,
                                status = None,
                                response_type = 'json'):
        """Does a POST request to /calls/interruptcalls.{ResponseType}.

        Interrupt the Call by Call Sid

        Args:
            call_sid (string): Call SId
            url (string, optional): URL the in-progress call will be
                redirected to
            method (HttpAction, optional): The method used to request the
                above Url parameter
            status (InterruptedCallStatus, optional): Status to set the
                in-progress call to
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
        if call_sid == None:
            raise ValueError("Required parameter 'call_sid' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/calls/interruptcalls.{ResponseType}'

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
            'CallSid': call_sid,
            'Url': url,
            'Method': method,
            'Status': status
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



    def create_list_calls(self,
                          page = None,
                          page_size = None,
                          to = None,
                          mfrom = None,
                          date_created = None,
                          response_type = 'json'):
        """Does a POST request to /calls/listcalls.{ResponseType}.

        A list of calls associated with your Message360 account

        Args:
            page (string, optional): Which page of the overall response will
                be returned. Zero indexed
            page_size (string, optional): Number of individual resources
                listed in the response per page
            to (string, optional): Only list calls to this number
            mfrom (string, optional): Only list calls from this number
            date_created (string, optional): Only list calls starting within
                the specified date range
            response_type (string, optional): Response format, xml or json

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/calls/listcalls.{ResponseType}'

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
            'Page': page,
            'PageSize': page_size,
            'To': to,
            'From': mfrom,
            'DateCreated': date_created
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
