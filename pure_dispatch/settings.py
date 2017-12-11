'''Settings for our application.
'''

import os

BASE_DIR = os.path.curdir

DATABASE_CONFIGURATION = {
    'DRIVER': 'sqlite3',
    'PATH': BASE_DIR
}