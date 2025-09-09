class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=strs[0]
        for i in strs[1:]:
            while i[:len(result)]!=result:
                result=result[:-1]
                if result=="":
                    return ""
        return result
        