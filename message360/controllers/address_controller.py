# -*- coding: utf-8 -*-

"""
    message360.controllers.address_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 12/08/2016
"""

from .base_controller import *

class AddressController(BaseController):

    """A Controller to access Endpoints in the message360 API."""
    

    def create_address(self,
                       options=dict()):
        """Does a POST request to /address/createaddress.{ResponseType}.

        To add an address to your address book, you create a new address
        object. You can retrieve and delete individual addresses as well as
        get a list of addresses. Addresses are identified by a unique random
        ID.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    name -- string -- Name of user
                    address -- string -- Address of user.
                    country -- string -- Must be a 2 letter country short-name
                        code (ISO 3166)
                    state -- string -- Must be a 2 letter State eg. CA for US.
                        For Some Countries it can be greater than 2 letters.
                    city -- string -- City Name.
                    zip -- string -- Zip code of city.
                    description -- string -- Description of addresses.
                    email -- string -- Email Id of user.
                    phone -- string -- Phone number of user.
                    response_type -- string -- Response Type Either json or
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
        self.validate_parameters(name = options.get("name"),
                                 address = options.get("address"),
                                 country = options.get("country"),
                                 state = options.get("state"),
                                 city = options.get("city"),
                                 zip = options.get("zip"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/address/createaddress.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'name': options.get('name', None),
            'address': options.get('address', None),
            'country': options.get('country', None),
            'state': options.get('state', None),
            'city': options.get('city', None),
            'zip': options.get('zip', None),
            'description': options.get('description', None),
            'email': options.get('email', None),
            'phone': options.get('phone', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_delete_address(self,
                              options=dict()):
        """Does a POST request to /address/deleteaddress.{ResponseType}.

        To delete Address to your address book

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    addressid -- string -- The identifier of the address to be
                        deleted.
                    response_type -- string -- Response type either json or
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
        self.validate_parameters(addressid = options.get("addressid"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/address/deleteaddress.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'addressid': options.get('addressid', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_verify_address(self,
                              options=dict()):
        """Does a POST request to /address/verifyaddress.{ResponseType}.

        Validates an address given.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    addressid -- string -- The identifier of the address to be
                        verified.
                    response_type -- string -- Response type either JSON or
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
        self.validate_parameters(addressid = options.get("addressid"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/address/verifyaddress.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'addressid': options.get('addressid', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_list_address(self,
                            options=dict()):
        """Does a POST request to /address/listaddress.{ResponseType}.

        List All Address 

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- int -- Return requested # of items starting the
                        value, default=0, must be an integer
                    page_size -- int -- How many results to return,
                        default=10, max 100, must be an integer
                    address_id -- string -- addresses Sid
                    date_created -- string -- date created address.
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

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/address/listaddress.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': options.get('page', None),
            'pageSize': options.get('page_size', None),
            'addressId': options.get('address_id', None),
            'dateCreated': options.get('date_created', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_view_address(self,
                            options=dict()):
        """Does a POST request to /address/viewaddress.{ResponseType}.

        View Address Specific address Book by providing the address id

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    address_id -- string -- The identifier of the address to
                        be retrieved.
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
        self.validate_parameters(address_id = options.get("address_id"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/address/viewaddress.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'addressId': options.get('address_id', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body
