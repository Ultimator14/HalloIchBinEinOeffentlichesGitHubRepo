from User import User
from Password import Password

cleartext_password = "123_x&5s".encode('utf-8')
p = Password(cleartext_password)

user1 = User()
user1.set_name("Bert")
user1.set_password(p)

p2 = user1.get_password()

if p2.hash_check(cleartext_password):
    print("Yes")
else:
    print("No")
