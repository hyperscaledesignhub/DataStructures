class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def path_sum_value(root: TreeNode,sum:int):
    result=[]
    flag=[False]
    def helper(node:TreeNode,target:int,slate:list[int]):
        #Base case
        if node.left is None and node.right is None:
            if node.val == target:
                slate.append(node.val)
                result.append(slate[:])
                slate.pop()
                flag[0]=True
                return
            
        #Recursive case 
        if node.left!=None:
            slate.append(node.val)
            helper(node.left,target - node.val,slate)
            slate.pop()
        if node.right != None:
            slate.append(node.val)
            helper(node.right,target-node.val,slate)
            slate.pop()
    helper(root,sum,[])
    return (flag[0],result)
root=TreeNode(10)
root.left= TreeNode(5)
root.right = TreeNode(4)
root.left.left=TreeNode(6)
root.left.right=TreeNode(7)
root.right.left=TreeNode(8)
root.right.right = TreeNode(2)
result_value=path_sum_value(root,21)
if result_value[0] is True:
    print(f" We have root to leaf path sum available, value is {result_value[1]}")