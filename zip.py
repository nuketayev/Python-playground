usernames = ["Aka","Baka","Make"]
passwords = ("password1","password2","password3")

users = zip(usernames, passwords)

print(type(users))
for i in users:
    print(i)