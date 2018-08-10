class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in xrange(len(strs[0])):
            print(i)
            for string in strs[1:]:
                print(string)
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["hello", "heaven", "heavy"]))