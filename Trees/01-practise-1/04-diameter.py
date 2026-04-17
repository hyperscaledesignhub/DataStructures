class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left=left
        self.right=right
def diameter(root:TreeNode):
    result = []
    diameter=[-1]
    #We need to find the longest diameter that 
    #includes the root node as well 
    #it may not be always part of the path that
    #is not requuired to be always pass through the root
    #sometimes left or right side may have more nodes 
    #Which traversal we have to use, do we need to start 
    #counting right from root node or from leaf node?
    #if we start counting right from root node 
    #then we have to pass the count from eavry root to next root
    #and then we need to pass the count 
    #this will be diffcult because after root finishes count, it
    #won't have left and right subtree counts available to them
    #where as if we go for inorder, only left is available right 
    #is not available. Where as if we do post order traversal 
    #left and right node height is available and we can mesaure
    #the diameter well 
    def helper(node:TreeNode,slate:list[int]):
        lhight=0
        rhight=0
        max_height=0
        print("enter-1")
        if node == None:
            return
        print("enter-2")
        if node.left != None:
            slate.append(node.val)
            lheight=helper(node.left,slate)
            slate.pop()
        if node.right != None:
            slate.append(node.val)
            rheight=helper(node.right,slate)
            slate.pop()
        max_height = lhight if lhight > rhight else rhight
        if diameter[0] < max_height:
            diameter[0] = max_height+1
            print(f"result is {result}")
            if len(result) !=0:
                result.pop()
            result.append(slate[:])
        return max_height +1
    helper(root,[])
    return (diameter[0],result)
root = TreeNode(1)
root.left=TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left=TreeNode(6)
root.left.left.right=TreeNode(7)
root.right.right = TreeNode(8)
r=diameter(root)
print(f"max diameter {r[0]} and diameter path {r[1]}")

    
        