'''Binary Tree Class and its methods'''
class BinaryTree:
	def __init__(self, data):
		self.data = data  # root node
		self.left = None  # left child
		self.right = None  # right child
	# set data
	def setData(self, data):
		self.data = data
	# get data   
	def getData(self):
		return self.data	
	# get left child of a node
	def getLeft(self):
		return self.left
	# get right child of a node
	def getRight(self):
		return self.right
	# get left child of a node
	def setLeft(self, left):
		self.left = left
	# get right child of a node
	def setRight(self, right):
		self.right = right
	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.left = self.left
			self.left = temp
	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.right = self.right
			self.right = temp
				    

# Post-order recursive traversal. The nodes' values are appended to the result list in traversal order
def postorderRecursive(root, result):
    if not root:
        return
    
    postorderRecursive(root.left, result)
    postorderRecursive(root.right, result)
    result.append(root.data)


# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order
def postorderIterative(root, result):
    if not root:
        return
    visited = set() #keep track  of visited nodes
    stack = []
    node = root
    while stack or node:
        if node: #node first then stack
            stack.append(node)
            node = node.left  #Go all the way to the left!!!!
        else:
            node = stack.pop() #no more nodes on left. get parent node
            if node.right and not node in visited:  #single visit
                visited.add(node) 
                stack.append(node)
                node = node.right #Go all the way to the right!!!!
            else:
                result.append(node.data)
                node = None #no right, so set to none to stop iteration


			
#Initialize Binary Tree
root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)

#Traverse
result = []
postorderRecursive(root, result)
print("PostOrder traversal (recursive): %s" % (result))

del result[::]
postorderIterative(root, result)
print("PostOrder traversal (Iterative): %s" % (result))
