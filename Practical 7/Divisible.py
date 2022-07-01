#Print the elements of given tuple that are divisible by k
arr = []
n = int(input("Enter number of elements in the tuple: "))
for i in range(n):
    list1 = list(map(int,input("Enter the elements: ").split()))
    arr.append(tuple(list1))

k = int(input("Enter value of k: "))
for i in arr:
    if(all(j%k==0 for j in i)):
        print(i)