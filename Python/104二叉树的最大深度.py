import collections

null = None

class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
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
    def getDepth(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        Depth = 1 + max(leftDepth,rightDepth)
        return Depth

    def maxDepth(self, root) -> int:
        return self.getDepth(root)

Solve = Solution()
root = [3,9,20,null,null,15,7]
root = List2TreeNode(root)
print(Solve.maxDepth(root))