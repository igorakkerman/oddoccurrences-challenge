from unittest import TestCase

import pytest

from oddoccurences.odd_occurences import odd_occurences


class TestOddOccurences(TestCase):

    def test_empty(self):
        with pytest.raises(ValueError, match="List must contain an odd number of items."):
            odd_occurences([])

    def test_single(self):
        assert odd_occurences([1]) == 1

    def test_2(self):
        with pytest.raises(ValueError, match="List must contain an odd number of items."):
            odd_occurences([1, 2])

    def test_3_right(self):
        assert odd_occurences([1, 1, 2]) == 2

    def test_3_left(self):
        assert odd_occurences([1, 2, 2]) == 1

    def test_3_middle(self):
        assert odd_occurences([1, 2, 1]) == 2

    def test_3_no_pair(self):
        with pytest.raises(ValueError, match="List must only contain paired items and a single non-paired item."):
            odd_occurences([1, 2, 3])
