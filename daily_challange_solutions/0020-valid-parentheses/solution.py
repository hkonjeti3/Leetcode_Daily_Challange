class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i,j=0,1
        for b in s:
            if b in ['{','[','(']:
                stack.append(b)
                continue
            else:
                if len(stack)!=0:
                    validate=stack.pop()  
                else: 
                    return False

                if (validate == '{' and b=='}') or (validate == '[' and b==']') or (validate == '(' and b==')'):
                    i+=2
                    j+=2
                else:
                    return False
        if len(stack) == 0:            
            return True
        else:
            return False
        
        
