class Solution:
    def triangleType(self, nums: List[int]) -> str:
        type=len(set(nums))
        if nums[0]+nums[1]<=nums[2] or nums[0]+nums[2]<=nums[1] or nums[2]+nums[1]<=nums[0]:
            return "none"
        elif type==1:
            return "equilateral"
        elif type==2:
            return "isosceles"
        elif type==3:
            return "scalene"

