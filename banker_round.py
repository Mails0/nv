import math
import unittest


def banker_round(value, decimal=0):
    return round((value + 0.00000001), decimal)


class TestRound(unittest.TestCase):

    def test_banker_round(self):
        for i in range(1000):
            for n in range(10):
                self.assertEqual(banker_round(float(f'{i}.{n}') + 0.05, 1), round(float(f'{i}.{n}') + 0.1, 1),
                                 "Should be rounded up")


if __name__ == '__main__':
    unittest.main()
