#!/usr/bin/env python3

# Run from project root directory with
# python3 -m tests.test_wordle
# Note - test_wordle, not test_worlde.py (no file extension)

import unittest

import mock

from wordle import Wordle


# Test with practice word 'CHAIR'
class TestWordle_01(unittest.TestCase):

    def setUp(self):
        w = Wordle()
        w.correct = ['', 'H', '', 'I', '']
        w.close = ['A', 'R']
        w.eliminated = ['B', 'C', 'D', 'S', 'T']

    def tearDown(self):
        pass

    # Check possible solutions
    def test_check_words(self):
        self.assertFalse(w.check_word(self, 'flair'))


if __name__ == '__main__':
    unittest.main()
