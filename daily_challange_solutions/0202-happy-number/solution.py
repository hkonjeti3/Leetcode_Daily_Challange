class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        loop=[]
        while n !=1:
            total= sum(int(i)*int(i) for i in str(n))
            n=total
            print(n,loop)
            if n == 1:
                return True
            elif n in loop:
                return False
            else:
                loop.append(n)

            
        
        
        
