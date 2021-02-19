from boast_api_test.src.Utilities.requestsUtility import RequestUtility


class GetTenantHelper(object):

    def __init__(self):
        self.request_utility = RequestUtility()

    def get_tenant_by_id(self, tenant_id):
        return self.request_utility.get(f"api/tenants/tenant/{tenant_id}/")

    def call_create_tenant(self, payload):
        return self.request_utility.post('api/tenants/tenant/', payload=payload, expected_status_code=201)






