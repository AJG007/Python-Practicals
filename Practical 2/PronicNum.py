#To find whether given number is Pronic number or not
def check_pronic(n):
    for i in range(n):
        if i * (i + 1) == n:
            return True
        if i * (i + 1) > n:
            return False

num = int(input('Enter a number: '))

if check_pronic(num):
    print(f'{num} is a Pronic number')
else:
    print(f'{num} is not a Pronic number')