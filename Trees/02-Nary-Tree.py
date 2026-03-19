import collections
class BinaryTree:
    def __init__(self,val=0,children=None):
        self.val = val 
        self.children = children if children is not None else []
def level_order(root:BinaryTree):
    q= collections.deque([root])
    result=[]
    while len(q) !=0:
        size = len(q)
        temp=[]
        while size > 0:
            node = q.popleft()
            temp.append(node.val)
            for child in node.children:
                q.append(child)
            size -=1
        result.append(temp)
    return result
root=BinaryTree(1)
root.children = [BinaryTree(2),BinaryTree(3),BinaryTree(4)]
root.children[0].children=[BinaryTree(5),BinaryTree(6)]
root.children[1].children = [BinaryTree(7),BinaryTree(8)]
r= level_order(root)
print(f"level order traversal of N-Aray tree is {r}")

                