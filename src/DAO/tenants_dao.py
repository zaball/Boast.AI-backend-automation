# dao = data access object
from boast_api_test.src.Utilities.db_utility import DBUtility
import pdb
import random


class TenantsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_tenant_from_db(self, quantity=1):
        sql = f"SELECT * FROM badger.tenants_tenant"
        rs_sql = self.db_helper.execute_select_query(sql)

        return random.sample(rs_sql, int(quantity))

    def get_tenant_by_id(self, tenant_id):
        sql = f"SELECT * FROM badger.tenants_tenant WHERE ID = {tenant_id}"

        return self.db_helper.execute_select_query(sql)



