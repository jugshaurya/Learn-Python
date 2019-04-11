from BTNode import BinaryTreeNode

def printTree_preorder(root):
    if root==None:
        return

    print(root.data, ' : ', end = '')
    if root.left != None:
        print('L' , root.left.data, end = ',')
    if root.right != None:
        print('R' , root.right.data, end = ' ')
    print()
    
    printTree_preorder(root.left)
    printTree_preorder(root.right)

def printTree_postorder(root):
    if root == None:
        return
    
    printTree_postorder(root.left)
    printTree_postorder(root.right)
    print(root.data)

def printTree_inorder(root):
    if root == None:
        return
    
    printTree_postorder(root.left)
    print(root.data)
    printTree_postorder(root.right)
    
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

def userBuiltTree():
    rootData = int(input())

    # -1 is used to stop continuing over the current branch - so taking input in depth-first Style
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    root.left = userBuiltTree()
    root.right = userBuiltTree()    
    return root

def nodesInTree(root):
    
    if root is None:
        return 0
    leftCount = nodesInTree(root.left)
    rightCount = nodesInTree(root.right)
    return 1 + leftCount + rightCount

def largest_node(root):
    if root==None:
        return -2**31 # returing -inf
    
    leftMax = largest_node(root.left)
    rightMax = largest_node(root.right)
    rootData = root.data
    return max(rootData, leftMax,rightMax)

def nodes_gt_x(root,x):
    if root==None:
        return 
    
    nodes_gt_x(root.left,x)
    nodes_gt_x(root.right,x)
    if root.data > x:
        print(root.data)

def sumOfAllNodes(root):
    if root==None :
        return 0
    leftSum = sumOfAllNodes(root.left)
    rightSum = sumOfAllNodes(root.right)
    return root.data  + leftSum + rightSum

def treeHeight(root):        

    if root is None:
        return 0

    leftHeight = treeHeight(root.left)
    rightHeight = treeHeight(root.right)

    return 1+ max(leftHeight, rightHeight)

def numberOfLeaveNodes(root):
    if root is None:
        return 0
    
    leftans = numberOfLeaveNodes(root.left)
    rightans = numberOfLeaveNodes(root.right)
    result = leftans + rightans
    if result == 0 :
        result+=1
    return result

print('Enter the data of tree : ')
# Given input:  1 2 4 -1 -1 5 -1 -1 3 -1 7 -1 -1 
root = userBuiltTree()
print('Preorder Print : ')
printTree_preorder(root)

print('Numbers of Nodes are : ', nodesInTree(root))

print('Postorder Print : ')
printTree_postorder(root)

print('Inorder Print : ')
printTree_inorder(root)

print('Max Node Data is : ', largest_node(root) )
print('Sum of All nodes is : ', sumOfAllNodes(root))
print('Height of tree is : ', treeHeight(root))
print('Number of leaves nodes are : ', numberOfLeaveNodes(root))

x=int(input('Enter x '))
print('Values greater than %d are : '%x)
nodes_gt_x(root,x)





