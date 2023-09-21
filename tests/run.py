import unittest

class case(unittest.TestCase):
    def setUp(self) -> None:
        "Corre antes que todos los tests."
        pass

    def test1(self) -> None:
        """
        Sample test.
        """
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
