# -*- coding: utf-8 -*-

"""
    message_360.controllers.call_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class CallController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def create_group_call(self,
                          options=dict()):
        """Does a POST request to /calls/groupcall.{ResponseType}.

        Group Call

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    from_country_code -- string -- TODO: type description
                        here. Example: 1
                    mfrom -- string -- TODO: type description here. Example: 
                    to_country_code -- string -- TODO: type description here.
                        Example: 1
                    to -- string -- TODO: type description here. Example: 
                    url -- string -- TODO: type description here. Example: 
                    response_type -- string -- TODO: type description here.
                        Example: json
                    method -- HttpActionEnum -- TODO: type description here.
                        Example: 
                    status_call_back_url -- string -- TODO: type description
                        here. Example: 
                    status_call_back_method -- HttpActionEnum -- TODO: type
                        description here. Example: 
                    fall_back_url -- string -- TODO: type description here.
                        Example: 
                    fall_back_method -- HttpActionEnum -- TODO: type
                        description here. Example: 
                    heart_beat_url -- string -- TODO: type description here.
                        Example: 
                    heart_beat_method -- HttpActionEnum -- TODO: type
                        description here. Example: 
                    timeout -- int -- TODO: type description here. Example: 
                    play_dtmf -- string -- TODO: type description here.
                        Example: 
                    hide_caller_id -- string -- TODO: type description here.
                        Example: 
                    record -- bool -- TODO: type description here. Example: 
                    record_call_back_url -- string -- TODO: type description
                        here. Example: 
                    record_call_back_method -- HttpActionEnum -- TODO: type
                        description here. Example: 
                    transcribe -- bool -- TODO: type description here.
                        Example: 
                    transcribe_call_back_url -- string -- TODO: type
                        description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(from_country_code=options.get("from_country_code"),
                                 mfrom=options.get("mfrom"),
                                 to_country_code=options.get("to_country_code"),
                                 to=options.get("to"),
                                 url=options.get("url"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/groupcall.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'FromCountryCode': options.get('from_country_code', None),
            'From': options.get('mfrom', None),
            'ToCountryCode': options.get('to_country_code', None),
            'To': options.get('to', None),
            'Url': options.get('url', None),
            'Method': options.get('method', None),
            'StatusCallBackUrl': options.get('status_call_back_url', None),
            'StatusCallBackMethod': options.get('status_call_back_method', None),
            'FallBackUrl': options.get('fall_back_url', None),
            'FallBackMethod': options.get('fall_back_method', None),
            'HeartBeatUrl': options.get('heart_beat_url', None),
            'HeartBeatMethod': options.get('heart_beat_method', None),
            'Timeout': options.get('timeout', None),
            'PlayDtmf': options.get('play_dtmf', None),
            'HideCallerId': options.get('hide_caller_id', None),
            'Record': options.get('record', None),
            'RecordCallBackUrl': options.get('record_call_back_url', None),
            'RecordCallBackMethod': options.get('record_call_back_method', None),
            'Transcribe': options.get('transcribe', None),
            'TranscribeCallBackUrl': options.get('transcribe_call_back_url', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_voice_effect(self,
                            options=dict()):
        """Does a POST request to /calls/voiceeffect.{ResponseType}.

        Voice Effect

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- TODO: type description here.
                        Example: 
                    response_type -- string -- Response type format xml or
                        json
                    audio_direction -- AudioDirectionEnum -- TODO: type
                        description here. Example: 
                    pitch_semi_tones -- float -- value between -14 and 14
                    pitch_octaves -- float -- value between -1 and 1
                    pitch -- float -- value greater than 0
                    rate -- float -- value greater than 0
                    tempo -- float -- value greater than 0

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(call_sid=options.get("call_sid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/voiceeffect.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'CallSid': options.get('call_sid', None),
            'AudioDirection': options.get('audio_direction', None),
            'PitchSemiTones': options.get('pitch_semi_tones', None),
            'PitchOctaves': options.get('pitch_octaves', None),
            'Pitch': options.get('pitch', None),
            'Rate': options.get('rate', None),
            'Tempo': options.get('tempo', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_record_call(self,
                           options=dict()):
        """Does a POST request to /calls/recordcalls.{ResponseType}.

        Record a Call

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- The unique identifier of each call
                        resource
                    record -- bool -- Set true to initiate recording or false
                        to terminate recording
                    response_type -- string -- Response format, xml or json
                    direction -- DirectionEnum -- The leg of the call to
                        record
                    time_limit -- int -- Time in seconds the recording
                        duration should not exceed
                    call_back_url -- string -- URL consulted after the
                        recording completes
                    fileformat -- AudioFormatEnum -- Format of the recording
                        file. Can be .mp3 or .wav

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(call_sid=options.get("call_sid"),
                                 record=options.get("record"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/recordcalls.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'CallSid': options.get('call_sid', None),
            'Record': options.get('record', None),
            'Direction': options.get('direction', None),
            'TimeLimit': options.get('time_limit', None),
            'CallBackUrl': options.get('call_back_url', None),
            'Fileformat': options.get('fileformat', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_play_audio(self,
                          options=dict()):
        """Does a POST request to /calls/playaudios.{ResponseType}.

        Play Dtmf and send the Digit

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- The unique identifier of each call
                        resource
                    audio_url -- string -- URL to sound that should be played.
                        You also can add more than one audio file using
                        semicolons e.g.
                        http://example.com/audio1.mp3;http://example.com/audio2
                        .wav
                    response_type -- string -- Response type format xml or
                        json
                    length -- int -- Time limit in seconds for audio play
                        back
                    direction -- DirectionEnum -- The leg of the call audio
                        will be played to
                    loop -- bool -- Repeat audio playback indefinitely
                    mix -- bool -- If false, all other audio will be muted

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(call_sid=options.get("call_sid"),
                                 audio_url=options.get("audio_url"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/playaudios.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'CallSid': options.get('call_sid', None),
            'AudioUrl': options.get('audio_url', None),
            'Length': options.get('length', None),
            'Direction': options.get('direction', None),
            'Loop': options.get('loop', None),
            'Mix': options.get('mix', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_interrupted_call(self,
                                options=dict()):
        """Does a POST request to /calls/interruptcalls.{ResponseType}.

        Interrupt the Call by Call Sid

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- Call SId
                    response_type -- string -- Response type format xml or
                        json
                    url -- string -- URL the in-progress call will be
                        redirected to
                    method -- HttpActionEnum -- The method used to request the
                        above Url parameter
                    status -- InterruptedCallStatusEnum -- Status to set the
                        in-progress call to

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(call_sid=options.get("call_sid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/interruptcalls.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'CallSid': options.get('call_sid', None),
            'Url': options.get('url', None),
            'Method': options.get('method', None),
            'Status': options.get('status', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_send_digit(self,
                          options=dict()):
        """Does a POST request to /calls/senddigits.{ResponseType}.

        Play Dtmf and send the Digit

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- The unique identifier of each call
                        resource
                    play_dtmf -- string -- DTMF digits to play to the call.
                        0-9, #, *, W, or w
                    response_type -- string -- Response type format xml or
                        json
                    play_dtmf_direction -- DirectionEnum -- The leg of the
                        call DTMF digits should be sent to

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(call_sid=options.get("call_sid"),
                                 play_dtmf=options.get("play_dtmf"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/senddigits.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'CallSid': options.get('call_sid', None),
            'PlayDtmf': options.get('play_dtmf', None),
            'PlayDtmfDirection': options.get('play_dtmf_direction', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_make_call(self,
                         options=dict()):
        """Does a POST request to /calls/makecall.{ResponseType}.

        You can experiment with initiating a call through Message360 and view
        the request response generated when doing so and get the response in
        json

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    from_country_code -- string -- from country code
                    mfrom -- string -- This number to display on Caller ID as
                        calling
                    to_country_code -- string -- To cuntry code number
                    to -- string -- To number
                    url -- string -- URL requested once the call connects
                    response_type -- string -- Response type format xml or
                        json
                    method -- HttpActionEnum -- Specifies the HTTP method used
                        to request the required URL once call connects.
                    status_call_back_url -- string -- specifies the HTTP
                        methodlinkclass used to request StatusCallbackUrl.
                    status_call_back_method -- HttpActionEnum -- Specifies the
                        HTTP methodlinkclass used to request
                        StatusCallbackUrl.
                    fall_back_url -- string -- URL requested if the initial
                        Url parameter fails or encounters an error
                    fall_back_method -- HttpActionEnum -- Specifies the HTTP
                        method used to request the required FallbackUrl once
                        call connects.
                    heart_beat_url -- string -- URL that can be requested
                        every 60 seconds during the call to notify of elapsed
                        tim
                    heart_beat_method -- bool -- Specifies the HTTP method
                        used to request HeartbeatUrl.
                    timeout -- int -- Time (in seconds) Message360 should wait
                        while the call is ringing before canceling the call
                    play_dtmf -- string -- DTMF Digits to play to the call
                        once it connects. 0-9, #, or *
                    hide_caller_id -- bool -- Specifies if the caller id will
                        be hidden
                    record -- bool -- Specifies if the call should be
                        recorded
                    record_call_back_url -- string -- Recording parameters
                        will be sent here upon completion
                    record_call_back_method -- HttpActionEnum -- Method used
                        to request the RecordCallback URL.
                    transcribe -- bool -- Specifies if the call recording
                        should be transcribed
                    transcribe_call_back_url -- string -- Transcription
                        parameters will be sent here upon completion
                    if_machine -- IfMachineEnum -- How Message360 should
                        handle the receiving numbers voicemail machine

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(from_country_code=options.get("from_country_code"),
                                 mfrom=options.get("mfrom"),
                                 to_country_code=options.get("to_country_code"),
                                 to=options.get("to"),
                                 url=options.get("url"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/makecall.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_parameters = {
            'Method': options.get('method', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'FromCountryCode': options.get('from_country_code', None),
            'From': options.get('mfrom', None),
            'ToCountryCode': options.get('to_country_code', None),
            'To': options.get('to', None),
            'Url': options.get('url', None),
            'StatusCallBackUrl': options.get('status_call_back_url', None),
            'StatusCallBackMethod': options.get('status_call_back_method', None),
            'FallBackUrl': options.get('fall_back_url', None),
            'FallBackMethod': options.get('fall_back_method', None),
            'HeartBeatUrl': options.get('heart_beat_url', None),
            'HeartBeatMethod': options.get('heart_beat_method', None),
            'Timeout': options.get('timeout', None),
            'PlayDtmf': options.get('play_dtmf', None),
            'HideCallerId': options.get('hide_caller_id', None),
            'Record': options.get('record', None),
            'RecordCallBackUrl': options.get('record_call_back_url', None),
            'RecordCallBackMethod': options.get('record_call_back_method', None),
            'Transcribe': options.get('transcribe', None),
            'TranscribeCallBackUrl': options.get('transcribe_call_back_url', None),
            'IfMachine': options.get('if_machine', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_list_calls(self,
                          options=dict()):
        """Does a POST request to /calls/listcalls.{ResponseType}.

        A list of calls associated with your Message360 account

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
                    to -- string -- Only list calls to this number
                    mfrom -- string -- Only list calls from this number
                    date_created -- string -- Only list calls starting within
                        the specified date range

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
        _query_builder += '/calls/listcalls.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Page': options.get('page', None),
            'PageSize': options.get('page_size', None),
            'To': options.get('to', None),
            'From': options.get('mfrom', None),
            'DateCreated': options.get('date_created', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_send_ringless_vm(self,
                                options=dict()):
        """Does a POST request to /calls/makeringlessvoicemailcall.{ResponseType}.

        API endpoint used to send a Ringless Voicemail

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    from_country_code -- string -- From country code
                    mfrom -- string -- This number to display on Caller ID as
                        calling
                    to_country_code -- string -- To country code
                    to -- string -- To number
                    voice_mail_url -- string -- URL to an audio file
                    method -- string -- Not currently used in this version
                    response_type -- string -- Response type format xml or
                        json
                    status_call_back_url -- string -- URL to post the status
                        of the Ringless request
                    stats_call_back_method -- string -- POST or GET

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(from_country_code=options.get("from_country_code"),
                                 mfrom=options.get("mfrom"),
                                 to_country_code=options.get("to_country_code"),
                                 to=options.get("to"),
                                 voice_mail_url=options.get("voice_mail_url"),
                                 method=options.get("method"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/makeringlessvoicemailcall.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'FromCountryCode': options.get('from_country_code', None),
            'From': options.get('mfrom', None),
            'ToCountryCode': options.get('to_country_code', None),
            'To': options.get('to', None),
            'VoiceMailURL': options.get('voice_mail_url', None),
            'Method': options.get('method', None),
            'StatusCallBackUrl': options.get('status_call_back_url', None),
            'StatsCallBackMethod': options.get('stats_call_back_method', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_view_call(self,
                         options=dict()):
        """Does a POST request to /calls/viewcalls.{ResponseType}.

        View Call Response

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    callsid -- string -- Call Sid id for particular Call
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
        self.validate_parameters(callsid=options.get("callsid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/viewcalls.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'callsid': options.get('callsid', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
