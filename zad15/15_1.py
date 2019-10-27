N = 5
def factorial(num):
    if num == 1: return 1
    return num * factorial(num-1)

class Perm:
    def __init__(self, list_of_perms):
        self.perms = list_of_perms

    def __mul__(self, perm):
        return Perm([self.perms[perm.perms[i]] for i in range(N)])

    def invert_perm(self):
        return Perm([self.perms.index(i) for i in range(N)])

    def is_identity(self):
        return all(i == self.perms[i] for i in range(N))

    def find_order(self):
        return factorial(N)

import unittest

class TestPerm(unittest.TestCase):
    def setUp(self):
        self.p1 = Perm([0,1,2,3,4])
        self.p2 = Perm([4,3,2,1,0])
        self.p3 = Perm([0,1,4,2,3])

    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_init(self):
        self.assertEqual(self.p1.perms, [0,1,2,3,4])
        self.assertEqual(self.p2.perms, [4,3,2,1,0])

    def test_mul(self):
        self.assertEqual((self.p1 * self.p2).perms, [4,3,2,1,0])
        self.assertEqual((self.p2 * self.p1).perms, [4,3,2,1,0])
        self.assertEqual((self.p1 * self.p1).perms, [0,1,2,3,4])
        self.assertEqual((self.p2 * self.p2).perms, [0,1,2,3,4])

    def test_invert(self):
        self.assertEqual(self.p1.invert_perm().perms, self.p1.perms)
        self.assertEqual(self.p2.invert_perm().perms, self.p2.perms)
        self.assertEqual(self.p3.invert_perm().perms, [0,1,3,4,2]) 

    def test_identity(self):
        self.assertTrue(self.p1.is_identity())
        self.assertFalse(self.p2.is_identity())
        self.assertFalse(self.p3.is_identity())

if __name__ == "__main__":
    unittest.main()
