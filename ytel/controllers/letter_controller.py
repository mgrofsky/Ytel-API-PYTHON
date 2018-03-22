# -*- coding: utf-8 -*-

"""
    ytel.controllers.letter_controller

    This file was automatically generated for ytel by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class LetterController(BaseController):

    """A Controller to access Endpoints in the ytel API."""


    def view_letter(self,
                    options=dict()):
        """Does a POST request to /letter/viewletter.{ResponseType}.

        Retrieve a letter object by its LetterSid.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    lettersid -- string -- The unique identifier for a letter
                        object.
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
        self.validate_parameters(lettersid=options.get("lettersid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/letter/viewletter.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'lettersid': options.get('lettersid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_letter(self,
                      options=dict()):
        """Does a POST request to /letter/create.{ResponseType}.

        Create, print, and mail a letter to an address. The letter file must
        be supplied as a PDF or an HTML string.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    to -- string -- The AddressId or an object structured when
                        creating an address by addresses/Create.
                    mfrom -- string -- The AddressId or an object structured
                        when creating an address by addresses/Create.
                    attachbyid -- string -- Set an existing letter by
                        attaching its LetterId.
                    file -- string -- File can be a 8.5"x11" PDF uploaded file
                        or URL that links to a file.
                    color -- string -- Specify if letter should be printed in
                        color.
                    response_type -- string -- Response Type either json or
                        xml
                    description -- string -- A description for the letter.
                    extraservice -- string -- Add an extra service to your
                        letter. Options are "certified" or "registered".
                        Certified provides tracking and delivery confirmation
                        for domestic destinations and is an additional $5.00.
                        Registered provides tracking and confirmation for
                        international addresses and is an additional $16.50.
                    doublesided -- string -- Specify if letter should be
                        printed on both sides.
                    template -- string -- Boolean that defaults to true. When
                        set to false, this specifies that your letter does not
                        follow the m360 address template. In this case, a
                        blank address page will be inserted at the beginning
                        of your file and you will be charged for the extra
                        page.
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
        self.validate_parameters(to=options.get("to"),
                                 mfrom=options.get("mfrom"),
                                 attachbyid=options.get("attachbyid"),
                                 file=options.get("file"),
                                 color=options.get("color"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/letter/create.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'to': options.get('to', None),
            'from': options.get('mfrom', None),
            'attachbyid': options.get('attachbyid', None),
            'file': options.get('file', None),
            'color': options.get('color', None),
            'description': options.get('description', None),
            'extraservice': options.get('extraservice', None),
            'doublesided': options.get('doublesided', None),
            'template': options.get('template', None),
            'htmldata': options.get('htmldata', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_letters(self,
                     options=dict()):
        """Does a POST request to /letter/listsletter.{ResponseType}.

        Retrieve a list of letter objects. The letter objects are sorted by
        creation date, with the most recently created letters appearing
        first.

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
                    lettersid -- string -- The unique identifier for a letter
                        object.
                    date_created -- string -- The date the letter was
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
        _query_builder += '/letter/listsletter.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'lettersid': options.get('lettersid', None),
            'dateCreated': options.get('date_created', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def delete_letter(self,
                      options=dict()):
        """Does a POST request to /letter/delete.{ResponseType}.

        Remove a letter object by its LetterId.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    lettersid -- string -- The unique identifier for a letter
                        object.
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
        self.validate_parameters(lettersid=options.get("lettersid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/letter/delete.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'lettersid': options.get('lettersid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
