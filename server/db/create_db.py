"""Script to ensure the DB exists before starting the server
Called by launch_server.sh
"""
import os
import subprocess

from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = os.environ['DB_NAME']
DB_HOST = os.environ['DB_SERVICE']
DB_USER = os.environ['DB_USER']
CON = connect(
    user=DB_USER,
    host=DB_HOST,
    port=os.environ['DB_PORT'],
    password=os.environ['DB_PASS'])

CON.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
CUR = CON.cursor()

CUR.execute(
    "SELECT datname FROM pg_database WHERE datname='{0}'".format(DB_NAME))
RESULT = CUR.fetchone()
if RESULT is None:
    CUR.execute("CREATE DATABASE {0}".format(DB_NAME))
    subprocess.run([
        "psql", "-h", DB_HOST, "-U", DB_USER, "-d", DB_NAME, "-f",
        "db/starter_db.sql"
    ],
                   check=True,
                   capture_output=True)

CUR.close()
CON.close()
