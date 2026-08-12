# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # bfs

        treeOne = deque([p])
        treeTwo = deque([q])

        while treeOne and treeTwo:
            for _ in range(len(treeOne)):
                nodeP = treeOne.popleft()
                nodeQ = treeTwo.popleft()
                if nodeP is None and nodeQ is None:
                    continue
                    
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                treeOne.append(nodeP.left)
                treeOne.append(nodeP.right)
                treeTwo.append(nodeQ.left)
                treeTwo.append(nodeQ.right)

        return True
                    
 

                    

                    
