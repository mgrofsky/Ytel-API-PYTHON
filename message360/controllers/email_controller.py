# -*- coding: utf-8 -*-

"""
    message360.controllers.email_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 12/08/2016
"""

from .base_controller import *

class EmailController(BaseController):

    """A Controller to access Endpoints in the message360 API."""
    

    def create_delete_invalid(self,
                              options=dict()):
        """Does a POST request to /email/deleteinvalidemail.{ResponseType}.

        This endpoint allows you to delete entries in the Invalid Emails
        list.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    email -- string -- TODO: type description here. Example: 
                    response_type -- string -- TODO: type description here.
                        Example: json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(email = options.get("email"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/email/deleteinvalidemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'email': options.get('email', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_list_blocks(self,
                           options=dict()):
        """Does a POST request to /email/listblockemail.{ResponseType}.

        Outputs email addresses on your blocklist

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    offset -- string -- Where to start in the output list
                    limit -- string -- Maximum number of records to return
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

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/email/listblockemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'offset': options.get('offset', None),
            'limit': options.get('limit', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_list_spam(self,
                         options=dict()):
        """Does a POST request to /email/listspamemail.{ResponseType}.

        List out all email addresses marked as spam

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    offset -- string -- The record number to start the list
                        at
                    limit -- string -- Maximum number of records to return

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
        _query_builder += '/email/listspamemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'offset': options.get('offset', None),
            'limit': options.get('limit', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_list_bounces(self,
                            options=dict()):
        """Does a POST request to /email/listbounceemail.{ResponseType}.

        List out all email addresses that have bounced

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    offset -- string -- The record to start the list at
                    limit -- string -- The maximum number of records to
                        return

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
        _query_builder += '/email/listbounceemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'offset': options.get('offset', None),
            'limit': options.get('limit', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_delete_bounces(self,
                              options=dict()):
        """Does a POST request to /email/deletebouncesemail.{ResponseType}.

        Delete an email address from the bounced address list

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    email -- string -- The email address to remove from the
                        bounce list
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
        self.validate_parameters(email = options.get("email"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/email/deletebouncesemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'email': options.get('email', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_list_invalid(self,
                            options=dict()):
        """Does a POST request to /email/listinvalidemail.{ResponseType}.

        List out all invalid email addresses

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    offet -- string -- Starting record for listing out emails
                    limit -- string -- Maximum number of records to return

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
        _query_builder += '/email/listinvalidemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'offet': options.get('offet', None),
            'limit': options.get('limit', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_list_unsubscribes(self,
                                 options=dict()):
        """Does a POST request to /email/listunsubscribedemail.{ResponseType}.

        List all unsubscribed email addresses

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    offset -- string -- Starting record of the list
                    limit -- string -- Maximum number of records to be
                        returned

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
        _query_builder += '/email/listunsubscribedemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'offset': options.get('offset', None),
            'limit': options.get('limit', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_delete_unsubscribes(self,
                                   options=dict()):
        """Does a POST request to /email/deleteunsubscribedemail.{ResponseType}.

        Delete emails from the unsubscribe list

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    email -- string -- The email to remove from the
                        unsubscribe list
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
        self.validate_parameters(email = options.get("email"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/email/deleteunsubscribedemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'email': options.get('email', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def add_unsubscribes(self,
                         options=dict()):
        """Does a POST request to /email/addunsubscribesemail.{ResponseType}.

        Add an email to the unsubscribe list

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    email -- string -- The email to add to the unsubscribe
                        list
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
        self.validate_parameters(email = options.get("email"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/email/addunsubscribesemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'email': options.get('email', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_delete_block(self,
                            options=dict()):
        """Does a POST request to /email/deleteblocksemail.{ResponseType}.

        Deletes a blocked email

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    email -- string -- Email address to remove from block
                        list
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
        self.validate_parameters(email = options.get("email"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/email/deleteblocksemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'email': options.get('email', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_delete_spam(self,
                           options=dict()):
        """Does a POST request to /email/deletespamemail.{ResponseType}.

        Deletes a email address marked as spam from the spam list

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    email -- string -- Email address
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
        self.validate_parameters(email = options.get("email"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/email/deletespamemail.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'email': options.get('email', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body

    def create_send_email(self,
                          options=dict()):
        """Does a POST request to /email/sendemails.{ResponseType}.

        Send out an email

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    to -- string -- The to email address
                    mfrom -- string -- The from email address
                    mtype -- SendEmailAs -- email format type, html or text
                    subject -- string -- Email subject
                    message -- string -- The body of the email message
                    cc -- string -- CC Email address
                    bcc -- string -- BCC Email address
                    attachment -- string -- File to be attached.File must be
                        less than 7MB.
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
        self.validate_parameters(to = options.get("to"),
                                 mfrom = options.get("mfrom"),
                                 mtype = options.get("mtype"),
                                 subject = options.get("subject"),
                                 message = options.get("message"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/email/sendemails.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'to': options.get('to', None),
            'from': options.get('mfrom', None),
            'type': options.get('mtype', None),
            'subject': options.get('subject', None),
            'message': options.get('message', None),
            'cc': options.get('cc', None),
            'bcc': options.get('bcc', None),
            'attachment': options.get('attachment', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body
