import logging as logger
import pytest


def test_health_check_1():
    logger.info("Just running health check 1")
    print("hello")


def test_login_page_example_1():
    print("Login with valid user")
    print("function 1")


def test_login_wrong_pass():
    print("Login with wrong password")
    print("function 2")


def test_fail_example():
    assert 1 == 2, 'One is not two'


class TestCheckout(object):

    def test_checkout_as_guest(self):
        print("checkout as guest")
        print("111111")

    def test_checkout_user_example(self):
        print("checkout as user")
        print('222222')


# pytestmark = pytest.mark.fe


@pytest.fixture(scope='module')
def my_setup():
    print("")
    print("<<<<my setup>>>>")
    return {'id': 20, 'name': 'Adrian'}


# @pytest.mark.smoke
@pytest.mark.ll
def test_login_valid_user(my_setup):
    print("")
    print("aaaaaaaaa - valid user")
    print("Name: {}".format(my_setup.get('name')))


@pytest.mark.regression
def test_login_invalid_user(my_setup):
    print('invalid user')


@pytest.mark.ll
class TestFixture(object):

    def test_fixture1(self, my_setup):
        print("test if it works")

