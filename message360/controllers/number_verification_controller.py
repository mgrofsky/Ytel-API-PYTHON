# -*- coding: utf-8 -*-

"""
    message360.controllers.number_verification_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 12/12/2016
"""

from .base_controller import *

class NumberVerificationController(BaseController):

    """A Controller to access Endpoints in the message360 API."""
    

    def create_verify_number(self,
                             options=dict()):
        """Does a POST request to /verifycallerid/verifynumber.{ResponseType}.

        Number Verification

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    phonenumber -- string -- TODO: type description here.
                        Example: 
                    mtype -- string -- TODO: type description here. Example: 
                    response_type -- string -- Response Type either json or
                        xml

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(phonenumber = options.get("phonenumber"),
                                 mtype = options.get("mtype"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/verifycallerid/verifynumber.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'phonenumber': options.get('phonenumber', None),
            'type': options.get('mtype', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body
