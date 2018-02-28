class Node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

	def get(self):
		return {'value':self.value,'left':self.left,'right':self.right}

def insert(root,node):
	if root.value < node.value: #add to right
		if root.right is None: #check node is leaf
			root.right = node
		else:insert(root.right, node)
	else:
		if root.left is None:root.left = node
		else:insert(root.left, node)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.value
        inorder(root.right)


def preorder(root):
    if root is not None:
    	print root.value
        preorder(root.left)
        
        preorder(root.right)

def getMin(root):
	while root.left is not None:
		root = root.left
	return root.valuedef 

def getMax(root):
	while root.right is not None:
		root = root.right
	return root.value

def getMin(root):
	while root.left is not None:
		root = root.left
	return root.value

def getMinNode(root):
	while root.left is not None:
		root = root.left
	return root

def delete(root,key):
	if root.value > key:
		root.left=delete(root.left,key)
	elif root.value < key:
		root.right=delete(root.right,key)
	else: 
		if root.left is None and root.right is None: root = None #delete leaf node
		elif root.left is None:
			root = root.right
		elif root.right is None:
			root = root.left
		else: # node has both clild
			temp = getMinNode(root.right)
			root.value = temp.value
			delete(root.right,temp.value)

	return root

def printTree(root,depth=0):
    if root is not None:
        printTree(root.left,depth+1)
        print '+++++++'*depth +str(root.value)
        printTree(root.right,depth+1)



root = Node(12)
l = [5,15,3,2,7,13,17,16,1,9,19]
for i in l:
	insert(root,Node(i))

#print root.left.value
printTree(root)

delete(root,15)
print 'After delete'
printTree(root)

