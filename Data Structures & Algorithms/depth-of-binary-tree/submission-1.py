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
        # create a queue with the root as the first element?
        q = deque([root])

        # recursively pop from the queue as you go down levels, so at bottom q is popped 
        while q:
            # loop through the q
            for i in range(len(q)):
                # pop from the beginning of the queue aka popleft
                # as you pop, that means you are moving through the nodes, or going down levels
                root = q.popleft()
                if root.left:
                    # if there is a left child add the child 
                    q.append(root.left)
                    
                if root.right:
                    # if there is a right child add the child 
                    q.append(root.right)
            count += 1
        return count
            
