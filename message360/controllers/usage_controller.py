# -*- coding: utf-8 -*-

"""
    message360.controllers.usage_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 12/02/2016
"""

from .base_controller import *

class UsageController(BaseController):

    """A Controller to access Endpoints in the message360 API."""

    def create_list_usage(self,
                          options=dict()):
        """Does a POST request to /usage/listusage.{ResponseType}.

        Get all usage 

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    product_code -- ProductCode -- Product Code
                    start_date -- string -- Start Usage Date
                    end_date -- string -- End Usage Date
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
        self.validate_parameters(product_code = options.get("product_code"),
                                 start_date = options.get("start_date"),
                                 end_date = options.get("end_date"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/usage/listusage.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ProductCode': options.get('product_code', None),
            'startDate': options.get('start_date', None),
            'endDate': options.get('end_date', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body


