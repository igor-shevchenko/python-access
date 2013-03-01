# This test cases demonstrate the bad consequences of some assumptions made in access.py
import unittest
import access


class ProtectedTest(unittest.TestCase):

    def setUp(self):
        self.SECRET_VALUE = 'spam'
        value = self.SECRET_VALUE

        class A:
            @access.protected
            def protected(self):
                return value
            def public(self):
                return self.protected()
        self.A = A

    def test_access_with_fake_self(self):
        class B:
            def get_protected(this, self):
                return self.protected()
        a = self.A()
        b = B()
        self.assertRaises(Exception, b.get_protected, a)


class PrivateTest(unittest.TestCase):

    def setUp(self):
        self.SECRET_VALUE = 'spam'
        value = self.SECRET_VALUE

        class A:
            @access.private
            def private(self):
                return value
            def public(self):
                return self.private()
        self.A = A

    def test_access_with_fake_self(self):
        class B:
            def get_private(this, self):
                return self.private()
        a = self.A()
        b = B()
        self.assertRaises(Exception, b.get_private, a)

    def test_access_from_same_named_child(self):
        class A(self.A):
            def get_private(self):
                return self.private()
        self.assertRaises(Exception, A().get_private)


if __name__ == '__main__':
    unittest.main()
