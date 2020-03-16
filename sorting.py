import time

A = [1, 3, 2, 5, 4]

for i in range(len(A)):
	
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j

	cont = A[i]
	A[i] = A[min_idx]
	A[min_idx] = cont

print ("Sorted array")
for i in range(len(A)):
	print("keluar angka %d" %A[i]),

start_time = time.process_time()
print(start_time)
