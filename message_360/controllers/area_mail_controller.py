# -*- coding: utf-8 -*-

"""
    message_360.controllers.area_mail_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class AreaMailController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def create_area_mail(self,
                         options=dict()):
        """Does a POST request to /areamail/create.{ResponseType}.

        Create a new AreaMail object.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    routes -- string -- List of routes that AreaMail should be
                        delivered to.  A single route can be either a zipcode
                        or a carrier route.List of routes that AreaMail should
                        be delivered to.  A single route can be either a
                        zipcode or a carrier route. A carrier route is in the
                        form of 92610-C043 where the carrier route is composed
                        of 5 numbers for zipcode, 1 letter for carrier route
                        type, and 3 numbers for carrier route code. Delivery
                        can be sent to mutliple routes by separating them with
                        a commas. Valid Values: 92656, 92610-C043
                    attachbyid -- string -- Set an existing areamail by
                        attaching its AreamailId.
                    front -- string -- The front of the AreaMail item to be
                        created. This can be a URL, local file, or an HTML
                        string. Supported file types are PDF, PNG, and JPEG.
                        Back required
                    back -- string -- The back of the AreaMail item to be
                        created. This can be a URL, local file, or an HTML
                        string. Supported file types are PDF, PNG, and JPEG.
                    response_type -- string -- Response Type either json or
                        xml
                    description -- string -- A string value to use as a
                        description for this AreaMail item.
                    targettype -- string -- The delivery location type.
                    htmldata -- string -- A string value that contains HTML
                        markup.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(routes=options.get("routes"),
                                 attachbyid=options.get("attachbyid"),
                                 front=options.get("front"),
                                 back=options.get("back"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/areamail/create.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'routes': options.get('routes', None),
            'attachbyid': options.get('attachbyid', None),
            'front': options.get('front', None),
            'back': options.get('back', None),
            'description': options.get('description', None),
            'targettype': options.get('targettype', None),
            'htmldata': options.get('htmldata', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_area_mail(self,
                       options=dict()):
        """Does a POST request to /areamail/view.{ResponseType}.

        Retrieve an AreaMail object by its AreaMailId.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    areamailid -- string -- The unique identifier for an
                        AreaMail object.
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
        self.validate_parameters(areamailid=options.get("areamailid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/areamail/view.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'areamailid': options.get('areamailid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_area_mail(self,
                       options=dict()):
        """Does a POST request to /areamail/lists.{ResponseType}.

        Retrieve a list of AreaMail objects.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response Type either json or
                        xml
                    page -- int -- The page count to retrieve from the total
                        results in the collection. Page indexing starts at 1.
                    pagesize -- int -- The count of objects to return per
                        page.
                    areamailsid -- string -- The unique identifier for an
                        AreaMail object.
                    date_created -- string -- The date the AreaMail was
                        created.

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
        _query_builder += '/areamail/lists.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'areamailsid': options.get('areamailsid', None),
            'dateCreated': options.get('date_created', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def delete_area_mail(self,
                         options=dict()):
        """Does a POST request to /areamail/delete.{ResponseType}.

        Remove an AreaMail object by its AreaMailId.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    areamailid -- string -- The unique identifier for an
                        AreaMail object.
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
        self.validate_parameters(areamailid=options.get("areamailid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/areamail/delete.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'areamailid': options.get('areamailid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
