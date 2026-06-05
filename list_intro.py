friend_banks = []

userInput = input("Type the name of a friend: ")
friend_banks.append(userInput)

while userInput != "end":
    userInput = input("Type the name of a friend: ")
    if userInput != "end":
     friend_banks.append(userInput)


print("The friends are: ")
for friend in friend_banks:
    print(f" {friend}")