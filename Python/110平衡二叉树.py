import collections

null = None

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left

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

        if nums[index]:
            node.right = TreeNode(nums[index])
            queue.append(node.right)
        index += 1

        return root

class Solution:
    def checkHeight(self, root):
        if not root:
            return 0
        leftHeight = self.checkHeight(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.checkHeight(root.right)
        if rightHeight == -1:
            return -1
        
        if abs(leftHeight-rightHeight) > 1:
            return -1
        else:
            return 1+max(leftHeight,rightHeight)

    def isBalanced(self, root) -> bool:
        return False if self.checkHeight(root) == -1 else True

Solve = Solution()
root = [3,9,20,null,null,15,7]
root = List2TreeNode(root)
print(Solve.isBalanced(root))