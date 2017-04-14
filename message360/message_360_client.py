# -*- coding: utf-8 -*-

"""
    message360.message_360_client

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""
from .decorators import lazy_property
from .controllers.short_code_controller import ShortCodeController
from .controllers.conference_controller import ConferenceController
from .controllers.email_controller import EmailController
from .controllers.number_verification_controller import NumberVerificationController
from .controllers.carrier_controller import CarrierController
from .controllers.call_controller import CallController
from .controllers.web_rtc_controller import WebRTCController
from .controllers.sub_account_controller import SubAccountController
from .controllers.address_controller import AddressController
from .controllers.phone_number_controller import PhoneNumberController
from .controllers.recording_controller import RecordingController
from .controllers.sms_controller import SMSController
from .controllers.transcription_controller import TranscriptionController
from .controllers.usage_controller import UsageController
from .controllers.account_controller import AccountController
from .configuration import Configuration

class Message360Client(object):

    @lazy_property
    def short_code(self):
        return ShortCodeController()

    @lazy_property
    def conference(self):
        return ConferenceController()

    @lazy_property
    def email(self):
        return EmailController()

    @lazy_property
    def number_verification(self):
        return NumberVerificationController()

    @lazy_property
    def carrier(self):
        return CarrierController()

    @lazy_property
    def call(self):
        return CallController()

    @lazy_property
    def web_rtc(self):
        return WebRTCController()

    @lazy_property
    def sub_account(self):
        return SubAccountController()

    @lazy_property
    def address(self):
        return AddressController()

    @lazy_property
    def phone_number(self):
        return PhoneNumberController()

    @lazy_property
    def recording(self):
        return RecordingController()

    @lazy_property
    def sms(self):
        return SMSController()

    @lazy_property
    def transcription(self):
        return TranscriptionController()

    @lazy_property
    def usage(self):
        return UsageController()

    @lazy_property
    def account(self):
        return AccountController()


    def __init__(self, 
                 basic_auth_user_name = None,
                 basic_auth_password = None):
        if basic_auth_user_name != None:
            Configuration.basic_auth_user_name = basic_auth_user_name
        if basic_auth_password != None:
            Configuration.basic_auth_password = basic_auth_password


