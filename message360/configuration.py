# -*- coding: utf-8 -*-

"""
   message360.configuration

   This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io )
"""
from .api_helper import APIHelper

class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
	are accessible without instance creation.

    """

    # An enum for SDK environments
    class Environment(object):
        # Our message360 production environment.  This is our latest stable release.
        PRODUCTION = 0
        # Pre-Production environment used to test your code in our beta systems.  There is a good chance nothing will work here.  Don't use it unless instructed by our staff.
        PREPRODUCTION = 1
        # Internal development testing.  This configuration of the API is not available to the public.
        DEVELOPMENT = 2

    # An enum for API servers
    class Server(object):
        DEFAULT = 0

    # The environment in which the SDK is running
    environment = Environment.PRODUCTION

    # The username to use with basic authentication
    # TODO: Set an appropriate value
    basic_auth_user_name = "TODO: Replace"

    # The password to use with basic authentication
    # TODO: Set an appropriate value
    basic_auth_password = "TODO: Replace"

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.DEFAULT: 'https://api.message360.com/api/v2',
        },
        Environment.PREPRODUCTION: {
            Server.DEFAULT: 'https://api-preprod.message360.com/api/v2',
        },
        Environment.DEVELOPMENT: {
            Server.DEFAULT: 'https://lara-dev.message360.com/api/v2',
        },
    }

    @classmethod
    def get_base_uri(cls, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the server.

        Args:
            server (Configuration.Server): The server enum for which the base URI is required.

        Returns:
            String: The base URI.

        """
        parameters = {
        }
        return APIHelper.append_url_with_template_parameters(cls.environments[cls.environment][server], parameters)
