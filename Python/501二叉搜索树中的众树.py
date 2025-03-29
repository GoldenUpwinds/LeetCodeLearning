import collections
from typing import List,Optional

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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_appear = 0
        output = []
        pre = None
        appear_times = 0

        def preoder(root):
            nonlocal max_appear
            nonlocal output
            nonlocal pre
            nonlocal appear_times
            
            if not root:
                return
            
            preoder(root.left)

            if pre == None:
                appear_times = 1
            elif pre == root.val:
                appear_times += 1
            else:
                appear_times = 1
            pre = root.val

            if appear_times == max_appear:
                output.append(root.val)
            elif appear_times > max_appear:
                max_appear = appear_times
                output = [root.val]
            
            preoder(root.right)
        
        preoder(root)

        return output

Solve = Solution()
root = [1,null,2,2]
root = List2TreeNode(root)
print(Solve.findMode(root))


