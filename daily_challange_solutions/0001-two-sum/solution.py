class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for idx in range(len(nums)):
            need=target-nums[idx]
            if need in dic:
                return [dic[need],idx]
            else:
                dic[nums[idx]]=idx
                
