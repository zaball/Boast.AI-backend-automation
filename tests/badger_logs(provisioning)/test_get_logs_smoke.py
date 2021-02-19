import pytest
from boast_api_test.src.Utilities.requestsUtility import RequestUtility
import logging as logger
import pdb


@pytest.mark.smoke
@pytest.mark.logs
@pytest.mark.tcid06
def test_get_all_logs():
    logger.info('Fetch and display all boast logs: ')
    req_helper = RequestUtility()
    rs_api = req_helper.get('api/apputils/backgroundtask/')

    assert rs_api, f"Response of the list 'all logs' is empty. "
