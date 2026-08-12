# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS

        #if not root:
         #   return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # bfs
        if not root:
            return 0

        count = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            count += 1
        return count
            
