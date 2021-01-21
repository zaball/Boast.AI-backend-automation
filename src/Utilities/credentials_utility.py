import os


class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_db_credentials():
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception('The DB user and password should be stored as environment variables: "DB_USER" and'
                            '"DB_PASSWORD".')
        else:
            return {'db_user': db_user, 'db_password': db_password}
