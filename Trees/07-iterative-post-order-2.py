class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def iterative_post_order(root:TreeNode):
    #We need to keep moving left side 
    #Store the left pointer in a stack
    #Once the left side is null then 
    #remove from stack, here 2 cases 
    #case-1 leaf node then add this to result 
    #case-2 root node, that has to go right side subtree
    #case-3 root node, already visited right subtree and ready 
    #to be printed
    #How we find that root node which is already visited given the case
    #let's take simple tree root node left and right subtree 
    #For the case right subtree not visited, previous visited is not
    #true, when right subtree is visited, previous visited node equal
    #to the right subtree node then that means we already visited 
    current = root
    stack=[]
    previous=None
    peek_node=None
    result=[]
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            #Get the top element of stack
            peek_node=stack[-1]
            #Now check the case we are first time visiting the
            #right subtree
            #If its first time then point our current to right subtree
            #once travel is done right sub tree 
            #And comes back to same root, then we store the previous 
            #visited node to right node. This root node right and previous 
            #visited confirms that we need to now print root node 
            if peek_node.right and peek_node.right != previous:
                current=peek_node.right
            else:
                #Now we print the root node value since 
                #We already visited that node
                result.append(peek_node.val)
                previous=stack.pop()
    return result
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
r=iterative_post_order(root)
print(f"Expected iterative result is [4,5,2,3,1]")
print(f"Actual iterative value got is {r}")