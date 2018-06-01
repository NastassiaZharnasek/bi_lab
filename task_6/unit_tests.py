from program import is_palindrome
import unittest


class IsPalindromeTests(unittest.TestCase):

    def case_tests(self):
        self.assertEqual(is_palindrome('Repaper'), 'Palindrome')
        self.assertEqual(is_palindrome('MaDAm'), 'Palindrome')
        self.assertEqual(is_palindrome('emploYee'), 'Not a palindrome')

    def whitespace_and_punctual_symbols_tests(self):
        self.assertEqual(is_palindrome('r epa per'), 'Palindrome')
        self.assertEqual(is_palindrome('never odd or even'), 'Palindrome')
        self.assertEqual(is_palindrome('Re-p;ap!@e*r'), 'Palindrome')
        self.assertEqual(is_palindrome('m- -a,,,da.?#m'), 'Palindrome')
        self.assertEqual(is_palindrome('emp l oy e?e'), 'Not a palindrome')

    def mixed_tests(self):
        self.assertEqual(is_palindrome('A man, a plan, a canal – Panama'),
                         'Palindrome')
        self.assertEqual(is_palindrome("Madam, I'm Adam"), 'Palindrome')
        self.assertEqual(is_palindrome(" , "), 'Palindrome')
        self.assertEqual(is_palindrome("Madam 7_3, I'37m Adam"), 'Palindrome')
        self.assertEqual(is_palindrome("Go hang a salami, I'm a lasagna hog"),
                         'Palindrome')
        self.assertEqual(is_palindrome("Madam, I'm a Adam"), 'Not a '
                                                             'palindrome')


if __name__ == '__main__':
    unittest.main()
