class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not s:
            return []

        left, right = 1, len(s) - 1
        result = []

        if s in wordDict:
            result = [s]

        while True:
            while left <= len(s) and s[:left] not in wordDict:
                left += 1

            while right >= 0 and s[right:] not in wordDict:
                right -= 1

            if left > right:
                break

            leftStr = s[:left]
            rightStr = s[left:]

            rresult = self.wordBreak(rightStr, wordDict)

            left += 1
            if not rresult:
                continue
            else:
                for _r in rresult:
                    result.append(leftStr[:] + " " + _r)

        return result