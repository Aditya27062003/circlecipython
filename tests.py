import unittest
from main import to_upper


class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Aditya"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "Aditya")

    if __name__ == '__main__':
        unittest.main()
