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


if __name__ == "__main__":
	# Driver code
	# Linear search
	l = [1,2,3,4,5,6,7,8,9,0,11,12,13,114,33,44,55,66,77,88,99]
	x = 1000
	if linear_search(x,l):
		print(x, "Found!")
	else:
		print(x, "Not Found!!")
		
	print("-------------------------------------------------")
	
	# Binary Search	
	l = [1,2,3,4,5,6,7,8,9,0,11,12,13,114,33,44,55,66,77,88,99]
	x = 13
	if binary_search(x,l):
		print(x, "Found!")
	else:
		print(x, "Not Found!!")
		
	print("-------------------------------------------------")
	
	
