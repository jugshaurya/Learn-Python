import queue

class BinaryTreeNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def height(root):

    if root == None:
        return 0 

    lh = height(root.left)
    rh = height(root.right)

    return 1 + max(lh,rh)

# if height difference of all left and right subtree is -1,0,1, then tree is balanced.
def isBalanced(root):

    if root == None:
        return True


    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)
    lh = height(root.left)
    rh = height(root.right)

    return isLeftBalanced and isRightBalanced and (lh-rh) in [-1,0,1]

def isBalanced_improved_helper(root):

    if root == None :
        return (True, 0)

    isLeftBalanced, lh = isBalanced_improved_helper(root.left)
    isRightBalanced, rh = isBalanced_improved_helper(root.right)

    return (isLeftBalanced and isRightBalanced and (lh-rh) in [-1,0,1], 1 + max(lh,rh) )

def isBalanced_improved(root):
    isBalancedans , height = isBalanced_improved_helper(root)
    return isBalancedans 

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
# 1 2 -1 3 -1 -1 -1 -> not balanced
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1 -> balanced 
levelOrder = [int(i) for i in input().split()]
root = buildLevelTree(levelOrder)
printLevelATNewLine(root)

ans = isBalanced(root)
if ans :
    print('Tree is Balanced.')
else:
    print('Tree is not Balanced.')


ans = isBalanced_improved(root)
if ans :
    print('Tree is Balanced.')
else:
    print('Tree is not Balanced.')
