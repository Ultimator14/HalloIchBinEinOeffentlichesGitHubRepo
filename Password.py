import bcrypt
import hmac


class Password:
    def __init__(self, password_string):
        self.salt = bcrypt.gensalt()
        self.hashed_password = self.hash_password(password_string)

    def hash_password(self, password_string):
        hashed_password = bcrypt.hashpw(password_string, self.salt)
        return hashed_password

    def hash_check(self, password_string):
        if hmac.compare_digest(self.hash_password(password_string), self.hashed_password):
            return True
        return False
