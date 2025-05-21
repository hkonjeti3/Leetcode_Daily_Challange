from collections import defaultdict
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        operations=[0]*(len(nums)+1)
        final=[]
        for i,j in queries:
            operations[i]+=1
            operations[j+1]-=1

        curr=0
        for i in range(len(nums)):
            curr+=operations[i]
            final.append(curr)

        for i in range(len(nums)):
            if nums[i]>final[i]:
                return False

        return True
