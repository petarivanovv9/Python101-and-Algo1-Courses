import unittest
import warmup


class WarmupTests(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(warmup.factorial(0), 1)
        self.assertEqual(warmup.factorial(1), 1)
        self.assertEqual(warmup.factorial(5), 120)

    def test_first_nth_members_of_Fibonacci(self):
        self.assertEqual(warmup.fibonacci(1), [1])
        self.assertEqual(warmup.fibonacci(2), [1, 1])
        self.assertEqual(warmup.fibonacci(3), [1, 1, 2])
        self.assertEqual(
            warmup.fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_sum_all_digits_of_a_number(self):
        self.assertEqual(warmup.sum_of_digits(1325132435356), 43)
        self.assertEqual(warmup.sum_of_digits(123), 6)
        self.assertEqual(warmup.sum_of_digits(6), 6)
        self.assertEqual(warmup.sum_of_digits(-10), 1)

    def test_factorial_digits(self):
        self.assertEqual(warmup.fact_digits(111), 3)
        self.assertEqual(warmup.fact_digits(145), 145)
        self.assertEqual(warmup.fact_digits(999), 1088640)

    def test_palindrome(self):
        self.assertTrue(warmup.palindrome(121))
        self.assertTrue(warmup.palindrome("kapak"))
        self.assertFalse(warmup.palindrome("baba"))

    def test_turn_a_number_into_list_of_digits(self):
        self.assertEqual(warmup.to_digits(123), [1, 2, 3])
        self.assertEqual(warmup.to_digits(99999), [9, 9, 9, 9, 9])
        self.assertEqual(warmup.to_digits(123023), [1, 2, 3, 0, 2, 3])

    def test_turn_a_list_of_digits_into_a_number(self):
        self.assertEqual(warmup.to_number([1, 2, 3]), 123)
        self.assertEqual(warmup.to_number([9, 9, 9, 9, 9]), 99999)

    def test_fibonacci_number(self):
        pass

    def test_vowels_in_a_string(self):
        self.assertEqual(warmup.count_vowels("Python"), 2)
        self.assertEqual(warmup.count_vowels("Theistareykjarbunga"), 8)
        self.assertEqual(warmup.count_vowels("grrrrgh!"), 0)
        self.assertEqual(warmup.count_vowels(
            "Github is the second best thing that happend to programmers, after the keyboard!"), 22)
        self.assertEqual(warmup.count_vowels("A nice day to code!"), 8)

    def test_consonants_in_string(self):
        self.assertEqual(warmup.count_consonants("Python"), 4)
        self.assertEqual(warmup.count_consonants("Theistareykjarbunga"), 11)
        self.assertEqual(warmup.count_consonants("grrrrgh!"), 7)
        self.assertEqual(warmup.count_consonants(
            "Github is the second best thing that happend to programmers, after the keyboard!"), 44)
        self.assertEqual(warmup.count_consonants("A nice day to code!"), 6)

    def test_char_histogram(self):
        self.assertEqual(warmup.char_histogram(
            "Python!"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})
        self.assertEqual(
            warmup.char_histogram("AAAAaaa!!!"), {'A': 4, 'a': 3, '!': 3})

    def test_palindrome_score(self):
        self.assertEqual(warmup.p_score(121), 1)
        self.assertEqual(warmup.p_score(48), 3)
        self.assertEqual(warmup.p_score(198), 6)

    def test_increasing_sequence(self):
        self.assertTrue(warmup.is_increasing([1, 2, 3, 4, 5]))
        self.assertTrue(warmup.is_increasing([1]))
        self.assertFalse(warmup.is_increasing([5, 6, -10]))
        self.assertFalse(warmup.is_increasing([1, 1, 1, 1]))

    def test_decreasing_sequence(self):
        self.assertTrue(warmup.is_decreasing([5, 4, 3, 2, 1]))
        self.assertFalse(warmup.is_decreasing([1, 2, 3]))

    def test_hack_numbers(self):
        self.assertEqual(warmup.next_hack(0), 1)
        self.assertEqual(warmup.next_hack(10), 21)
        self.assertEqual(warmup.next_hack(8031), 8191)

if __name__ == '__main__':
    unittest.main()
