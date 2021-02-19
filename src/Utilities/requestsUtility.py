from boast_api_test.src.configs.hosts_config import API_HOSTS
import requests
import os
import json
# from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1
from boast_api_test.tests.data_practice import credentials
import logging as logger


class RequestUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Wrong status code. Expected" \
                 f" {self.expected_status_code}. Actual status code: {self.status_code}. URL: {self.url}." \
                 f"Response jsone: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {'Content-Type': 'application/json'}

        self.url = self.base_url + endpoint

        rs_api = requests.post(self.url, data=json.dumps(payload), headers=headers, auth=credentials)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        # no longer needed
        # assert self.status_code == int(expected_status_code),\
        #     f'Expected status code {expected_status_code} ' \
        #     f'but got ' f'{self.status_code}'
        logger.debug(f"POST API response: {self.rs_json}")

        return self.rs_json

        # import pdb; pdb.set_trace()

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {'Content-Type': 'application/json'}

        self.url = self.base_url + endpoint

        rs_api = requests.get(self.url, headers=headers, auth=credentials)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"GET API response: {self.rs_json}")
        return self.rs_json
