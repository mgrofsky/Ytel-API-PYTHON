# -*- coding: utf-8 -*-

"""
   message360.exceptions.api_exception

   This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ) on 11/04/2016
"""

class APIException(Exception):

    """Class that handles HTTP Exceptions when fetching API Endpoints.
    
    Attributes:
		response_code (int): The status code of the response.
        context (HttpContext): The HttpContext of the API call.
    
    """

    def __init__(self,
                 reason,
                 context):
        """Constructor for the APIException class
        
        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.            
            context (HttpContext): The HttpContext of the API call.
        
        """
        super(APIException, self).__init__(reason)
        self.context = context
        self.response_code = context.response.status_code