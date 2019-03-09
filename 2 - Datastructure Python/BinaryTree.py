from BTNode import BinaryTreeNode

def printTree_preorder(root):
    if root==None:
        return

    print(root.data, ' : ', end = '')
    if root.left != None:
        print(root.left.data, end=',')
    if root.right != None:
        print(root.right.data, end=' ')
    print()
    
    printTree_preorder(root.left)
    printTree_preorder(root.right)

def buildTree():
    # li = [int(x) for x in input().split()] # given input in a line only, data is seperated by space
    root = None
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5


    root = node1
    return root

root = buildTree()
printTree_preorder(root)