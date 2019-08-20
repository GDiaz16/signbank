import os
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(BASE_DIR)
PROJECT_DIR = os.path.join(os.path.dirname(BASE_DIR),"locale")
print(PROJECT_DIR)
print( os.path.join(BASE_DIR, 'static'))