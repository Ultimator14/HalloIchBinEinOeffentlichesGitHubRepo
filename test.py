import unittest
from Password import Password
from User import User
import bcrypt


class TestPassword(unittest.TestCase):
    @staticmethod
    def getPasswordHashes(*inputs):
        """Returns password hashes for all inputs (calculated using the same salt)"""
        all_hashes = []

        mysalt = bcrypt.gensalt()

        for ip in inputs:
            p = Password()
            p.salt = mysalt
            pwd = ip.encode('utf-8')
            hash_ = p.hash_password(pwd)

            all_hashes.append(hash_)

        return all_hashes

    def testHash(self):
        # test if two equal inputs provide equal hashes
        hash1, hash2 = self.getPasswordHashes("Test123", "Test123")
        self.assertEquals(hash1, hash2)

        # test if two different inputs provide two different hashes
        hash1, hash2 = self.getPasswordHashes("Test123", "Test456")
        self.assertNotEqual(hash1, hash2)

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
