import sys
import os
import unittest
import sys

from src.run import app

class case(unittest.TestCase):
    def setUp(self) -> None:
        "Corre antes que todos los tests."
        app.testing = True
        self.app = app.test_client()
        pass

    def test1(self) -> None:
        """
        Sample test para Flask.
        """
        result = self.app.get("/")
        print(result.get_json())
        pass

if __name__ == '__main__':
    unittest.main()
