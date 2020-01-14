import bcrypt
import hmac


def is_password_complex(password_string):
    if len(password_string) < 8:
        return False

    uppercase = False
    lowercase = False
    number = False
    symbol = False  # printable symbols

    for char in password_string:
        if chr(char).isupper():
            uppercase = True
        elif chr(char).islower():
            lowercase = True
        elif chr(char).isnumeric():
            number = True
        elif chr(char).isprintable():
            symbol = True
        else:
            return False  # non-printable symbol encountered

    if uppercase and lowercase and number and symbol:
        return True
    return False


class Password:
    def __init__(self, password_string):
        self.salt = bcrypt.gensalt()

        if not is_password_complex(password_string):
            raise ValueError('Password does not match complexity criteria.')

        self.hashed_password = self.hash_password(password_string)

    def hash_password(self, password_string):
        hashed_password = bcrypt.hashpw(password_string, self.salt)
        return hashed_password

    def hash_check(self, password_string):
        if hmac.compare_digest(self.hash_password(password_string), self.hashed_password):
            return True
        return False
