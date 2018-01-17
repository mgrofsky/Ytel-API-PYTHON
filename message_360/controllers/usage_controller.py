# -*- coding: utf-8 -*-

"""
    message_360.controllers.usage_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class UsageController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def list_usage(self,
                   options=dict()):
        """Does a POST request to /usage/listusage.{ResponseType}.

        Retrieve usage metrics regarding your message360 account. The results
        includes inbound/outbound voice calls and inbound/outbound SMS
        messages as well as carrier lookup requests.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    product_code -- ProductCodeEnum -- Filter usage results by
                        product type.
                    start_date -- string -- Filter usage objects by start
                        date.
                    end_date -- string -- Filter usage objects by end date.
                    include_sub_accounts -- string -- Will include all
                        subaccount usage data

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
        _query_builder += '/usage/listusage.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ProductCode': options.get('product_code', None),
            'startDate': options.get('start_date', None),
            'endDate': options.get('end_date', None),
            'IncludeSubAccounts': options.get('include_sub_accounts', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
