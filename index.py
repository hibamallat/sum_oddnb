#The user must enter a number n
n = int(input("Enter n please: "))
#At the beginning, the sum is 0 
sum = 0

for i in range (n+1):
    if i % 2 != 0 : #If the number is odd, add it to the sum
        sum += i

print("The sum of the odd numbers is ", sum)