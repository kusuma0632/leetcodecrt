class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxwords=0
        for sentence in sentences:
            count=len(sentence.split())
            if count>maxwords:
                maxwords=count
        return maxwords        