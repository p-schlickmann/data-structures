class Solution:
    def groupAnagrams(self, strs):
        strs_hash = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in strs_hash:
                strs_hash[sorted_string] = strs_hash[sorted_string] + [string]
            else:
                strs_hash[sorted_string] = [string]

        return strs_hash.values()


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
