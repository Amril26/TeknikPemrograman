import time
def bubbleSort(arr):
	n = len (arr)
	for i in range (n):
		for j in range ( 0 , n - i - 1 ):
			if arr[j] > arr[j + 1 ] :
				cou = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = cou
				print("#%i%s" %(i,arr))

arr = [ 64 , 34 , 25 , 12 , 22 , 11 , 90 ] 
start= time.time()
bubbleSort(arr) 
end = time.time()
print ("selesai %f " % (end - start))

