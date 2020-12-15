"""
py script showcasing some of the search algorithms implementations
"""

def linear_search(x, l):
	""" equates to each element one by one, O(n) complexity """
	print("Linear Search started!")
	for i in range(len(l)):
		if l[i] == x:
			return True
	return False

def binary_search(x,seq):
	"""
	finds mid value of the list and equates it with x, then accordinly
	narrows down the search to one of the half of the list and keeps on 
	narrowing down till the element is found, O(log n) complexity
	"""
	print("Linear Search started!")
	l=0
	u=len(seq)-1
	seq=sorted(seq)
	print(seq)
	while l <= u:
		mid = (l+u)//2
		print(mid)
		if seq[mid] == x:
			return True
		elif seq[mid] > x:
			u = mid-1
		else:
			l = mid+1
	return False

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:35:37 2020

@author: rt2
"""


def jump_search(x,arr):
	"""
	Jump search algo implemenation
	"""
	n = len(arr)
	step = int(n**0.5)
	arr=sorted(arr)
	for i in range(0,n,step):
		
		if arr[i] < x:
			continue
		elif arr[i] == x:
			return i
		else:
			#found a number bigger than x
			break
	# after for loop ends, applying linear search for last 
	# left-out chunk of array
	if i < n:
		for j in range(i,n):
			if arr[j] == x:
				return i
	# Applying linear search for selected range of elements in array
	for j in range(i-step, i):
		if arr[j] == x:
			return j
	else:
		return -1

if __name__ == "__main__":
	# Driver code
	# Linear search
	l = [0,1,2,3,4,5,6,7,8,9,11,12,13,33,44,55,66,77,88,99,114]
	x = 1000
	if linear_search(x,l):
		print(x, "Found!")
	else:
		print(x, "Not Found!!")
		
	print("-------------------------------------------------")
	
	# Binary Search	
	l = [0,1,2,3,4,5,6,7,8,9,11,12,13,33,44,55,66,77,88,99,114]
	x = 13
	if binary_search(x,l):
		print(x, "Found!")
	else:
		print(x, "Not Found!!")
		
	print("-------------------------------------------------")
	l = [0,1,2,3,4,5,6,7,8,9,11,12,13,33,44,55,66,77,88,99,114]
	x = 13
	i=jump_search(x,arr)
	if i == -1:
		print(x, "Not found")
	else:
		print(x, "found at", i, "position")
	print("-------------------------------------------------")
	
	
