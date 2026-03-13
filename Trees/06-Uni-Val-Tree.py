#Unival tree means whose left subtree and right subtree and root 
#of the subtree values all are same. this is called 
#Unival tree
#First left subtree check its unival
#After that check my value with its left 
#value, then left_univa is true 
#now i traverser right and check return 
#if its univalue, if its i check right node value

#with my value so that right is univalue 
#if both left and right univalue then i increment
#Uni val count of the tree 
#I return to my manager overall i am unival 
# or not to my manager 
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def unival(root:TreeNode):
    unival_count=[0]
    def helper(node:TreeNode):
        left_unival=True
        right_unival=True
        ami_unival=True
        #Base case 
        
        #Recursive case
        if node.left !=None:
            left_unival=helper(node.left)
            if not left_unival or node.left.val != node.val:
                left_unival=False
        if node.right !=None:
            right_unival=helper(node.right)
            if not right_unival or node.right.val !=node.val:
                right_unival=False
        if not left_unival or not right_unival:
            ami_unival=False
        else:
            unival_count[0] +=1
        return ami_unival
    helper(root)
    return unival_count[0]
root=TreeNode(3)
root.left=TreeNode(5)
root.right=TreeNode(5)
root.right.right=TreeNode(5)
r=unival(root)
print(f"Unival count of the tree is {r}")