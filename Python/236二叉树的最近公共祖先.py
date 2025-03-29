import collections

null = None

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def List2TreeNode(nums,p,q):
    if not nums:
        return None
    
    root = TreeNode(nums[0])
    if nums[0] == p:
        p_TreeNode = root
    elif nums[0] == q:
        q_TreeNode = root
    index = 1
    queue = collections.deque([root])

    while index < len(nums):
        node = queue.popleft()
        if node.val == p:
            p_TreeNode = node
        elif node.val == q:
            q_TreeNode = node

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
    return root, p_TreeNode, q_TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == q or root == p:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None

Solve = Solution()
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 1
root,p,q = List2TreeNode(root,p,q)
print(Solve.lowestCommonAncestor(root,p,q).val)
