# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result=[]
        queue=deque([root])
        flag=True
        
        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node .right:
                    queue.append(node.right)

            if not flag:
                level.reverse()
                    
            result.append(level)

            flag=not flag    

            
            
        return result
        
            

        
        

        