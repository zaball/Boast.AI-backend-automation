import pymysql
from boast_api_test.src.Utilities.credentials_utility import CredentialsUtility


class DBUtility(object):

    def __init__(self):
        cred_helper = CredentialsUtility()
        self.cred = cred_helper.get_db_credentials()
        self.host = 'localhost'

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.cred['db_user'], password=self.cred['db_password'],
                                     port=13306)
        return connection

    def execute_select_query(self, sql):
        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
        pass

