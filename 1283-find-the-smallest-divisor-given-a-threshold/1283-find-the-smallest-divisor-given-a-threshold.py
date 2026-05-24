import math
class Solution:
    def touch(self,nums , divisor, threshold):
        n=len(nums)
        sum=0
        for i in nums:
            sum+=math.ceil(i/ divisor)
        return sum<=threshold
    
    def smallestDivisor(self,nums,threshold):
        left=1
        right=max(nums)
        ans=1
        while left<=right:
            mid=(left+right)//2
            if self.touch(nums,mid,threshold):
                ans=mid
                
                right=mid-1
            else:
                left=mid+1
        return ans 