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
    def preoder(self, root, path, ans):
        path.append(str(root.val))
        if not root.left and not root.right:
            ans.append(path[:])
            path.pop()
            return
        
        if root.left:
            self.preoder(root.left,path,ans)
        if root.right:
            self.preoder(root.right,path,ans)

        path.pop()
        return
        


    def binaryTreePaths(self, root) -> List[str]:
        path, ans = [], []
        self.preoder(root,path,ans)

        output = []
        for sub_path in ans:
            output.append("->".join(sub_path))

        return output
    
Solve = Solution()
root = [1,2,3,null,5]
root = List2TreeNode(root)
print(Solve.binaryTreePaths(root))