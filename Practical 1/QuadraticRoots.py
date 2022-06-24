#Find roots of the quadratic equation
a = int(input("Enter the square term: "))
b = int(input("Enter the middle term: "))
c = int(input("Enter the coefficient term: "))
delta = (b**2 - 4*a*c) ** 0.5
root1 = (-b + delta) / 2*a
root2 = (-b - delta) / 2*a
print("The roots of the given quadratic equation are:",root1,"and",root2)