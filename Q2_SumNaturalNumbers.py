n=int(input("Enter how many natural numbers you want to find sum:"))
sum=0
for i in range(1, n+1):
    sum=i+sum
print("Sum of first",n, "natural numbers =",sum)
