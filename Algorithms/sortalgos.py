# selction sort

def selection_sort(arr):
	n=len(arr)
	for i in range(n):
		min_indx = i
		for j in range(i+1, n):
			if arr[j] < arr[min_indx]:
				min_indx = j
			
		arr[min_indx], arr[i] = arr[i], arr[min_indx]
	return arr

l=[99,12,1223,2323,1,0,278,23,222]

print(selection_sort(l))


