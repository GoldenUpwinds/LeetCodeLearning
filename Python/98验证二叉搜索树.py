import collections

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
    def preoder(self,root,output):
        if not root:
            return
        
        self.preoder(root.left,output)
        output.append(root.val)
        self.preoder(root.right,output)

        return
    
    def isValidBST(self, root) -> bool:
        nums = []
        self.preoder(root,nums)

        if len(nums) < 1:
            return True
        
        index = 1

        while index < len(nums):
            if nums[index] <= nums[index-1]:
                return False
            index += 1
        return True
    
Solve = Solution()
root = [2,1,3]
root = List2TreeNode(root)
print(Solve.isValidBST(root))