# -*- coding: utf-8 -*-

"""
    message_360.models.message_360_model

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io )
"""
import message_360.models.message_model

class Message360Model(object):

    """Implementation of the 'Message360' model.

    TODO: type model description here.

    Attributes:
        response_status (int): TODO: type description here.
        message_count (int): TODO: type description here.
        message (MessageModel): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "response_status" : "ResponseStatus",
        "message_count" : "MessageCount",
        "message" : "Message"
    }

    def __init__(self,
                 response_status=None,
                 message_count=None,
                 message=None):
        """Constructor for the Message360Model class"""

        # Initialize members of the class
        self.response_status = response_status
        self.message_count = message_count
        self.message = message


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        response_status = dictionary.get("ResponseStatus")
        message_count = dictionary.get("MessageCount")
        message = message_360.models.message_model.MessageModel.from_dictionary(dictionary.get("Message")) if dictionary.get("Message") else None

        # Return an object of this model
        return cls(response_status,
                   message_count,
                   message)


