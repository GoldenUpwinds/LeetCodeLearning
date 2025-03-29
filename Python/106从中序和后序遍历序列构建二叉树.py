import collections
from typing import List, Optional

null = None

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def TreeNode2List(root):
    if not root:
        return None
    
    queue = collections.deque([root])
    count = 1
    nums = []

    while queue and count>0:
        node = queue.popleft()

        if not node:
            nums.append(null)
            queue.append(null)
            queue.append(null)
        else:
            nums.append(node.val)
            count -= 1
            if node.left:
                count += 1
            if node.right:
                count += 1
            queue.append(node.left)
            queue.append(node.right)
        
    while nums and not nums[-1]:
        nums.pop()
        
    return nums

class Solution:
    def buildTree_slow(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        root = TreeNode(postorder[-1])
        index = 0
        while inorder[index] != root.val:
            index += 1
        
        left_inorder = inorder[:index]
        left_postorder = postorder[:index]
        if index == len(inorder)-1:
            right_inorder = []
            right_postorder = []
        else:
            right_inorder = inorder[index+1:]
            right_postorder = postorder[index:len(postorder)-1]
        
        root.left = self.buildTree(left_inorder,left_postorder)
        root.right = self.buildTree(right_inorder,right_postorder)

        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hash_inorder = {val:index for index, val in enumerate(inorder)}

        def getTree(left_inorder,right_inorder,left_postorder,right_postorder):
            if left_inorder>right_inorder:
                return None
            if left_inorder == right_inorder:
                return TreeNode(inorder[left_inorder])
            
            val = postorder[right_postorder]
            root = TreeNode(val)

            index = hash_inorder[val]
            left_len = index - left_inorder
            root.left = getTree(left_inorder,index-1,left_postorder,left_postorder+left_len-1)
            root.right = getTree(index+1,right_inorder,left_postorder+left_len,right_postorder-1)

            return root
            
        return getTree(0,len(inorder)-1,0,len(postorder)-1)

Solve = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = (Solve.buildTree(inorder,postorder))
print(TreeNode2List(root))

