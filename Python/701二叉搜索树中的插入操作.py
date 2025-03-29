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

def TreeNode2List(root):
    if not root:
        return []
    
    nums = []
    counter = 1
    queue = collections.deque([root])

    while queue and counter > 0:
        node = queue.popleft()

        if node:
            counter -= 1
            nums.append(node.val)
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

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)
        
        return root

Solve = Solution()
root = [4,2,7,1,3]
root = List2TreeNode(root)
val = 5
root = Solve.insertIntoBST(root,val)
print(TreeNode2List(root))