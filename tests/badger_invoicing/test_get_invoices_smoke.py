import pytest
from boast_api_test.src.Utilities.requestsUtility import RequestUtility
import logging as logger
import pdb


@pytest.mark.smoke
@pytest.mark.invoicing
@pytest.mark.tcid05
def test_get_all_invoices():
    logger.info('Fetch and display all existing invoices: ')
    req_helper = RequestUtility()
    rs_api = req_helper.get('api/boast_invoicing/invoices/')

    assert rs_api, f"Response of the list 'all invoices' is empty."
