# dao = data access object
from boast_api_test.src.Utilities.db_utility import DBUtility
import pdb


class UsersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_user_by_email(self, email):

        sql = f"SELECT * FROM badger.account_emailaddress AS address INNER JOIN badger.users_profile AS users " \
              f"ON address.user_id = users.user_id WHERE email = '{email}';"
        rs_sql = self.db_helper.execute_select_query(sql)

        # pdb.set_trace()
