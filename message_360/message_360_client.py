# -*- coding: utf-8 -*-

"""
    message_360.message_360_client

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""
from .decorators import lazy_property
from .configuration import Configuration
from .controllers.shared_short_code_controller import SharedShortCodeController
from .controllers.conference_controller import ConferenceController
from .controllers.transcription_controller import TranscriptionController
from .controllers.phone_number_controller import PhoneNumberController
from .controllers.usage_controller import UsageController
from .controllers.web_rtc_controller import WebRTCController
from .controllers.recording_controller import RecordingController
from .controllers.email_controller import EmailController
from .controllers.sms_controller import SMSController
from .controllers.call_controller import CallController
from .controllers.carrier_controller import CarrierController
from .controllers.address_controller import AddressController
from .controllers.sub_account_controller import SubAccountController
from .controllers.account_controller import AccountController
from .controllers.short_code_controller import ShortCodeController

class Message360Client(object):

    config = Configuration

    @lazy_property
    def shared_short_code(self):
        return SharedShortCodeController()

    @lazy_property
    def conference(self):
        return ConferenceController()

    @lazy_property
    def transcription(self):
        return TranscriptionController()

    @lazy_property
    def phone_number(self):
        return PhoneNumberController()

    @lazy_property
    def usage(self):
        return UsageController()

    @lazy_property
    def web_rtc(self):
        return WebRTCController()

    @lazy_property
    def recording(self):
        return RecordingController()

    @lazy_property
    def email(self):
        return EmailController()

    @lazy_property
    def sms(self):
        return SMSController()

    @lazy_property
    def call(self):
        return CallController()

    @lazy_property
    def carrier(self):
        return CarrierController()

    @lazy_property
    def address(self):
        return AddressController()

    @lazy_property
    def sub_account(self):
        return SubAccountController()

    @lazy_property
    def account(self):
        return AccountController()

    @lazy_property
    def short_code(self):
        return ShortCodeController()


    def __init__(self, 
                 basic_auth_user_name = None,
                 basic_auth_password = None):
        if basic_auth_user_name != None:
            Configuration.basic_auth_user_name = basic_auth_user_name
        if basic_auth_password != None:
            Configuration.basic_auth_password = basic_auth_password


