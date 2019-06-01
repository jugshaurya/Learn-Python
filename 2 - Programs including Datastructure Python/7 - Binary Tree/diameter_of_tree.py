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

def diameter_tree(root):

    if root == None:
        return 0

    ld = diameter_tree(root.left)
    rd = diameter_tree(root.right)

    lh = height(root.left)
    rh = height(root.right)
    
    return max(ld, rd, 1 + lh + rh)

def diameter_tree_improved(root):

    if root == None:
        return (0,0)

    ld,lh = diameter_tree_improved(root.left)
    rd,rh = diameter_tree_improved(root.right)
    
    total_h = 1 + max(lh , rh)
    return max(ld, rd, lh + rh + 1), total_h 

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
levelOrder = [int(i) for i in input().split()]
root = buildLevelTree(levelOrder)
printLevelATNewLine(root)
print()

d = diameter_tree(root)
print('Diameter of tree is : ', d)

d = diameter_tree_improved(root)[0]
print('Diameter of tree is : ', d)

