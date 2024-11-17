class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k=len(word1)
        j=len(word2)
        merged=""
        for i in range(min(k,j)):
            merged+=word1[i]
            merged+=word2[i]
        if k>j:
            merged+=word1[j:]
        else:
            merged+=word2[k:]
        return merged
        