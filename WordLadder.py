import string

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
            
        if beginWord == endWord:
            return 1
            
        usedWord = set()
        sets = [set([beginWord]), set([endWord])]
        levels = [1, 1]

        while sets[0] and sets[1]:
            if len(sets[1]) < len(sets[0]):
                sets.reverse()
                levels.reverse()
                
            usedWord.update(sets[0])
            
            newBeginSet = set()
            for word in sets[0]:
                for idx in xrange(len(word)):
                    prefix = word[:idx]
                    suffix = word[idx+1:]
                    for c in string.ascii_lowercase:
                        testWord = prefix + c + suffix
                        if testWord != word and testWord in wordList and testWord not in usedWord:
                            if testWord in sets[1]:
                                return levels[0] + levels[1]
                            newBeginSet.add(testWord)
            sets[0] = newBeginSet
            levels[0] += 1
            
        return 0
