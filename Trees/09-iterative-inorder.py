class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
def iterative_inorder(root:TreeNode):
    if not root:
        return []
    result=[]
    stack=[]
    current=root
    while stack or current:
        while current:
            stack.append(current)
            current=current.left
        current=stack.pop()
        result.append(current.val)
        current=current.right
    return result
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
r=iterative_inorder(root)
print(f"Iterative inorder traversal expected is [4 2 5 1 3]")
print(f"Actual iterative inorder traversal is {r}")