from boast_api_test.src.Utilities.genericUtilities import generate_random_email_and_password
from boast_api_test.src.Utilities.requestsUtility import RequestUtility
import pdb


class CreateUserHelper(object):

    def __init__(self):
        self.requests_utility = RequestUtility()

    def create_users(self, email=None, password=None, **kwargs):

        if not email:
            email_and_password = generate_random_email_and_password()
            email = email_and_password['email']
        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        create_user_json = self.requests_utility.post('api/users/user/', payload=payload,
                                                      expected_status_code=201)
        return create_user_json



