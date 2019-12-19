import bcrypt
import hmac


class Password:
    def __init__(self):
        self.salt = bcrypt.gensalt()

    def hash_password(self, password_string):
        hashed_password = bcrypt.hashpw(password_string, self.salt)
        return hashed_password

    def hash_check(self, cleartext_password, hashed_password):
        if hmac.compare_digest(self.hash_password(cleartext_password), hashed_password):
            return True
        return False
