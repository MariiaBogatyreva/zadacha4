def sorti(array, NN):
    for i in range(NN):
        if array[i] > 0 and i > 0:
            j = i-1
            while j >= 0 and array[j] <= 0:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                j-=1
f = open(r"C:\Users\superuser\Desktop\4\test.txt","r+")
N = int(f.readline())
arr = []
arr = list(map(int, f.read().split()))
if N < 1:
    print('Error!!!')
else:
    sorti(arr, N)
    print(arr)
    for x in arr:
        f.write(str(x)+'\n')
f.close()               
a = [1,2,-3,4,5]
sorti(a,5)
if a == [1,2,4,5,-3]:
    print('autotest passed')
else:
    print('autotest failed')

