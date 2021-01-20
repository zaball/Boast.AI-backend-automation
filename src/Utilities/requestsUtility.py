from boast_api_test.src.configs.hosts_config import API_HOSTS
import requests
import os
import json
# from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1


class RequestUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {'Content-Type': 'application/json'}

        url = self.base_url + endpoint

        credentials = ('adrian.abonei.boast@gmail.com', 'suntfericit')

        rs_api = requests.post(url, data=json.dumps(payload), headers=headers, auth=credentials)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code),\
            f'Expected status code {expected_status_code} ' \
            f'but got ' f'{self.status_code}'
        return rs_api.json()

        # import pdb; pdb.set_trace()

    def get(self):
        pass
