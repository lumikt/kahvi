# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
import subprocess
from os import path

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"
        self.abs_path = path.dirname(path.abspath(__file__))

    def reset_application(self):
        print(self.abs_path)
        subprocess.run(["python3", f"{self.abs_path}/db_helper.py"], check=True)
