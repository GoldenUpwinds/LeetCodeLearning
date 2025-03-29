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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.left
            else:
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                return root.right
        
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)

        return root
    
Solve = Solution()
root = [5,3,6,2,4,null,7]
root = List2TreeNode(root)
key = 3
root = Solve.deleteNode(root,key)
print(TreeNode2List(root))