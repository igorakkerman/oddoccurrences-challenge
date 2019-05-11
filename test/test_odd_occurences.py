from unittest import TestCase

from main.odd_occurences import odd_occurences


class TestOddOccurences(TestCase):
    def test_odd_occurences(self):
        assert odd_occurences() == 42
