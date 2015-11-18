import string

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        usedWord = set()
        beginMap, endMap = {}, {}
        beginMap[beginWord] = [[beginWord]]
        endMap[endWord] = [[endWord]]

        result = []
        while beginMap and endMap:
            if len(endMap) < len(beginMap):
                tmp = endMap
                endMap = beginMap
                beginMap = tmp

            usedWord.update(beginMap.keys())

            newBeginMap = {}
            for word in beginMap.keys():
                for idx in xrange(len(word)):
                    prefix = word[:idx]
                    suffix = word[idx+1:]
                    for c in string.ascii_lowercase:
                        newWord = prefix + c + suffix
                        if newWord != word and newWord in wordlist and newWord not in usedWord:
                            if newWord in endMap:
                                for l in beginMap[word]:
                                    for r in endMap[newWord]:
                                        _l = l[:]
                                        _r = r[:]
                                        _r.reverse()
                                        result.append(_l + _r)
                            else:
                                if newWord not in newBeginMap:
                                    newBeginMap[newWord] = []

                                for l in beginMap[word]:
                                    _l = l[:]
                                    _l.append(newWord)
                                    newBeginMap[newWord].append(_l)

            if result:
                for idx in range(len(result)):
                    if result[idx][0] != beginWord:
                        result[idx].reverse()
                return result

            beginMap = newBeginMap

        return result