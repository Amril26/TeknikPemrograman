import time
def search(arr, n, x): 
  
    for i in range (0, n): 
        if (arr[i] == x): 
            return i; 

arr = [ 50, 2, 3, 4, 10, 40 ]; 
print("========== Pilihan Array ==========")
print("{}" .format(arr))
print("===================================")
x = int(input("Masukan Nilai yang di Inginkan : "))

n = len(arr); 
start = time.time()
result = search(arr, n, x) 
end = time.time()
if(result == -1): 
    print("Angka yang di cari tidak ada di array") 
else: 
    print("Array ke : {}" .format(result)); 
    print("waktu yang di butuhkan %f detik " % (end - start))

