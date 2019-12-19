from User import User
from Password import Password
import hashlib

password = "123_x&5s"
hash_object = hashlib.md5(b'123_x32&')

user1 = User()
user1.set_name("Bert")

hashed_password = Password.hash_password(password)
user1.set_password(hashed_password)

hashed_password = user1.get_password()
Password.hash_check(password, hashed_password)
