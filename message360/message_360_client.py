# -*- coding: utf-8 -*-

"""
    message360.message_360_client

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 11/04/2016
"""

from .http import *
from .models import *
from .exceptions import *
from .decorators import *
from .controllers import *

class Message360Client(object):

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
    def email(self):
        return EmailController()

    @lazy_property
    def sms(self):
        return SMSController()

    @lazy_property
    def account(self):
        return AccountController()

    @lazy_property
    def recording(self):
        return RecordingController()

    @lazy_property
    def call(self):
        return CallController()

    @lazy_property
    def carrier(self):
        return CarrierController()


    def __init__(self, 
                 basic_auth_user_name = None,
                 basic_auth_password = None):

        Configuration.basic_auth_user_name = basic_auth_user_name
        Configuration.basic_auth_password = basic_auth_password


