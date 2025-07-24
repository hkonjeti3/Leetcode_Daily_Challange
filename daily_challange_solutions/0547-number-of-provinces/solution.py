class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces=0
        seen=set()
        n=len(isConnected)

        def dfs(node):
            for neighbour in range(n):
                if isConnected[node][neighbour] == 1 and neighbour not in seen:
                    seen.add(neighbour) 
                    dfs(neighbour)   


        for i in range(n):
            if i not in seen:
                seen.add(i)
                provinces+=1
                dfs(i)
            
                
        return provinces

        
