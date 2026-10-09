class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        diff=[]
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        total=prefix[len(nums)-1]
        for i in range(len(nums)):
            rs=total-prefix[i]
            ls=prefix[i]-nums[i]
            diff.append(abs(ls-rs))
        return diff

        