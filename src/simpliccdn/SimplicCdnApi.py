# ---------------------------------------------------------------
# Simplic CDN Api for using with Python and IronPython
# Copyright - 2016 @ EDV-Systeme Spiegelburg GmbH
# ---------------------------------------------------------------

import requests
from requests_jwt import JWTAuth
import base64
import uuid

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SimplicCdnApi(object):
    """Contains everything that is needed to work with the simplic cdn restful service"""

    # Login-Status
    NOT_LOGGED_IN = 0
    LOGIN_FAILED = 99
    LOGIN_SUCCESSFULL = 100

    def __init__(self, url):

        # Login-Status
        #    0 - Not logged in
        #   99 - Login failed
        #  100 - Login successfull
        self.login_status = self.NOT_LOGGED_IN
        self.url = url + '/api/' + self.api_version() + '/'

    def login(self, username, password):
        """
        Open a session and requests a JWT. If the login was successfull, the login_status will be set to LOGIN_SUCCESSFULL, if login failed,
        an exception will be thrown and the status will be set to LOGIN_FAILED
        
        Parameter
        ---------
        username (str) : User name
        password (str) : Password
        """

        if not self.is_available():
            raise Exception('Could not access api at: ' + self.url)

        # Request JWT token
        result = requests.post(self.url + '/auth/login', json = { 'userName': username, 'password': password })

        # Check status and token
        if result.status_code == 200:
            print result.json()['Token']
            self.jwt = result.json()['Token']
            self.login_status = self.LOGIN_SUCCESSFULL
        else:
            self.login_status = self.LOGIN_FAILED
            raise Exception('Could not connect to simplic cdn: ' + result.text)

    def ping_req(self):
        """
        Create a get request to the ping api method

        Returns
        -------
        Requests get-result of /cdn/ping
        """
        return requests.get(self.url + '/cdn/ping')

    def ping(self):
        """
        Returns the result of a ping as json/object

        Returns
        -------
        Ping result as json object
        """
        return self.ping_req().json()

    def is_available(self):
        """
        Check whether the cdn is available

        Returns
        -------
        Returns true if the cdn is available
        """
        return self.ping_req().status_code == 200

    def api_version(self):
        """
        Get the currently used api-version

        Returns
        -------
        Api version as string
        """
        return 'v1-0'

    def set_data(self, path, data):
        """
        Save data in the cdn

        Parameter
        --------
        path (str): Path as string
        data (base64): Data as bytearray
        """
        self.assert_login()

        result = requests.post(self.url + '/cdn/set', json = { 'path': path, 'data': data})

        # Check status and token
        if result.status_code == 200:
            return result.text
        else:
            return Exception('Could not set data to simplic cdn: ' + result.text)

    def get_headers(self):
        return {'Authorization': 'Bearer ' + self.jwt}

    def get_data(self, path):

        try:
            self.assert_login()
            result = requests.get(self.url + '/cdn/get?path=' + path, headers = self.get_headers())
        except:
            result = requests.get(self.url + '/cdn/get?path=' + path)

        # Check status and token
        if result.status_code == 200:
            return result.text
        else:
            return Exception('Could not get data from simplic cdn: ' + result.text)

    def assert_login(self):
        if self.login_status != self.LOGIN_SUCCESSFULL:
            raise Exception('Please login before calling this api methods.')