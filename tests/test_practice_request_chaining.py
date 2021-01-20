import json
import jsonpath
import pytest
import requests
from boast_api_test.tests.data_practice import credentials


# If all 4 tests are run at once -> create + update + delete user in badger


@pytest.mark.request_chaning_01
def test_add_new_user():
    file = open('/home/adi/Boast/boast_api_test/tests/create_user.json', 'r')
    json_file = json.loads(file.read())
    response = requests.post('http://badger.boast.net:8080/api/users/user/', json=json_file, auth=credentials)
    global id_user
    assert response.status_code == 201
    id_user = jsonpath.jsonpath(response.json(), 'id')


@pytest.mark.request_chaning_01
def test_get_user_details():
    response = requests.get('http://badger.boast.net:8080/api/users/user/' + str(id_user[0]), auth=credentials)
    assert response.status_code == 200
    print(response)


@pytest.mark.request_chaning_01
def test_update_user_details():
    file = open('/home/adi/Boast/boast_api_test/tests/create_user.json', 'r')
    json_file = json.loads(file.read())
    response = requests.put('http://badger.boast.net:8080/api/users/user/' + str(id_user[0]) + '/', json=json_file,
                            auth=credentials)
    assert response.status_code == 200


@pytest.mark.request_chaning_01
def test_delete_user_details():
    response = requests.delete('http://badger.boast.net:8080/api/users/user/' + str(id_user[0]) + '/', auth=credentials)
    assert response.status_code == 204











