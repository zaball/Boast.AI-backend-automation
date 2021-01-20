import pytest
import json
import requests
import pdb
import jsonpath
from requests.auth import HTTPBasicAuth
import django
from selenium.webdriver import Chrome
from boast_api_test.tests.data_practice import credentials


@pytest.mark.practice_01
def test_with_basic_authentication():
    response = requests.get('http://badger.boast.net:8080/api/users/user/', auth=credentials)
    assert response.status_code == 200
    # print(credentials)
    # print(response.text)


@pytest.mark.practice_02
def test_using_post_to_create_user():
    file = open('/home/adi/Boast/boast_api_test/tests/create_user.json', 'r')
    json_read = file.read()
    requests_json = json.loads(json_read)
    url = 'http://badger.boast.net:8080/api/users/user/'
    post_response = requests.post(url, json=requests_json, auth=credentials)
    assert post_response.status_code == 201
    # print(post_response.content)
    # pdb.set_trace()


@pytest.mark.practice_03
def test_get_request():
    response_auth_page = requests.get(url='http://id.boast.net:8080/auth')
    # print(response_auth_page.content)
    get_client_id = requests.get(url='http://id.boast.net:8080/api/apputils/config/get_google_client_id/')
    print(get_client_id.content)
    print(get_client_id.headers)
    # fetch response headers
    print(get_client_id.headers.get('content-type'))
    print(get_client_id.headers.get('Server'))
    # fetch response cookies
    print(get_client_id.cookies)
    print(get_client_id.encoding)
    print(get_client_id.elapsed)
    # validate status code
    s_code = get_client_id.status_code
    assert get_client_id.status_code == 200, f'Expected status code {s_code} and got another'
    cookies = get_client_id.cookies


@pytest.mark.practice_04
def test_parse_to_json_format():
    response = requests.get(url='http://badger.boast.net:8080/api/users/user/', auth=credentials)
    # print((response.json()))
    print('=======================')
    # print(json.loads(response.text))
    # fetch value using json path
    json_response = json.loads(response.text)
    email = jsonpath.jsonpath(json_response, 'json_response')
    print(json_response[1]['email'])
    # pdb.set_trace()
    assert json_response[1]['email'] == 'aabonei@boastcapital.com'
    print(json_response[0])
    for i in range(0, 10):
        print(json_response[i]['first_name'])
        print(json_response[i]['last_name'])
        print(json_response[i]['email'])
        print(json_response[i]['id'])


@pytest.mark.practice_05
def test_delete_user():
    response = requests.get(url='http://badger.boast.net:8080/api/users/user/', auth=credentials)
    assert response.status_code == 200
    delete_user = requests.delete(url='http://badger.boast.net:8080/api/users/user/14/', auth=credentials)
    # assert delete_user.status_code == 204


@pytest.mark.practice_06
def test_update_user_info():
    file = open('/home/adi/Boast/boast_api_test/tests/create_user.json', 'r')
    json_read = file.read()
    request_json = json.loads(json_read)
    response = requests.put(url='http://badger.boast.net:8080/api/users/user/12/', json=request_json, auth=credentials)


# practice front end testing
@pytest.mark.practice_07
def test_pytests_with_selenium_and_chromedriver():
    path = '/home/adi/Boast/chromedriver'
    driver = Chrome(executable_path=path)
    driver.get('http://id.boastlabs.com/auth')
    driver.maximize_window()


# practice fixtures
@pytest.fixture(scope='module')
def set_path():
    global driver
    path = '/home/adi/Boast/chromedriver'
    driver = Chrome(executable_path=path)
    driver.maximize_window()
    yield
    driver.close()


@pytest.mark.practice_08
def test_open_boastlabs_auth(set_path):
    driver.get('http://id.boastlabs.com/auth')


@pytest.mark.practice_08
def test_open_boast_net_auth(set_path):
    driver.get('http://id.boast.net:8080/auth')


@pytest.mark.skip
@pytest.mark.practice_08
def test_open_boast_ai_auth(set_path):
    driver.get('https://id.boast.ai/auth')

# use '-k <test_name> <tests folder>' to select specific test case!


@pytest.mark.practice_09
def test_create_user():
    file = open('/home/adi/Boast/boast_api_test/tests/create_user.json', 'r')
    json_file = json.loads(file.read())
    response = requests.post('http://badger.boast.net:8080/api/users/user/', json=json_file, auth=credentials)
    assert response.status_code == 201


@pytest.mark.practice_10
def test_get_user_data():
    response = requests.get('http://badger.boast.net:8080/api/users/user/15/', auth=credentials)
    print(response.json())
    assert response.status_code == 200
    json_response = json.loads(response.text)
    # another way of writhing the above line:
    # json_response = response.json()
    id_user = jsonpath.jsonpath(json_response, 'id')
    assert id_user[0] == 15
    assert response.url == 'http://badger.boast.net:8080/api/users/user/15/'


@pytest.mark.practice_11
def test_update_user_data():
    file = open('/home/adi/Boast/boast_api_test/tests/create_user.json', 'r')
    json_file = json.loads(file.read())
    response = requests.put('http://badger.boast.net:8080/api/users/user/15/', json=json_file, auth=credentials)
    # pdb.set_trace()
    assert response.status_code == 200


@pytest.mark.practice_12
def test_delete_user():
    response = requests.delete('http://badger.boast.net:8080/api/users/user/14/', auth=credentials)
    assert response.status_code == 204
    response = requests.delete('http://badger.boast.net:8080/api/users/user/12/', auth=credentials)
    assert response.status_code == 204
    response = requests.delete('http://badger.boast.net:8080/api/users/user/13/', auth=credentials)
    assert response.status_code == 204






