import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'projectaccount'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'kCumRfZjUAvdisiPgVnJNu3YVmp2g3cDWo58twtxAN3Jb+5msV6ZWYxIaE3boUmMmh4mDi7bCz5c+AStWs2dqQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'projectcontainer'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacity-project-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacity-project-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'projectadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'password-1234'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "Ze_8Q~eZZT5nSCq.RlgRhnL2UD8R_97d1xMrba0K"
    # Try client secret from working msal app:
    # CLIENT_SECRET = "oTM8Q~OFV5wmXqZnVnuijagfyQkLhxKQ3NQ_NdA0"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "7aaa82ec-16ee-4a89-a879-6a61e7ea3a35" 
    # Try client id from working msal app:
    # CLIENT_ID = "0c5ac42c-45f9-4498-951e-18570a1b50ea"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
