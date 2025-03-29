import collections
from typing import Optional

null = None

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def TreeNode2List(root):
    if not root:
        return []
    
    queue = collections.deque([root])
    counter = 1
    nums = []

    while queue and counter > 0:
        node = queue.popleft()

        if node:
            nums.append(node.val)
            counter -= 1
            if node.left:
                counter += 1
            if node.right:
                counter += 1
            queue.append(node.left)
            queue.append(node.right)
        else:
            nums.append(null)
            queue.append(null)
            queue.append(null)

    return nums

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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right = self.mergeTrees(root1.right,root2.right)

        return root1

Solve = Solution()
root1 = [1,3,2,5]
root2 = [2,1,3,null,4,null,7]
root1 = List2TreeNode(root1)
root2 = List2TreeNode(root2)
root = Solve.mergeTrees(root1,root2)
print(TreeNode2List(root))