from BTNode import BinaryTreeNode

def userBuiltTree():
    rootData = int(input())

    # -1 is used to stop continuing over the current branch - so taking input in depth-first Style
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    root.left = userBuiltTree()
    root.right = userBuiltTree()    
    return root

def printTree_preorder(root):
    if root==None:
        return

    print(root.data, ' : ', end = '')
    if root.left != None:
        print('L', root.left.data, end = ',')
    if root.right != None:
        print('R', root.right.data, end = ' ')
    print()
    
    printTree_preorder(root.left)
    printTree_preorder(root.right)

def delete_leaf_nodes(root):
    if root == None:
        return None

    if root.left == None and root.right == None:
        return None
    
    root.left = delete_leaf_nodes(root.left)
    root.right = delete_leaf_nodes(root.right)

    return root

def mirror_image(root):
    
    if root == None:
        return 
    
    mirror_image(root.left)
    mirror_image(root.right)
    
    root.left,root.right = root.right,root.left
    
print('Enter the data of tree : ')
# Given input:  1 2 4 -1 -1 5 -1 -1 3 -1 7 -1 -1 
root = userBuiltTree()
print('Preorder Print : ')
printTree_preorder(root)

# changes the tree
mirror_image(root)
print('Mirror Image : ')
printTree_preorder(root)

# changes the tree
root = delete_leaf_nodes(root)
print('After the leafs are deleted : ')
printTree_preorder(root)


