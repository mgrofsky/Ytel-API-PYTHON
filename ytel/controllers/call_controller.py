# -*- coding: utf-8 -*-

"""
    ytel.controllers.call_controller

    This file was automatically generated for ytel by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class CallController(BaseController):

    """A Controller to access Endpoints in the ytel API."""


    def make_call(self,
                  options=dict()):
        """Does a POST request to /calls/makecall.{ResponseType}.

        You can experiment with initiating a call through Ytel and view the
        request response generated when doing so and get the response in json

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    mfrom -- string -- A valid Ytel Voice enabled number
                        (E.164 format) that will be initiating the phone
                        call.
                    to -- string -- To number
                    url -- string -- URL requested once the call connects
                    response_type -- string -- Response type format xml or
                        json
                    method -- HttpActionEnum -- Specifies the HTTP method used
                        to request the required URL once call connects.
                    status_call_back_url -- string -- URL that can be
                        requested to receive notification when call has ended.
                        A set of default parameters will be sent here once the
                        call is finished.
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
                    heart_beat_method -- HttpActionEnum -- Specifies the HTTP
                        method used to request HeartbeatUrl.
                    timeout -- int -- Time (in seconds) Ytel should wait while
                        the call is ringing before canceling the call
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
                    if_machine -- IfMachineEnum -- How Ytel should handle the
                        receiving numbers voicemail machine
                    if_machine_url -- string -- URL requested when
                        IfMachine=continue
                    if_machine_method -- HttpActionEnum -- Method used to
                        request the IfMachineUrl.
                    feedback -- bool -- Specify if survey should be enable or
                        not
                    survey_id -- string -- The unique identifier for the
                        survey.

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
                                 url=options.get("url"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/makecall.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'From': options.get('mfrom', None),
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
            'TranscribeCallBackUrl': options.get('transcribe_call_back_url', None),
            'IfMachine': options.get('if_machine', None),
            'IfMachineUrl': options.get('if_machine_url', None),
            'IfMachineMethod': options.get('if_machine_method', None),
            'Feedback': options.get('feedback', None),
            'SurveyId': options.get('survey_id', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def play_audio(self,
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
                    say_text -- string -- Valid alphanumeric string that
                        should be played to the In-progress call.
                    response_type -- string -- Response type format xml or
                        json
                    length -- int -- Time limit in seconds for audio play
                        back
                    direction -- DirectionEnum -- The leg of the call audio
                        will be played to
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
                                 say_text=options.get("say_text"),
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
            'SayText': options.get('say_text', None),
            'Length': options.get('length', None),
            'Direction': options.get('direction', None),
            'Mix': options.get('mix', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def record_call(self,
                    options=dict()):
        """Does a POST request to /calls/recordcalls.{ResponseType}.

        Start or stop recording of an in-progress voice call.

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

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def voice_effect(self,
                     options=dict()):
        """Does a POST request to /calls/voiceeffect.{ResponseType}.

        Add audio voice effects to the an in-progress voice call.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- The unique identifier for the
                        in-progress voice call.
                    response_type -- string -- Response type format xml or
                        json
                    audio_direction -- AudioDirectionEnum -- The direction the
                        audio effect should be placed on. If IN, the effects
                        will occur on the incoming audio stream. If OUT, the
                        effects will occur on the outgoing audio stream.
                    pitch_semi_tones -- float -- Set the pitch in semitone
                        (half-step) intervals. Value between -14 and 14
                    pitch_octaves -- float -- Set the pitch in octave
                        intervals.. Value between -1 and 1
                    pitch -- float -- Set the pitch (lowness/highness) of the
                        audio. The higher the value, the higher the pitch.
                        Value greater than 0
                    rate -- float -- Set the rate for audio. The lower the
                        value, the lower the rate. value greater than 0
                    tempo -- float -- Set the tempo (speed) of the audio. A
                        higher value denotes a faster tempo. Value greater
                        than 0

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

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def send_digit(self,
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

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def interrupted_call(self,
                         options=dict()):
        """Does a POST request to /calls/interruptcalls.{ResponseType}.

        Interrupt the Call by Call Sid

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- The unique identifier for voice call
                        that is in progress.
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

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_calls(self,
                   options=dict()):
        """Does a POST request to /calls/listcalls.{ResponseType}.

        A list of calls associated with your Ytel account

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
                    to -- string -- Filter calls that were sent to this
                        10-digit number (E.164 format).
                    mfrom -- string -- Filter calls that were sent from this
                        10-digit number (E.164 format).
                    date_created -- string -- Return calls that are from a
                        specified date.

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

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def send_ringless_vm(self,
                         options=dict()):
        """Does a POST request to /calls/makervm.{ResponseType}.

        Initiate an outbound Ringless Voicemail through Ytel.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    mfrom -- string -- A valid Ytel Voice enabled number
                        (E.164 format) that will be initiating the phone
                        call.
                    rvm_caller_id -- string -- A required secondary Caller ID
                        for RVM to work.
                    to -- string -- A valid number (E.164 format) that will
                        receive the phone call.
                    voice_mail_url -- string -- The URL requested once the RVM
                        connects. A set of default parameters will be sent
                        here.
                    response_type -- string -- Response type format xml or
                        json
                    method -- HttpActionEnum -- Specifies the HTTP method used
                        to request the required URL once call connects.
                    status_call_back_url -- string -- URL that can be
                        requested to receive notification when call has ended.
                        A set of default parameters will be sent here once the
                        call is finished.
                    stats_call_back_method -- HttpActionEnum -- Specifies the
                        HTTP method used to request the required
                        StatusCallBackUrl once call connects.

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
                                 rvm_caller_id=options.get("rvm_caller_id"),
                                 to=options.get("to"),
                                 voice_mail_url=options.get("voice_mail_url"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/makervm.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'From': options.get('mfrom', None),
            'RVMCallerId': options.get('rvm_caller_id', None),
            'To': options.get('to', None),
            'VoiceMailURL': options.get('voice_mail_url', None),
            'Method': options.get('method', None),
            'StatusCallBackUrl': options.get('status_call_back_url', None),
            'StatsCallBackMethod': options.get('stats_call_back_method', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_call(self,
                  options=dict()):
        """Does a POST request to /calls/viewcalls.{ResponseType}.

        Retrieve a single voice call’s information by its CallSid.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    callsid -- string -- The unique identifier for the voice
                        call.
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

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_call_detail(self,
                         call_sid,
                         response_type):
        """Does a POST request to /calls/viewcalldetail.{ResponseType}.

        Retrieve a single voice call’s information by its CallSid.

        Args:
            call_sid (string): The unique identifier for the voice call.
            response_type (string): Response type format xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(call_sid=call_sid,
                                 response_type=response_type)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/viewcalldetail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': response_type
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'callSid': call_sid
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def group_call(self,
                   options=dict()):
        """Does a POST request to /calls/groupcall.{ResponseType}.

        Group Call

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    mfrom -- string -- This number to display on Caller ID as
                        calling
                    to -- string -- Please enter multiple E164 number. You can
                        add max 10 numbers. Add numbers separated with comma.
                        e.g : 1111111111,2222222222
                    url -- string -- URL requested once the call connects
                    response_type -- string -- TODO: type description here.
                        Example: json
                    group_confirm_key -- string -- Define the DTMF that the
                        called party should send to bridge the call. Allowed
                        Values : 0-9, #, *
                    group_confirm_file -- AudioFormatEnum -- Specify the audio
                        file you want to play when the called party picks up
                        the call
                    method -- HttpActionEnum -- Specifies the HTTP method used
                        to request the required URL once call connects.
                    status_call_back_url -- string -- URL that can be
                        requested to receive notification when call has ended.
                        A set of default parameters will be sent here once the
                        call is finished.
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
                        time and pass other general information.
                    heart_beat_method -- HttpActionEnum -- Specifies the HTTP
                        method used to request HeartbeatUrl.
                    timeout -- int -- Time (in seconds) we should wait while
                        the call is ringing before canceling the call
                    play_dtmf -- string -- DTMF Digits to play to the call
                        once it connects. 0-9, #, or *
                    hide_caller_id -- string -- Specifies if the caller id
                        will be hidden
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
                                 url=options.get("url"),
                                 response_type=options.get("response_type"),
                                 group_confirm_key=options.get("group_confirm_key"),
                                 group_confirm_file=options.get("group_confirm_file"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/calls/groupcall.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'From': options.get('mfrom', None),
            'To': options.get('to', None),
            'Url': options.get('url', None),
            'GroupConfirmKey': options.get('group_confirm_key', None),
            'GroupConfirmFile': options.get('group_confirm_file', None),
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

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
