import unittest
from repo_metrics import len_generator

class TestLenGenerator(unittest.TestCase):
    def test_empty_generator_has_0_length(self):
        self.assertEqual(0, len_generator([].__iter__()))

    def test_generator_with_1_element(self):
        self.assertEqual(1, len_generator([1].__iter__()))

    def test_generator_with_2_elements(self):
        self.assertEqual(2, len_generator([1, 1].__iter__()))
