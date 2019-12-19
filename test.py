import unittest
from Password import Password
from User import User
import bcrypt


class TestPassword(unittest.TestCase):
    def testHash(self):
        p = Password()
        q = Password()

        mysalt = bcrypt.gensalt()
        p.salt = mysalt
        q.salt = mysalt

        pwd = "Test123".encode('utf-8')

        hash1 = p.hash_password(pwd)
        hash2 = q.hash_password(pwd)

        self.assertEquals(hash1, hash2)

    def testHashCheck(self):
        p = Password()

        pwd = "MyTest".encode('utf-8')
        hash_ = p.hash_password(pwd)

        self.assertTrue(p.hash_check(pwd, hash_))


class TestUser(unittest.TestCase):
    def testSetName(self):
        u1 = User()
        u1.set_name("MyName")

        self.assertEquals(u1.name, "MyName")

    def testGetName(self):
        u1 = User()
        u1.name = "MyName"

        self.assertEquals(u1.name, u1.get_name())

    def testGetPassword(self):
        u1 = User()
        u1.name = "MyName2"
        name = u1.get_name()

        self.assertEquals(name, "MyName2")

    def testSetPassword(self):
        u1 = User()
        p1 = Password()
        pwd = p1.hash_password("MyPW".encode('utf-8'))
        u1.set_password(pwd)

        self.assertEquals(pwd, u1.hashed_pw)


if __name__ == '__main__':
    unittest.main()
