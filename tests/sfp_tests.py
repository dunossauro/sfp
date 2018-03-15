from unittest import TestCase, main
import sys
sys.path.append('../')

from sfp import *


class tests(TestCase):

    def test_pipe(self):
        resul = pipe(
            lambda x: x ** 2,
            lambda x: x * 5,
            lambda x: x // 5
        )(5)

        self.assertEqual(resul, 25)


if __name__ == '__main__':
    main()
