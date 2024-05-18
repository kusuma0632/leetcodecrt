class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth=0
        for account in accounts:
            curwealth=sum(account)
            if curwealth>maxwealth:
                maxwealth=curwealth
        return maxwealth        

        