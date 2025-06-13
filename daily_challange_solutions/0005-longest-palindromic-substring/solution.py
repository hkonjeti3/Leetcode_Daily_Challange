class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.l=0
        self.maxL=0

        def check(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            curL=j-i-1
            
            if curL>self.maxL:
                self.maxL=curL
                self.l=i+1

            return


        for i in range(len(s)):
            check(i,i)
            check(i,i+1)
        return s[self.l:self.l+self.maxL]
        


