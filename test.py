import unittest
from Password import Password
from User import User
import bcrypt


def get_password_hashes(*inputs):
    """Returns password hashes for all inputs (calculated using the same salt)"""
    all_hashes = []

    salt = bcrypt.gensalt()

    for ip in inputs:
        p = Password("".encode('utf-8'))

        p.salt = salt
        p.hashed_password = p.hash_password(ip.encode('utf-8'))
        hash_ = p.hashed_password

        all_hashes.append(hash_)

    return all_hashes


class TestPassword(unittest.TestCase):
    def testHash(self):
        # test if two equal inputs provide equal hashes
        hash1, hash2 = get_password_hashes("Test123", "Test123")
        self.assertEquals(hash1, hash2)

        # test if two different inputs provide two different hashes
        hash1, hash2 = get_password_hashes("Test123", "Test456")
        self.assertNotEqual(hash1, hash2)

    def testHashCheck(self):
        pwd = "MyTest".encode('utf-8')
        p = Password(pwd)

        self.assertTrue(p.hash_check(pwd))


class TestUser(unittest.TestCase):
    def testSetName(self):
        u1 = User()
        u1.set_name("MyName")

        self.assertEquals(u1.name, "MyName")

    def testGetName(self):
        u1 = User()
        u1.name = "MyName"

        self.assertEquals(u1.name, u1.get_name())

    def testGetHashedPassword(self):
        clear_pw = "MyPW".encode('utf-8')
        u1 = User()
        p1 = Password(clear_pw)
        u1.pw = p1

        self.assertEquals(p1, u1.get_password())

    def testSetHashedPassword(self):
        clear_pw = "MyPW2".encode('utf-8')
        u1 = User()
        p1 = Password(clear_pw)
        u1.set_password(p1)

        self.assertEquals(p1, u1.pw)


if __name__ == '__main__':
    unittest.main()
