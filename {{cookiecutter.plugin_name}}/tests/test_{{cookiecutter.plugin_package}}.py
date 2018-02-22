import sys
import unittest
try:
    from unittest import mock
except ImportError:
    from mock import mock
from {{ cookiecutter.plugin_package }}.{{ cookiecutter.plugin_package }} import logic


class Test{{ cookiecutter.plugin_package }}(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_{{ cookiecutter.plugin_package }}(self):
        self.assertEqual('Hello World!', logic())


if __name__ == '__main__':
    unittest.main()
