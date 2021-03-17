import pytest
from boast_api_test.src.Utilities.requestsUtility import RequestUtility
import logging as logger
import pdb
from boast_api_test.src.DAO.users_dao import UsersDAO
from boast_api_test.src.helpers.user_helper import CreateUserHelper

pytestmark = [pytest.mark.users, pytest.mark.smoke]


@pytest.mark.tcid03
def test_get_all_users():
    logger.info('Fetch and display all boast users: ')
    req_helper = RequestUtility()
    rs_api = req_helper.get('api/users/user/')

    assert rs_api, f"Response of the list 'all users' is empty. "


@pytest.mark.tcid08
def test_get_user_by_id():
    logger.info('Fetch user by random ID: ')

    # get a user (test data) from db
    random_user = UsersDAO().get_random_user_from_db(1)
    rand_user_id = random_user[0]['user_id']

    # make the API call
    user_helper = CreateUserHelper()
    rs_api = user_helper.get_user_by_id(rand_user_id)

    # verify the response
    db_name_email = random_user[0]['email']
    api_name_email = rs_api['email']
    assert db_name_email == api_name_email, f"Get user by 'id' returned wrong user. ID: {rand_user_id}," \
                                            f"DB Name: {db_name_email}, API Name: {api_name_email}."

    db_name_nick_name = random_user[0]['nick_name']
    api_name_nick_name = rs_api['nick_name']
    assert db_name_nick_name == api_name_nick_name, f"Get user by 'id' returned wrong user. ID: {rand_user_id}," \
                                                    f"DB Name: {db_name_nick_name}, API Name: {api_name_nick_name}."

    db_name_mfa_state = random_user[0]['mfa_enabled']
    api_name_mfa_state = rs_api['mfa_enabled']
    assert db_name_mfa_state == api_name_mfa_state, f"Get user by 'id' returned wrong user. ID: {rand_user_id}," \
                                                    f"DB Name: {db_name_mfa_state}, API Name: {api_name_mfa_state}."

    db_name_phone = random_user[0]['phone']
    api_name_phone = rs_api['phone']
    assert db_name_phone == api_name_phone, f"Get user by 'id' returned wrong user. ID: {rand_user_id}," \
                                            f"DB Name: {db_name_phone}, API Name: {api_name_phone}."

    # pdb.set_trace()
