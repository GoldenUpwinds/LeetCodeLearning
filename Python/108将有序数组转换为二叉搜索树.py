import collections
from typing import Optional, List

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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(left,right):
            if left > right:
                return None
            
            mid = (left+right) // 2
            root = TreeNode(nums[mid])
            
            root.left = helper(left,mid-1)
            root.right = helper(mid+1,right)

            return root
        
        return helper(0,len(nums)-1)

Solve = Solution()
nums = [-10,-3,0,5,9]
root = Solve.sortedArrayToBST(nums)
print(TreeNode2List(root))