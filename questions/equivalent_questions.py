"""
How to check if two questions are equivalent?
That is, given two questions, and a dictionary of synonyms,
the task is to answer yes if equal, or no if not equal. Write a program to do that.
"""


synonyms = {
    'synonym': 'equivalent',
    'fun': 'enjoyable',
    'try': 'attempt',
}


class Solution:
    def is_equivalent(self, q1, q2):
        for key, value in synonyms.items():
            if key not in q1:
                q2 = q2.replace(key, value)
            if q1 == q2:
                return True
            if value not in q1:
                q2 = q2.replace(value, key)
            if q1 == q2:
                return True
        return q1 == q2


print(
    Solution().is_equivalent(
        'Is your job enjoyable? Try to find a synonym for that?'.lower(),
        'Is your job fun? Attempt to find a equivalent for that?'.lower()
    )
)
