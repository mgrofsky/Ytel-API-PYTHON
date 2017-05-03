# -*- coding: utf-8 -*-

"""
    message_360.models.short_code_test_response_model

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io )
"""
import message_360.models.message_360_model

class ShortCodeTestResponseModel(object):

    """Implementation of the 'ShortCode Test Response' model.

    TODO: type model description here.

    Attributes:
        message_360 (Message360Model): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message_360" : "Message360"
    }

    def __init__(self,
                 message_360=None):
        """Constructor for the ShortCodeTestResponseModel class"""

        # Initialize members of the class
        self.message_360 = message_360


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
        message_360 = message_360.models.message_360_model.Message360Model.from_dictionary(dictionary.get("Message360")) if dictionary.get("Message360") else None

        # Return an object of this model
        return cls(message_360)


