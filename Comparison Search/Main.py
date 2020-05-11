import time

def linearSearch(arr,n, x): 
  
    for i in range (0, n): 
        if (arr[i] == x): 
            return i
    return -1

def binarySearch(arr, min, max, x): 
  
    while min <= max: 
  
        mid = min + (max - min) // 2; 

        if arr[mid] == x: 
            return mid 
        elif arr[mid] < x: 
            min = mid + 1
        else: 
            max = mid - 1
    return -1

def Perbandingan():
    arr = [1,2,3,4,5,6,7,8,9,10]
    print ("========= List Array =========")
    print ("{}" .format(arr))
    x = int(input("Pilih angka yang di inginkan : "))
    print ("==============================\n")

    n = len(arr)
    start = time.time()
    result = linearSearch(arr,n,x)
    end = time.time()
    time1 = (end - start)

    if(result == -1): 
        print("Angka untuk Linear tidak ditemukan")
    else:
        print("Angka ke %d = Array ke : %d" %(x,result)); 
        print("Linear Search waktu %f detik \n" % (time1))


    start = time.time()
    result2 = binarySearch(arr,0 ,len(arr) -1,x)
    end = time.time()
    time2 = (end - start)
    if result2 != -1: 
        print ("Angka ke %d = Array ke : % d" %(x,result2) )
        print ("Binary Search Waktu %f detik\n" %(time2))
    else: 
        print ("Angka untuk binary tidak ditemukan ") 

    if (time1 < time2):
        print("===== Linear search lebih cepat =====")
    else :
        print("===== Binary search lebih cepat =====")
   


while True:
    Perbandingan()
    break


