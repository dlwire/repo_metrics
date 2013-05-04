from fickle import apply_filters
import unittest

class FilterTest(unittest.TestCase):
    def setUp(self):
        self.collection = range(1,21) 
        self.filters = [
                lambda x: x % 3 == 0,
                lambda x: x % 2 == 0 ]

    def test_applies_all_filters_to_collection(self):
        result = apply_filters(self.collection, self.filters)
        self.assertEqual(result, [6, 12, 18])


if __name__ == '__main__':
    unittest.main()
