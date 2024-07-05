class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j=0,len(nums)-1
        k=0
        while i<len(nums):
            if nums[i]==val:
                while nums[j]==val and j>0:
                    j-=1
                if j<0:
                    return k
                nums[i]=nums[j]
                i+=1
                j-=1
                
                # print(nums)
            else:
                i+=1
                k+=1
        return k
        
        
