import sys
import unittest
from unittest import mock
from {{ cookiecutter.package }}.{{ cookiecutter.package }} import logic


class Test{{ cookiecutter.package }}(unittest.TestCase):
    def test_{{ cookiecutter.package }}(self):
        self.assertEqual('Hello World!', logic())
