# Exercise 2: Write a function that accepts a string and returns the longest palindromic substring in that string.

def longest_palindromic_substring(s):
    if len(s) <= 1:
        return s

    longest = ""
    
    for i in range(len(s)):
        # Check odd-length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(longest):
                longest = s[left:right + 1]
            left -= 1
            right += 1
        
        # Check even-length palindromes
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(longest):
                longest = s[left:right + 1]
            left -= 1
            right += 1

    return longest
# Unit tests
import unittest

class TestExercise2(unittest.TestCase):

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("babad"), "bab")
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")

if __name__ == '__main__':
    unittest.main()
