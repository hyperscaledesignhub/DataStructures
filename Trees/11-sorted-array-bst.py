class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def sorted_array_to_bst(input:list[int]):
    input.sort()
    def helper(start:int,end:int):
        if start > end:
            return
        if start == end:
            return TreeNode(input[start])
        mid = (start + end)//2
        root = TreeNode(input[mid])
        root.left=helper(start,mid-1)
        root.right=helper(mid+1,end)
        return root
    return helper(0,len(input)-1)
def print_tree(root, level=0, prefix="Root: "):
    if root:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")
input=[10,5,1,2,3,8]
root= sorted_array_to_bst(input)
print(f"root value is {root.val}")
print_tree(root)
    