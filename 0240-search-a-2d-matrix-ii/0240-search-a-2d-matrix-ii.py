class Solution:
    def searchMatrix(self,Matrix,target):
        n=len(Matrix)
        m=len(Matrix[0])
        row=0
        col=m-1
        while row<n and col >=0:
            if Matrix[row][col]==target:
                return True
            elif Matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False
