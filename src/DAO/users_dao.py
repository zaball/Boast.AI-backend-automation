# dao = data access object
from boast_api_test.src.Utilities.db_utility import DBUtility
import pdb
import random


class UsersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_user_by_email(self, email):
        """
        Args: Perform inner join query
        Return: Get the new user email address.
        """

        sql = f"SELECT * FROM badger.account_emailaddress AS mail INNER JOIN badger.users_profile AS user " \
              f"ON mail.user_id = user.user_id WHERE email = '{email}';"
        rs_sql = self.db_helper.execute_select_query(sql)

        return rs_sql

    def get_random_user_from_db(self, quantity=1):

        sql = f"SELECT * FROM badger.account_emailaddress AS mail INNER JOIN badger.users_profile AS user " \
              f"ON mail.user_id = user.user_id;"
        rs_sql = self.db_helper.execute_select_query(sql)

        return random.sample(rs_sql, int(quantity))


