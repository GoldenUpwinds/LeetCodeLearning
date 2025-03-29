import collections
from typing import List

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
    queue = collections.deque([root])
    index = 1

    while index < len(nums):
        node = queue.popleft()

        if nums[index]:
            node.left = TreeNode(nums[index])
            queue.append(node.left)
        index += 1

        if nums[index]:
            node.right = TreeNode(nums[index])
            queue.append(node.right)
        index += 1
    return root

class Solution:
    def pathSum(self, root, targetSum: int) -> List[List[int]]:
        path, aus = [], []

        def findPath(root,targetSum):
            if not root:
                return

            path.append(root.val)
            if root.val == targetSum and not root.left and not root.right:
                aus.append(path[:])
                path.pop()
                return
            findPath(root.left, targetSum-root.val)
            findPath(root.right, targetSum-root.val)
            path.pop()
            return
        findPath(root,targetSum)
        return aus

Solve = Solution()
root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
root = List2TreeNode(root)
targetSum = 22
print(Solve.pathSum(root,targetSum))