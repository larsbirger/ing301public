import unittest
import exercise1 as e


class TestExercise1(unittest.TestCase):

    def test_read_file(self):
        expected = ["Det er\n", "bare\n", "noen få ord her!\n"]
        self.assertEqual(expected, e.read_file("small.txt"))

    def test_lines_to_words(self):
        self.assertEqual(["born", "åt", "heimdall"], e.lines_to_words(["born åt Heimdall;"]))
        self.assertEqual(["du", "bad", "meg", "koma", "odin"], e.lines_to_words(["du bad meg koma, Odin,\n"]))
        self.assertEqual([], e.lines_to_words([";,.:?!"]))
        self.assertEqual(["nothinghappenshere"], e.lines_to_words(["nOtHingHAPPENshere\n"]))
        self.assertEqual(["words", "on", "two", "lines"], e.lines_to_words(["words on\n", "two, lines!"]))

    def test_compute_frequency(self):
        self.assertEqual(e.compute_frequency(['hei', 'verden', 'hei']), {'hei': 2, 'verden': 1})
        test_data = ['the', 'quick', 'brown', 'fox', 'the', 'jumps', 'over', 'the', 'brown', 'wall']
        expected = {
            'fox': 1,
            'brown': 2,
            'the': 3,
            'quick': 1,
            'jumps': 1,
            'wall': 1,
            'over': 1
        }
        self.assertEqual(expected, e.compute_frequency(test_data))
        self.assertEqual(e.compute_frequency([]), {})

    def test_remove_filler_words(self):
        data = {
            'det': 42,
            'odin': 10,
            'og': 9,
            'ulv': 1,
            'til': 1,
            'gud': 3
        }
        expected = {
            'odin': 10,
            'ulv': 1,
            'gud': 3
        }
        self.assertEqual(expected, e.remove_filler_words(data))

    def test_largest_pair(self):
        self.assertEqual(("World", 5), e.largest_pair(('Hallo', 3), ("World", 5)))
        # kanskje du vil utvide test casene her

    def test_find_most_frequent(self):
        data = {
            'hei': 23,
            'sjelden': 1,
            'oftest': 9000,
            'answer': 42
        }
        self.assertEqual('oftest', e.find_most_frequent(data))
        del data['oftest']
        self.assertEqual('answer', e.find_most_frequent(data))


if __name__ == '__main__':
    unittest.main()