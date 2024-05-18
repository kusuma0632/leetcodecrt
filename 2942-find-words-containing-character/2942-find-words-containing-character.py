class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        r=[]
        for index,word in enumerate(words):
            if x in word:
                r.append(index)
        return r       