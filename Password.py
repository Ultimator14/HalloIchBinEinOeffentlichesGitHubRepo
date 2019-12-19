import bcrypt
import hmac


class Password:
    @staticmethod
    def hash_password(password_string):
        hashed_password = bcrypt.hashpw(password_string, bcrypt.gensalt())
        return hashed_password

    @staticmethod
    def hash_check(cleartext_password, hashed_password):
        if hmac.compare_digest(bcrypt.hashpw(cleartext_password, hashed_password), hashed_password):
            print("Yes")
        else:
            print("No")    

# pw = input("Passwort: ")
# password = str.encode(pw) #Conversion string to bytes
