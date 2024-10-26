#The user must enter a number n
n = int(input("Enter n please: "))
#At the start the sum is empty 
sum = 0
#If the number is odd, add it to the sum
for i in range (n+1):
    if i % 2 != 0 :
        sum += i

print("The sum of the odd numbers is ", sum)