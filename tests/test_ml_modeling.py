import json
import requests
import pytest
import jsonpath
from boast_api_test.tests.data_practice import credentials
import pdb


@pytest.mark.ml_test01
def test_post_on_github_system():
    response1 = requests.get('http://rod20190610.boastlabs.com/api/client/fiscalperiod/3/set_session_fp/',
                             auth=credentials)
    # id_fiscal_period = jsonpath.jsonpath(response1.json(), 'id')
    # file = open('/home/adi/Boast/boast_api_test/tests/FP_fiscal_period.json', 'r')
    # json_file = json.loads(file.read())
    # response = requests.post('http://rod20190610.boastlabs.com/api/integrations/remotedata/enqueue_ml_modeling/'
    #                          + str(id_fiscal_period[0]) + '/', json=json_file, auth=credentials)
    pdb.set_trace()
    # print(response)
