class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
#We are traversing iteratively using stack 
#And in post order traversal 
def iterative_post_order(root:TreeNode):
    stack = []
    last_visited=None
    current=root
    peek_node=None
    result=[]
    while current or stack:
        if current:
            stack.append(current)
            current=current.left
        else:
            peek_node=stack[-1]
            if peek_node.right and peek_node.right != last_visited:
                current=peek_node.right
            else:
                result.append(peek_node.val)
                last_visited=stack.pop()
    return result
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
r=iterative_post_order(root)
print(f"Expected iterative result is [4,5,2,3,1]")
print(f"Actual iterative value got is {r}")

                
            