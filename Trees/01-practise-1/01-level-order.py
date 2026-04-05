import collections
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

        
def level_order(root:TreeNode):
    result=[]
    def helper(node:TreeNode):
        #Insert root into Queue
        q=collections.deque([node])
        #print(f"length of q is {len(q)}")
        while len(q) !=0:
            #count the size of q 
            size=len(q)
            #loop through only that size 
            #since we are going to insert elements 
            #while travelling 
            #We are measuring the size ahead and doing the same
            count = 0
            temp=[]
            while count < size:
                #remove element from queue
                n= q.popleft()
                temp.append(n.val)
                if n.left != None:
                    q.append(n.left)
                if n.right != None:
                    q.append(n.right)
                count +=1
                #print(f"temp value is {temp}")
            result.append(temp)
            #print(f"value of result is {result}")
        return result
    return helper(root)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
r=level_order(root)
print(f"result of level order traversal is {r}")
            
                
            
        