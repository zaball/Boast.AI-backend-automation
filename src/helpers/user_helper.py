from boast_api_test.src.Utilities.genericUtilities import generate_random_user_email
from boast_api_test.src.Utilities.requestsUtility import RequestUtility
import pdb


class CreateUserHelper(object):

    def __init__(self):
        self.requests_utility = RequestUtility()

    def call_create_users(self, email=None, **kwargs):

        if not email:
            email = generate_random_user_email()
            email = email['email']

        payload = dict()
        payload['email'] = email
        payload.update(kwargs)

        create_user_json = self.requests_utility.post('api/users/user/', payload=payload,
                                                      expected_status_code=201)
        return create_user_json

    def get_user_by_id(self, id_rand_user):
        return self.requests_utility.get(f"api/users/user/{id_rand_user}/")


