class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def diameter_tree(root:TreeNode):
    if root is None:
        return 0
    global_diameter=[0]
    def helper(node:TreeNode):
        lheight=0
        rheight=0
        diameter=0
        if node.left != None:
            lheight=helper(node.left)
        if node.right!= None:
            rheight=helper(node.right)
        diameter = lheight + rheight
        if diameter > global_diameter[0]:
            global_diameter[0] = diameter
        return max(lheight,rheight) + 1
    helper(root)
    return global_diameter[0]
root = TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
dia=diameter_tree(root)
print(f"Tree diameter is {dia}")
    
        