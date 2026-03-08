import collections

class BinaryTree:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right 
def level_order(root:BinaryTree):
    q= collections.deque([root])
    result=[]
    while len(q) != 0:
        temp=[]
        size=len(q)
        while size > 0:
            node=q.popleft()
            temp.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            size -=1
        result.append(temp)
    return result
root = BinaryTree(9)
root.left = BinaryTree(5)
root.right = BinaryTree(4)
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(10)
root.right.left = BinaryTree(11)
root.right.right = BinaryTree(12)
r=level_order(root)
print(f"Level order traversal of the tree: is {r}")
        
    
    