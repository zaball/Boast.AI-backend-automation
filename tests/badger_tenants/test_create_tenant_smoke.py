from boast_api_test.src.Utilities.genericUtilities import generate_random_string
from boast_api_test.src.helpers.tenant_helper import GetTenantHelper
from boast_api_test.src.DAO.tenants_dao import TenantsDAO
from boast_api_test.src.Utilities.requestsUtility import RequestUtility
import pytest
import pdb
import logging as logger

py_mark = [pytest.mark.tenants, pytest.mark.smoke]


@pytest.mark.tenants
@pytest.mark.smoke
@pytest.mark.tcid09
def test_create_tenant():
    logger.info("Test: Create new tenant in badger")

    # generate data
    payload = dict()
    payload['admin'] = 2  # 2 is admin_id for adiAdmin
    payload['admin_name'] = 'adiAdmin'
    payload['name'] = generate_random_string()
    payload['domain'] = generate_random_string(5)
    payload['provisioned'] = False
    payload['status'] = 'ACTIVE'

    # make the call
    tenant_rs = GetTenantHelper().call_create_tenant(payload)

    # verify the response is not empty
    assert tenant_rs, f"Create tenant API response is empty. Payload: {payload}"
    assert tenant_rs['name'] == payload['name'], f"Create tenant API call response has an unexpected name. " \
                                                 f" Expected: {payload['name']}, Actual: {tenant_rs['name']}"
    assert tenant_rs['domain'] == payload['domain'], f"Create tenant API call response has an unexpected domain. " \
                                                     f" Expected: {payload['domain']}, Actual: {tenant_rs['domain']}"
    assert tenant_rs['admin'] == payload['admin'], f"Create tenant API call response has an unexpected admin. " \
                                                   f" Expected: {payload['admin']}, Actual: {tenant_rs['admin']}"
    assert tenant_rs['admin_name'] == payload['admin_name'], f"Create tenant API call response has an unexpected " \
                                                             f"admin_name. Expected: {payload['admin_name']}, " \
                                                             f"Actual: {tenant_rs['admin_name']}"
    assert tenant_rs['provisioned'] == payload[
        'provisioned'], f"Create tenant API call response has an unexpected provisioned state. " \
                        f" Expected: {payload['provisioned']}, Actual: {tenant_rs['provisioned']}"
    assert tenant_rs['status'] == payload['status'], f"Create tenant API call response has an unexpected status. " \
                                                     f" Expected: {payload['status']}, Actual: {tenant_rs['status']}"

    # verify the product exists in db
    tenant_id = tenant_rs['id']
    db_tenant = TenantsDAO().get_tenant_by_id(tenant_id)

    assert payload['name'] == db_tenant[0]['name'], f"Create tenant in DB does not match title in API response. " \
                                                    f"DB: {db_tenant['name']}, API: {payload['name']}"
    assert payload['domain'] == db_tenant[0]['domain'], f"Create tenant in DB does not match title in API response. " \
                                                        f"DB: {db_tenant['domain']}, API: {payload['domain']}"
    assert payload['provisioned'] == db_tenant[0][
        'provisioned'], f"Create tenant in DB does not match title in API response. " \
                        f"DB: {db_tenant['provisioned']}, API: {payload['provisioned']}"
    assert payload['status'] == db_tenant[0]['status'], f"Create tenant in DB does not match title in API response. " \
                                                        f"DB: {db_tenant['status']}, API: {payload['status']}"

    # pdb.set_trace()


@pytest.mark.tenants
@pytest.mark.smoke
@pytest.mark.tcid10
def test_create_tenant_fail_for_existing_domain(rs_json=None):
    # get existing domain from DB
    tenant_dao = TenantsDAO()
    existing_tenant = tenant_dao.get_random_tenant_from_db()
    existing_domain = existing_tenant[0]['domain']
    existing_name = existing_tenant[0]['name']

    # make API call
    tenant_object = RequestUtility()
    payload = {'domain': existing_domain, 'admin': 2, 'admin_name': 'adiAdmin', 'name': existing_name}

    tenant_api_info = tenant_object.post(endpoint='api/tenants/tenant/', payload=payload, expected_status_code=400)

    # verify the response
    error_message = "['Client with this Subdomain already exists.']"

    assert str(tenant_api_info['domain']) == error_message, f"Expected: {error_message}" \
                                                            f" Actual: {str(tenant_api_info['domain'])} "

