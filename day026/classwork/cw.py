password = "1234"
user_password = input("შეიყვანე პაროლი: ")

while user_password != password:
    print("პაროლი არასწორია, სცადე თავიდან!")
    user_password = input("შეიყვანე პაროლი: ")
print("პაროლი სწორია,")