"""
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


class Solution:
    """
    Sliding window approach
    O(n)

    create previous chars dictionary
    set max_length and start to 0
    iterate over the string

    if the current iteration value in previous chars:
        get the index of when that char appeared,
        Add 1 to that index, if the result is bigger then the current start, set it as the current start
    calculate the size of the substring, current_index - start(distance between the pointers) + 1
    if the result is bigger then the previously saved max_length, set as the new max_length
    add current iteration value to previous chars
    """
    def length_of_longest_substring_without_repeating_characters(self, string: str) -> int:
        """
        :param string: string to find the longest substring without repeating characters
        :return: length of the longest substring
        """
        previous_chars = {}
        max_length = start = 0
        for i, value in enumerate(string):
            if value in previous_chars:
                possible_new_start = previous_chars[value] + 1
                if possible_new_start > start:
                    start = possible_new_start
            size_of_substring = i - start + 1
            if size_of_substring > max_length:
                max_length = size_of_substring
            previous_chars[value] = i
        return max_length

        # dicts = {}
        # maxlength = start = 0
        # for i, value in enumerate(string):
        #     if value in dicts:
        #         sums = dicts[value] + 1
        #         if sums > start:
        #             start = sums
        #     num = i - start + 1
        #     if num > maxlength:
        #         maxlength = num
        #     dicts[value] = i
        # return maxlength


print(Solution().length_of_longest_substring_without_repeating_characters("pwwkew"))
