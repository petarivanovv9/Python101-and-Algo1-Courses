import unittest
import the_real_deal


class TheRealDealTests(unittest.TestCase):

    def test_sum_all_divisors_of_an_integer(self):
        self.assertEqual(the_real_deal.sum_of_divisors(8), 15)
        self.assertEqual(the_real_deal.sum_of_divisors(7), 8)
        self.assertEqual(the_real_deal.sum_of_divisors(1), 1)
        self.assertEqual(the_real_deal.sum_of_divisors(1000), 2340)

    def test_if_integer_is_prime(self):
        self.assertFalse(the_real_deal.is_prime(1))
        self.assertTrue(the_real_deal.is_prime(2))
        self.assertFalse(the_real_deal.is_prime(8))
        self.assertTrue(the_real_deal.is_prime(11))
        self.assertFalse(the_real_deal.is_prime(-10))

    def test_number_containing_single_digit(self):
        self.assertFalse(the_real_deal.contains_digit(123, 4))
        self.assertFalse(the_real_deal.contains_digit(12356789, 4))
        self.assertTrue(the_real_deal.contains_digit(42, 2))
        self.assertTrue(the_real_deal.contains_digit(1000, 0))

    def test_number_containing_all_digits(self):
        self.assertTrue(the_real_deal.contains_digits(402123, [0, 3, 4]))
        self.assertFalse(the_real_deal.contains_digits(123456789, [1, 2, 3, 0]))

    def test_is_number_balanced(self):
        self.assertTrue(the_real_deal.is_number_balanced(9))
        self.assertTrue(the_real_deal.is_number_balanced(11))
        self.assertTrue(the_real_deal.is_number_balanced(121))
        self.assertTrue(the_real_deal.is_number_balanced(4518))
        self.assertTrue(the_real_deal.is_number_balanced(1238033))
        self.assertFalse(the_real_deal.is_number_balanced(13))
        self.assertFalse(the_real_deal.is_number_balanced(28471))

    def test_counting_substrings(self):
        self.assertEqual(the_real_deal.count_substrings(
            "This is a test string", "is"), 2)
        self.assertEqual(the_real_deal.count_substrings("babababa", "baba"), 2)
        self.assertEqual(the_real_deal.count_substrings(
            "Python is an awesome language to program in!", "o"), 4)
        self.assertEqual(the_real_deal.count_substrings(
            "We have nothing in common!", "really?"), 0)
        self.assertEqual(the_real_deal.count_substrings(
            "This is this and that is this", "this"), 2)

    def test_zero_insertion(self):
        self.assertEqual(the_real_deal.zero_insert(116457), 10160457)
        self.assertEqual(the_real_deal.zero_insert(55555555), 505050505050505)
        self.assertEqual(the_real_deal.zero_insert(6446), 6040406)

    def test_sum_numbers_in_matrix(self):
        self.assertEqual(the_real_deal.sum_matrix(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)
        self.assertEqual(the_real_deal.sum_matrix(
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)
        self.assertEqual(the_real_deal.sum_matrix(
            [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), 55)

    def test_matrix_bombing(self):
        pass

if __name__ == '__main__':
    unittest.main()
