'''
	Python implementation of a Binary tree
'''
class BST:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

	'''
		Insert a node in BST
	'''
	def insert(self, n):
		if self.key>n:
			if self.left == None:
				self.left = BST(n)
			else:
				self.left.insert(n)
		else:
			if self.right == None:
				self.right = BST(n)
			else:
				self.right.insert(n)

	'''
		Search for a node in a BST
	'''
	def search(self, n):
		if self == None:
			return 0
		if self.key==n:
			return 1
		else:
			if self.key>n and self.left!=None:
				return self.left.search(n)
			elif self.key<n and self.right!=None:
				return self.right.search(n)
			return 0

	'''
		Traverse a BST in inorder
		left->root->right
	'''
	def inorder(self):
		if self.left!=None:
			self.left.inorder()
		print self.key
		if self.right!=None:
			self.right.inorder()

	'''
		Traverse a BST in preorder
		root->left->right
	'''
	def preorder(self):
		print self.key
		if self.left!=None:
			self.left.inorder()
		if self.right!=None:
			self.right.inorder()

	'''
		Traverse a BST in postorder
		left->right->root
	'''
	def postorder(self):
		if self.left!=None:
			self.left.inorder()
		if self.right!=None:
			self.right.inorder()
		print self.key

	'''
		Height of a node
	'''
	def height(self):
		lheight = 0
		if self.left!=None:
			lheight = self.left.height()
		rheight = 0
		if self.right!=None:
			rheight = self.right.height()
		return max(lheight, rheight)+1

	'''
		Maximum distance between any two leaf nodes
	'''
	def diameter(self, h):
		lheight = [0]
		ldiameter = 0
		if self.left!=None:
			ldiameter = self.left.diameter(lheight)
		rheight = [0]
		rdiameter = 0
		if self.right!=None:
			rdiameter = self.right.diameter(rheight)
		h[0] = max(lheight[0], rheight[0])+1
		return max(ldiameter, rdiameter, lheight[0]+rheight[0]+1)

	# TO EXCLUDE ODD LEVELS FOR REVERSING
	def inverse(self, h, exclude):
		h[0]+=1
		result = []
		if self.left!=None:
			result += self.left.inverse(h, exclude)
		if h[0]%2 == exclude:
			result.insert(len(result), self.key)
		if self.right!=None:
			result += self.right.inverse(h, exclude)
		h[0]-=1
		return result

	def inverse_replace(self, h, exclude, arr):
		h[0]+=1
		result = []
		if self.left!=None:
			self.left.inverse_replace(h, exclude, arr)
		if h[0]%2 == exclude:
			self.key = arr.pop(0)
		if self.right!=None:
			self.right.inverse_replace(h, exclude, arr)
		h[0]-=1

	'''
		Reverse a binary tree
	'''
	def reverse(self):
		h = [0]
		inord = self.inverse(h, 0)[::-1]
		self.inverse_replace(h, 0, inord)

	'''
		Checks if a Binary tree is perfect Binary tree or not
		every node has two child or none
	'''
	def isPerfect(self):
		if self.left!=None and self.right!=None:
			return self.left.isPerfect() and self.right.isPerfect()
		elif self.left==None and self.right==None:
			return True
		else:
			return False

	'''
		Finds the lowest common ancestor of two nodes labelled
		n1 and n2 in a BST
	'''	
	def LCA(self, n1, n2):
		n1, n2 = min(n1, n2), max(n1, n2)
		if self.key>=n1 and self.key<=n2:
			return self
		left = 0
		if self.left!=None:
			lLCA = self.left.LCA(n1, n2)
			if lLCA!=None:
				return lLCA
		if self.right!=None:
			rLCA = self.right.LCA(n1, n2)
			if rLCA!=None:
				return rLCA
		return None

	'''
		Finds the minimum depth of a node in Binary tree
	'''
	def minDepth(self):
		n = {'node': self, 'depth': 1}
		queue = [n]
		while len(queue)>0:
			e = queue.pop(0)
			n = e['node']
			if n.left==None or n.right==None:
				return e['depth']
			queue.insert(len(queue), {'node': n.left, 'depth': e['depth']+1})
			queue.insert(len(queue), {'node': n.right, 'depth': e['depth']+1})
			pass

	'''
		Check if a binary tree is a BST or not
	'''
	def isBST(self, previous):
		if self.left!=None:
			if self.left.isBST(previous)==False:
				return False
		if self.key>previous[0]:
			previous[0] = self.key
		else:
			return False
		if self.right!=None:
			if self.right.isBST(previous)==False:
				return False
		return True
'''
root = BST(8)
root.insert(4)
root.insert(12)
root.insert(2)
root.insert(6)
root.insert(1)
root.insert(3)
root.insert(5)
root.insert(7)
root.insert(10)
root.insert(9)
root.insert(11)
root.insert(14)
root.insert(13)
root.insert(15)
'''