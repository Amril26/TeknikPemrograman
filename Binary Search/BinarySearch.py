import time
def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l) // 2; 

        if arr[mid] == x: 
            return mid 
  
        elif arr[mid] < x: 
            l = mid + 1
  
        else: 
            r = mid - 1
      
    return -1
print("===== ini list angka =====")
arr = [ 2, 3, 4, 10, 40 ] 

print("{}" .format(arr))
x = int(input("Masukan angka yang di inginkan : "))

start = time.time()
result = binarySearch(arr, 0, len(arr)-1, x) 
end = time.time()
  
if result != -1: 
    print ("Array ke : % d" % result)
    print ("Waktu yang di butuhkan %f detik" %(end - start))
else: 
    print ("Angka tidak ada! ") 