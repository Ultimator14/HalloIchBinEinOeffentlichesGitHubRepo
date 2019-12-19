from User import User
from Password import Password

p = Password()
password = "123_x&5s".encode('utf-8')
hashed_password = p.hash_password(password)

user1 = User()
user1.set_name("Bert")
user1.set_password(hashed_password)

hashed_password2 = user1.get_password()
if p.hash_check(password, hashed_password2):
    print("Yes")
else:
    print("No")
