import pytest
import logging as logger
from boast_api_test.src.Utilities.genericUtilities import generate_random_user_email
from boast_api_test.src.helpers.user_helper import CreateUserHelper
from boast_api_test.src.DAO.users_dao import UsersDAO
from boast_api_test.src.Utilities.requestsUtility import RequestUtility
import pdb

pytestmark = [pytest.mark.users, pytest.mark.smoke]


@pytest.mark.tcid01
def test_create_user():
    logger.info("Test: Create new user in badger")
    # logger.debug("Test: Create new user in badger with email and pass")

    # generate data
    rand_info = generate_random_user_email()
    # logger.info(rand_info)
    email = rand_info['email']

    # make API call
    user_object = CreateUserHelper()
    user_api_info = user_object.call_create_users(email=email, nick_name='nickname', roles=['tenant_user']
                                                  , mfa_enabled=True, first_name='First User', last_name='Last',
                                                  username=email, calendar_url='http://badger.boast.net:8080')

    # verify the response
    assert user_api_info['email'] == email, f"Create customer api returned wrong email address. " \
                                            f"Email: {email}"
    assert user_api_info['nick_name'] == 'nickname', f"Create customer api returned wrong nick name. Nick Name: " \
                                                     f"{'nickname'}"
    assert user_api_info['roles'] == ['tenant_user'], f"Create customer api returned wrong role. " \
                                                      f"Role: {['tenant_user']}"
    assert user_api_info['mfa_enabled'] == True, f"Create customer api returned wrong mfa_enabled state. " \
                                                 f"MFA state: {True}"
    assert user_api_info['first_name'] == 'First User', f"Create customer api returned wrong first name. " \
                                                        f"First Name: {'first_name'}"
    assert user_api_info['last_name'] == 'Last', f"Create customer api returned wrong Last Name. " \
                                                 f"Last Name: {'last_name'}"
    assert user_api_info['username'] == email, f"Create customer api returned wrong username. " \
                                               f"Username: {email}"
    assert user_api_info['calendar_url'] == 'http://badger.boast.net:8080', \
        f"Create customer api returned wrong calendar URL. Calendar URL: {'calendar_url'}"

    # verify info in the database
    user_dao = UsersDAO()
    user_info = user_dao.get_user_by_email(email)

    id_in_api = user_api_info['id']
    id_in_db = user_info[0]['user_id']
    assert id_in_api == id_in_db, f"Create user response 'id' is not the same as 'id' in the database. " \
                                  f"Email: {email}"

    nick_name_in_api = user_api_info['nick_name']
    nick_name_in_db = user_info[0]['nick_name']
    assert nick_name_in_api == nick_name_in_db, f"Create user response 'nick_name' is not the same as 'nick_name' in " \
                                                f"the database. Email: {email}"

    mfa_in_api = user_api_info['mfa_enabled']
    mfa_in_db = user_info[0]['mfa_enabled']
    assert mfa_in_api == mfa_in_db, f"Create user response 'mfa_enabled' is not the same as 'mfa_enabled' in " \
                                    f"the database. Email: {email}"

    # pdb.set_trace()


@pytest.mark.tcid02
def test_create_user_fail_for_existing_email(rs_json=None):
    # get existing email from DB
    user_dao = UsersDAO()
    existing_user = user_dao.get_random_user_from_db()
    existing_email = existing_user[0]['email']
    existing_nick = existing_user[0]['nick_name']
    existing_calendar_url = existing_user[0]['calendar_url']
    existing_mfa = existing_user[0]['mfa_enabled']

    # make API call
    user_object = RequestUtility()
    payload = {'email': existing_email, 'nick_name': existing_nick, 'roles': ['tenant_user'],
               'mfa_enabled': existing_mfa, 'first_name': 'First User', 'last_name': 'Last', 'username': existing_email,
               'calendar_url': existing_calendar_url}
    user_api_info = user_object.post(endpoint='api/users/user/', payload=payload, expected_status_code=400)

    # verify the response
    error_message = "['This field must be unique.']"

    assert str(user_api_info['email']) == error_message, f"Expected: 'This field must be unique.' Actual: " \
                                                         f"{str(user_api_info['email'])} "
    # pdb.set_trace()


    #test test test