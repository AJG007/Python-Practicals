# To find whether the given number a happy number or not
def isHappy(n):
    sum = 0
    while n>0:
        rem = n%10
        sum += pow(rem,2)
        n = n//10

    return sum

num = int(input("Enter a number: "))
temp = isHappy(num)
temp1 = 0
if(temp==1):
    print(num,"is a happy number")
elif(temp==4):
    print(num,"is not a happy number")
else:
    while(temp>=10):
        temp = isHappy(temp)
        if(temp==1):
            print(num,"is a happy number")
        elif temp==4:
            print(num,"is not a happy number")
