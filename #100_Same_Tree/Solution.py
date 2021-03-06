class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} p
	# @param {TreeNode} q
	# @return {boolean}
	def isSameTree(self, p, q):
		if not p and not q:
			return True
		if not p or not q:
			return False
		if p is q:
			return True
		if p.val != q.val:
			return False
		return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)