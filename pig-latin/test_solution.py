import unittest
from solution import pig_latin


class TestPigLatin(unittest.TestCase):
    def test_words_starting_with_vowels(self):
        self.assertEqual(pig_latin("air"), "airway")
        self.assertEqual(pig_latin("eat"), "eatway")
        self.assertEqual(pig_latin("apple"), "appleway")

    def test_words_starting_with_consonants(self):
        self.assertEqual(pig_latin("python"), "ythonpay")
        self.assertEqual(pig_latin("computer"), "omputercay")
        self.assertEqual(pig_latin("dog"), "ogday")
        self.assertEqual(pig_latin("computer"), "omputercay")
        self.assertEqual(pig_latin("computer"), "omputercay")
        self.assertEqual(
            pig_latin("this is a test translation"),
            "histay isway away esttay ranslationtay",
        )

    def test_single_letter_words(self):
        self.assertEqual(pig_latin("a"), "away")
        self.assertEqual(pig_latin("banana"), "ananabay")

    def test_mixed_case_words(self):
        self.assertEqual(pig_latin("pYthon"), "ythonpay")
        self.assertEqual(pig_latin("cOmputer"), "omputercay")

if __name__ == "__main__":
    unittest.main()
