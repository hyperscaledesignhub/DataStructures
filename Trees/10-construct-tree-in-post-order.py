class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def construct_tree(inorder:list[int],preorder:list[int]):
    in_map={}
    def construct_in_map():
        for i,j in enumerate(inorder):
            in_map[j] = i
    construct_in_map()
    def helper(inorder:list[int],in_start:int,in_end:int,preorder:list[int],
               pre_start:int,pre_end:int):
        if pre_start > pre_end or in_start > in_end:
            return
        
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])
        root=TreeNode(preorder[pre_start])
        root_index = in_map[preorder[pre_start]]
        num_left = root_index - in_start
        num_right = in_end - root_index
        in_start_left = in_start
        in_end_left = in_start + num_left-1
        pre_start_left = pre_start +1 
        pre_end_left = pre_start+num_left
        
        in_start_right = root_index+1
        in_end_right = root_index+num_right
        pre_start_right= pre_start+num_left+1
        pre_end_right = pre_start+num_left+num_right
        root.left = helper(inorder,in_start_left,in_end_left,preorder,
                           pre_start_left,pre_end_left)
        root.right = helper(inorder,in_start_right,in_end_right,preorder,
                            pre_start_right,pre_end_right)
        return root
    return helper(inorder,0,len(inorder)-1,preorder,0,len(preorder)-1)
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

# Test case
if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    
    
    root = construct_tree(inorder, preorder)
    
    print("Preorder:", preorder)
    print("Inorder:", inorder)
    print("\nConstructed Tree:")
    print_tree(root)
    print("\nExpected Tree Structure:")
    print("       3")
    print("      / \\")
    print("     9   20")
    print("        /  \\")
    print("       15   7")

