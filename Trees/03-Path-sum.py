class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
def path_sum(root:TreeNode,sum:int):
    flag=[False]
    #We have to find all root to leaf paths here
    def helper(node:TreeNode,target:int):
        #Base case 
        if node.left is None and node.right is None:
            if node.val == target:
                flag[0] = True
                return
            
        #We are using the preorder traversal here 
        #Since we have to find the root to leaf paths, base case must 
        #check if we reached leaf node. Because ultimately this is
        #where any traversal ends
        #recursive case 
        if node.left != None:
            helper(node.left,target- node.val)
        if node.right !=None:
            helper(node.right,target-node.val)
    helper(root,sum)
    return flag[0]

    
    
root=TreeNode(10)
root.left= TreeNode(5)
root.right = TreeNode(4)
root.left.left=TreeNode(6)
root.left.right=TreeNode(7)
root.right.left=TreeNode(8)
root.right.right = TreeNode(2)
result=path_sum(root,21)
print(f"Leaf to root path sum 21, is present = {result}")
    
            