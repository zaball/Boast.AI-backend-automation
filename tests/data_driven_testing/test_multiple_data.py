import pytest
import requests
import json
import openpyxl
from boast_api_test.tests.data_practice import credentials
from boast_api_test.tests.data_driven_testing import library


# complex way of adding multiple data
@pytest.mark.multiple_data01
def test_create_multiple_users():
    # API
    file = open('/home/adi/Boast/boast_api_test/tests/data_driven_testing/create_multiple_users.json')
    json_file = json.loads(file.read())

    obj = library.Common('/home/adi/Boast/boast_api_test/tests/data_driven_testing/multiple_users.xlsx', 'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    key_list = obj.fetch_key_names()

    for i in range(2, row+1):
        updated_json_request = obj.update_request_with_data(i, json_file, key_list)
        response = requests.post('http://badger.boast.net:8080/api/users/user/', json=updated_json_request,
                                 auth=credentials)
        assert response.status_code == 201

