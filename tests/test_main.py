import operator
import unittest
import os


class TestMain(unittest.TestCase):
    def test_num(self):
        # env python3 3.9.2
        a_num = 0x12345678901234567890123456789012345678901234567890123456789012345678901234567890
        b_num = 0x987654431234567890123456789012345678901234567890123456789012345678901234567890
        self.assertGreater(a_num, b_num)
        print(operator.gt(str(a_num), str(b_num)))  # False
        # == python2 cmp(str(a_num), str(b_num)) >> eq <- 0 gt <- 1 lt <- -1
        self.assertLess(id(a_num), id(b_num))

        # self.assertTrue(operator.gt(str(a_num), str(b_num)))
        # self.assertTrue()


if __name__ == '__main__':
    unittest.main()
