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

        if nums[index] != None:
            node.left = TreeNode(nums[index])
            queue.append(node.left)
        index += 1

        if index == len(nums):
            break

        if nums[index] != None:
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < low:
            return self.trimBST(root.right,low,high)
        elif root.val > high:
            return self.trimBST(root.left,low,high)

        root.right = self.trimBST(root.right,low,high)
        root.left = self.trimBST(root.left,low,high)

        return root

Solve = Solution()
root = [1,0,2]
root = List2TreeNode(root)
low = 1
high = 2
root = Solve.trimBST(root,low,high)
print(TreeNode2List(root))