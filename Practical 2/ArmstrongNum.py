#To find whether given number is Armstrong number or not
num = int(input("Enter a number: "))
sum = 0
l = len(str(num))
temp = num
while(temp != 0):
    rem = temp % 10
    sum += pow(rem, l)
    temp = temp // 10
if(sum == num):
    print(num,"is a Armstrong number")
else:
    print(num,"is not a Armstrong number")