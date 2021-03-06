class Solution:
	# @param {integer[]} nums1
	# @param {integer} m
	# @param {integer[]} nums2
	# @param {integer} n
	# @return {void} Do not return anything, modify nums1 in-place instead.
	def merge(self, nums1, m, nums2, n):
		i = m - 1
		j = n - 1
		k = m + n - 1
		while i >= 0 or j >= 0:
			if i >= 0 and j >= 0:
				if nums1[i] > nums2[j]:
					nums1[k] = nums1[i]
					i -= 1
				else:
					nums1[k] = nums2[j]
					j -= 1
			elif i >= 0:
				nums1[k] = nums1[i]
				i -= 1
			else:
				nums1[k] = nums2[j]
				j -= 1
			k -= 1