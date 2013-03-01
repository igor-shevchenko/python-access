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

        class B(A):
            def get_parent_protected(self):
                return self.protected()

        class C:
            def get_protected(self):
                a = A()
                return a.protected()

        self.A = A
        self.B = B
        self.C = C

    def test_inner_access(self):
        a = self.A()
        self.assertEqual(a.public(), self.SECRET_VALUE)

    def test_child_access(self):
        b = self.B()
        self.assertEqual(b.get_parent_protected(), self.SECRET_VALUE)

    def test_fail_access_from_outer_class(self):
        c = self.C()
        self.assertRaises(Exception, c.get_protected)

    def test_fail_outer_access(self):
        a = self.A()
        self.assertRaises(Exception, a.protected)


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

        class B(A):
            def get_parent_private(self):
                return self.private()

        class C:
            def get_private(self):
                a = A()
                return a.private()

        self.A = A
        self.B = B
        self.C = C

    def test_inner_access(self):
        a = self.A()
        self.assertEqual(a.public(), self.SECRET_VALUE)

    def test_child_access(self):
        b = self.B()
        self.assertRaises(Exception, b.get_parent_private)

    def test_fail_access_from_outer_class(self):
        c = self.C()
        self.assertRaises(Exception, c.get_private)

    def test_fail_outer_access(self):
        a = self.A()
        self.assertRaises(Exception, a.private)


if __name__ == '__main__':
    unittest.main()