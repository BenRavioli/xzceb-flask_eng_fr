import unittest

from translator import french_to_english, english_to_french

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')


unittest.main()