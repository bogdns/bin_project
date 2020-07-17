import unittest
from Igra import get_number_from_index,get_empty_list,get_index_from_number

class test_Igra(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_2(self):
        self.assertEqual(get_number_from_index(3, 3), 16)

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mesto = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(get_empty_list(mesto),a)

    def test_4(self):
        a = [13,14,15,16]
        mesto = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
        self.assertEqual(get_empty_list(mesto),a)

    def test_5(self):
        a = []
        mesto = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        self.assertEqual(get_empty_list(mesto),a)

    def test_6(self):
        self.assertEqual(get_index_from_number(7),(1,2))

    def test_7(self):
        self.assertEqual(get_index_from_number(1), (0, 0))

    def test_8(self):
        self.assertEqual(get_index_from_number(16), (3, 3))


if __name__ == "Igra":
    unittest.main()


