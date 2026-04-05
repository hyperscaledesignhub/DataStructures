import collections
class NaryTreeNode:
    #In regular TreeNode creation we are supplying left and right 
    #child nodes. For current node we are assigning value and 
    #then pointing it to the left and right child
    #Where as in NaryTreeNode, we point it to the list of children nodes
    #Which are supplied by the client
    def __init__(self,val=0,children=None):
        self.val=val
        self.children = [] if children is None else children
def Nary_Tree(root:NaryTreeNode):
    result = []
    def helper(node:NaryTreeNode):
        q= collections.deque([node])
        while len(q) !=0:
            size = len(q)
            count = 0
            temp=[]
            while count < size:
                node=q.popleft()
                temp.append(node.val)
                for n in node.children:
                    q.append(n)
                count +=1
            result.append(temp)
        return result
    return helper(root)
root = NaryTreeNode(1)
child1=NaryTreeNode(2)
child2=NaryTreeNode(3)
child3=NaryTreeNode(4)
root.children = [child1,child2,child3]
child1.children = [NaryTreeNode(5),NaryTreeNode(6),NaryTreeNode(7)]
child2.children=[NaryTreeNode(8),NaryTreeNode(9),NaryTreeNode(10)]
r=Nary_Tree(root)
print(f"The result of Nary Tree is {r}")


                    
                
