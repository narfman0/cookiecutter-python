import sys
import unittest
try:
    from unittest import mock
except ImportError:
    from mock import mock
from {{ cookiecutter.package }}.{{ cookiecutter.package }} import logic


class Test{{ cookiecutter.package }}(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_{{ cookiecutter.package }}(self):
        self.assertEqual('Hello World!', logic())


if __name__ == '__main__':
    unittest.main()
