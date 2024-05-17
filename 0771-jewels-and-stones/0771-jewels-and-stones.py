class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jw=set(jewels)
        c=0
        for  stone in stones:
            if stone in jw:
                c+=1
        return c       
            
        