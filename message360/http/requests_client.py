# -*- coding: utf-8 -*-

"""
    message360.http.requests_client

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 11/11/2016
"""

import requests

from .http_client import HttpClient
from .http_response import HttpResponse
from .http_method_enum import HttpMethodEnum

class RequestsClient(HttpClient):

    """An implementation of HttpClient that uses Requests as its HTTP Client

    Attributes:
        timeout (int): The default timeout for all API requests.
    
    """

    def __init__(self, timeout):
        """The constructor.

        Args:
            timeout (float): The default global timeout(seconds).

        """
        self.timeout = timeout

    def execute_as_string(self, request):
        """Execute a given HttpRequest to get a string response back
       
        Args:
            request (HttpRequest): The given HttpRequest to execute.
            
        Returns:
            HttpResponse: The response of the HttpRequest.
            
        """	
        response = requests.request(HttpMethodEnum.to_string(request.http_method), 
                                    request.query_url, 
                                    headers=request.headers,
                                    params=request.query_parameters, 
                                    data=request.parameters,
                                    files=request.files,
                                    timeout=self.timeout)

        return self.convert_response(response, False)
    
    def execute_as_binary(self, request):
        """Execute a given HttpRequest to get a binary response back
       
        Args:
            request (HttpRequest): The given HttpRequest to execute.
            
        Returns:
            HttpResponse: The response of the HttpRequest.
            
        """        
        response = requests.request(HttpMethodEnum.to_string(request.http_method), 
                                    request.query_url, 
                                    headers=request.headers,
                                    params=request.query_parameters, 
                                    data=request.parameters, 
                                    files=request.files,
                                    timeout=self.timeout)
                                   
        return self.convert_response(response, True)
    
    def convert_response(self, response, binary):
        """Converts the Response object of the HttpClient into an
        HttpResponse object.
       
        Args:
            response (dynamic): The original response object.
            
        Returns:
            HttpResponse: The converted HttpResponse object.
            
        """
        if binary == True:
            return HttpResponse(response.status_code, response.headers, response.content)
        else:
            return HttpResponse(response.status_code, response.headers, response.text)