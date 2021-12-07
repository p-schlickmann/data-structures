"""
Input: s = "babad", "cbbd"
Output: "bab", "c"
"""


class Solution:
    def __init__(self):
        self.biggest_palindrome_start_index = 0
        self.biggest_palindrome_end_index = 0

    def longestPalindrome(self, string):
        """
        Checks for the longest palindrome expanding from center.
        Has to expand two times to cover cases where a palindrome is odd ('cbbd')
        Saves longest palindrome index to class properties, and uses them to slice the string
        :param string: string to check
        :return: longest palindrome substring
        """
        for i in range(len(string)):
            self.expand_from_center(string, i, i)
            self.expand_from_center(string, i, i + 1)
        return string[self.biggest_palindrome_start_index+1:self.biggest_palindrome_end_index]

    def expand_from_center(self, string, left, right):
        """
        Expands the string from the center (increases right one time, decreases left one time),

        If we loop though the borders, and the borders are equal,
        it is a palindrome until we reach a borders there are not equal
        :param string: string to check
        :param left: left index
        :param right: right index
        :return: None
        """
        while left > -1 and right < len(string) and string[left] == string[right]:
            # if True, it is a valid palindrome substring index, now expand it
            left -= 1
            right += 1

        if right - left > self.biggest_palindrome_end_index - self.biggest_palindrome_start_index:
            self.biggest_palindrome_start_index = left
            self.biggest_palindrome_end_index = right


Solution().longestPalindrome('cbbd')
