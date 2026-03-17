class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
def iterative_pre_order(root:TreeNode):
    stack=[root]
    result=[]
    while stack:
        node=stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
r=iterative_pre_order(root)
print(f"Iterative pre order traversal is = {r} ")
        