class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber>0:
              return self.convertToTitle((columnNumber-1)//26)+chr(ord('A')+(columnNumber-1) %26)
        else:
            return ''     