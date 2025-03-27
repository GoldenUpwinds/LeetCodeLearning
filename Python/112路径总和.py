import collections

null = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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
    def preoder(self,root,targetSum):
        if not root:
            return False
        
        targetSum -= root.val
        if targetSum == 0 and not root.left and not root.right:
            return True
        if self.preoder(root.left,targetSum) or self.preoder(root.right,targetSum):
            return True
        targetSum += root.val
        return False

    def hasPathSum(self, root, targetSum: int) -> bool:
        return self.preoder(root,targetSum)
    
Solve = Solution()
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
root = List2TreeNode(root)
targetSum = 22
print(Solve.hasPathSum(root,targetSum))