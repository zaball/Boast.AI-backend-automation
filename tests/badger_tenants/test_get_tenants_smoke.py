import pytest
from boast_api_test.src.Utilities.requestsUtility import RequestUtility
import logging as logger
from boast_api_test.src.DAO.tenants_dao import TenantsDAO
from boast_api_test.src.helpers.tenant_helper import GetTenantHelper
import pdb

py_mark = [pytest.mark.tenants, pytest.mark.smoke]


@pytest.mark.tenants
@pytest.mark.smoke
@pytest.mark.tcid04
def test_get_all_tenants():
    logger.info('Fetch and display all boast tenants: ')
    req_helper = RequestUtility()
    rs_api = req_helper.get('api/tenants/tenant/')

    assert rs_api, f"Response of the list 'all tenants' is empty."


@pytest.mark.tenants
@pytest.mark.smoke
@pytest.mark.tcid07
def test_get_tenant_by_id():
    logger.info('Fetch tenant by random ID: ')

    # get a tenant (test data) from db
    random_tenant = TenantsDAO().get_random_tenant_from_db(1)
    rand_tenant_id = random_tenant[0]['id']

    # make the call
    tenant_helper = GetTenantHelper()
    rs_api = tenant_helper.get_tenant_by_id(rand_tenant_id)

    # verify the response
    db_name = random_tenant[0]['db_name']
    api_name = rs_api['db_name']
    assert db_name == api_name, f"Get tenant by 'id' returned wrong tenant. " \
                                f"ID: {rand_tenant_id}, DB Name: {db_name}, API Name: {api_name}."

    db_name_domain = random_tenant[0]['domain']
    api_name_domain = rs_api['domain']
    assert db_name_domain == api_name_domain, f"Get tenant by 'id' returned wrong tenant. ID: {rand_tenant_id}," \
                                              f"DB Name: {db_name_domain}, API Name: {api_name_domain}."

    db_name_status = random_tenant[0]['status']
    api_name_status = rs_api['status']
    assert db_name_status == api_name_status, f"Get tenant by 'id' returned wrong tenant. ID: {rand_tenant_id}, " \
                                              f"DB Name: {db_name_status}, API Name: {api_name_status}."
    db_prov_state = random_tenant[0]['provisioned']
    api_prov_state = rs_api['provisioned']
    assert db_prov_state == api_prov_state, f"Get tenant by 'id' returned wrong tenant. ID: {rand_tenant_id}, " \
                                            f"DB Name: {db_prov_state}, API Name: {api_prov_state}."
    # pdb.set_trace()
