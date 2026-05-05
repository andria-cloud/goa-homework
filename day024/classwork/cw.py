password = "anrdia"
user_input = input("enter your password: ")

while password != user_input:
    user_input = input("enter your password: ")
    print("wrong password. try again")
print("correct your password")