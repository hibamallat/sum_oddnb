n = int(input("Enter n please: "))
sum = 0
for i in range (n+1):
    if i % 2 != 0 :
        sum += i

print("The sum of the odd numbers is ", sum)