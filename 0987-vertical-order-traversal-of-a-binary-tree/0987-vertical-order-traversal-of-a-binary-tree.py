# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        
        dicct=defaultdict(list)
        q=deque([(root,0,0)])

        while q:

            node,row,col=q.popleft()

            
            dicct[col].append((row,node.val))
            
            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                 q.append((node.right,row+1,col+1))

        ans=[]
        for col in sorted(dicct):
            dicct[col].sort()

            ans.append( [value for row,value in dicct[col]])
        return ans
        