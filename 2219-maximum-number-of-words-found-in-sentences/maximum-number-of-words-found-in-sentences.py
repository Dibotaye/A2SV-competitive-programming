class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        n = len(sentences)
        max_word = 0
        for i in range(n):
            count = 1
            for j in sentences[i]:
                if j == " ":
                    count += 1

            print(count)
            if count > max_word:
                max_word = count

        return max_word


