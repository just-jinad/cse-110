user_numbers = []

print("Enter a list of numbers, type 0 when finished.\n")

count = 1
total_sum = 0

userInput = int(input("Enter number: "))
user_numbers.append(userInput)

while userInput != 0 :
    userInput = int(input("Enter number: "))
    if userInput != 0:
     user_numbers.append(userInput)
     count+=1

print(f"The number count is: {count}")

for i in user_numbers:
    print(f"{i}")
    total_sum = total_sum + i

total_average = float(total_sum / count)
largest = max(user_numbers)

smallest_positive = 99999999999999999999999999

for number in user_numbers:
    if number > 0 and number < smallest_positive:
        smallest_positive = number 


print(f"The total sum: {total_sum}")
print(f"The average is: {total_average}")
print(f"The largest number is: {largest}")
print(f"The smallest positive is: {smallest_positive}")

