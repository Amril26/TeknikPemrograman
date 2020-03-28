import time

A = [1, 3, 2, 5, 4]
start = time.time()
for i in range(len(A)):
	
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j

	cont = A[i]
	A[i] = A[min_idx]
	A[min_idx] = cont
	print("#%i - %s" %(i,A))
end =time.time()
print ("Selesai %f detik" % (end - start) )
