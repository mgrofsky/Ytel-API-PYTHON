# -*- coding: utf-8 -*-

"""
    message_360.models.errors_model

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io )
"""
import message_360.models.error_model

class ErrorsModel(object):

    """Implementation of the 'Errors' model.

    TODO: type model description here.

    Attributes:
        error (list of ErrorModel): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error" : "Error"
    }

    def __init__(self,
                 error=None):
        """Constructor for the ErrorsModel class"""

        # Initialize members of the class
        self.error = error


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
        error = None
        if dictionary.get("Error") != None:
            error = list()
            for structure in dictionary.get("Error"):
                error.append(message_360.models.error_model.ErrorModel.from_dictionary(structure))

        # Return an object of this model
        return cls(error)


