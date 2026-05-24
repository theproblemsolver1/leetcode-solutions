class Solution:
    def minuf(self,bloomDay ,m,k, days):
        flower=0
        bouquet=0
        for bloom in bloomDay:
            if bloom <=days:
                flower+=1
            else:
                flower=0

            if flower==k:
                bouquet+=1
                flower=0

        return bouquet>=m
    
        
    
        
    
       
        
    
    def minDays(self,bloomDay,m,k) :
        n=len(bloomDay) 


        if m*k>n:
            return -1
        
               
        left=min(bloomDay)
        right=max(bloomDay)
        ans =-1
    
        while left<=right:
            mid=(left+right)//2
            if self.minuf(bloomDay,m,k,mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans 
            