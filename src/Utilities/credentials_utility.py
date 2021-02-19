import os


class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_db_credentials():
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception('The DB host, user and password should be stored as environment variables: "DB_HOST", '
                            '"DB_USER" and "DB_PASSWORD".')
        else:
            return {'db_host': db_host, 'db_user': db_user, 'db_password': db_password}
