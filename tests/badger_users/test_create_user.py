import pytest
import logging as logger
from boast_api_test.src.Utilities.genericUtilities import generate_random_email_and_password
from boast_api_test.src.Utilities.create_user import CreateUserHelper


@pytest.mark.tcid01
def test_create_user():
    logger.info("Test: Create new user in badger with email and password")
    # logger.debug("Test: Create new user in badger")

    rand_info = generate_random_email_and_password()
    # logger.info(rand_info)
    email = rand_info['email']
    password = rand_info['password']

    # create payload
    # payload = {'email': email, 'password': password}
    # logger.info(payload)

    # make API call
    user_object = CreateUserHelper()
    user_api_info = user_object.create_users(email=email, password=password, nick_name='nickname', roles=['tenant_user']
                                             , mfa_enabled=True, first_name='First User', last_name='Last',
                                             username='whatever', calendar_url='http://badger.boast.net:8080')

    # import pdb; pdb.set_trace()
