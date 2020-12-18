# selction sort

def selection_sort(arr):
	print()
	print("Selection sort: ")
	n=len(arr)
	for i in range(n):
		min_indx = i
		for j in range(i+1, n):
			if arr[j] < arr[min_indx]:
				min_indx = j
			
		arr[min_indx], arr[i] = arr[i], arr[min_indx]
	return arr

# Insertion sort
def insertion_sort(l):
	print()
	print("Insertion sort: ")
	for i in range(1,len(l)):
		flag1=0
		flag2=0
		for j in range(i-1,-1,-1):
			if l[i]<l[j]:
				flag1=1
				continue
			else:
				flag2=1
				break
		if flag1==1:
			key = l.pop(i)
			if flag2 == 0:
				l.insert(j,key)
			else:
				l.insert(j+1,key)
	return l

l=[99,12,1223,2323,1,0,278,23,222]
print("Unsorted List -> ", l)
print(selection_sort(l))
print(insertion_sort(l))
