import os
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
print(os.path.join(os.path.dirname(BASE_DIR), "locale"))