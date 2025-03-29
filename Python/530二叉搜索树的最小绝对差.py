import collections
from typing import Optional

null = None

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
def List2TreeNode(nums):
    if not nums:
        return None
    
    root = TreeNode(nums[0])
    index = 1
    queue = collections.deque([root])

    while index < len(nums):
        node = queue.popleft()
    
        if nums[index]:
            node.left = TreeNode(nums[index])
            queue.append(node.left)
        index += 1

        if index == len(nums):
            break

        if nums[index]:
            node.right = TreeNode(nums[index])
            queue.append(node.right)
        index += 1
    
    return root

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre = None
        output = float('inf')

        def inorder(root):
            nonlocal pre
            nonlocal output

            if not root:
                return
            
            inorder(root.left)

            if pre:
                output = min(output,root.val-pre.val)
            pre = root

            inorder(root.right)
        
        inorder(root)

        return output
    
Solve = Solution()
root = [4,2,6,1,3]
root = List2TreeNode(root)
print(Solve.getMinimumDifference(root))