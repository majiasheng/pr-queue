import os
from dotenv import load_dotenv
load_dotenv()

sql_user = 'prqueueadmin'
sql_host = os.environ.get('SQL_HOST', 'localhost')
sql_port = os.environ.get('SQL_PORT', 5432)
sql_database = os.environ.get('SQL_DATABASE', '')
