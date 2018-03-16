from unittest import TestCase, main
from sfp import tail, head


class testTail(TestCase):
    def test_should_get_tail_to_list(self):
        self.assertEqual(tail([1, 2, 3, 4]), [2, 3, 4])

    def test_should_get_tail_to_iterable(self):
        result = tail(iter([1, 2, 3, 4]))
        self.assertEqual(result, [2, 3, 4])


class TestHead(TestCase):
    def test_get_head_list(self):
        self.assertEqual(head([1, 2, 3, 4]), [1])
        self.assertEqual(head([1, 2, 3, 4], 3), [1, 2, 3])

    def test_get_head_string(self):
        self.assertEqual(head("Olá BB!", 3), "Olá")
        self.assertNotEqual(head("@python", 4), "@pyth")


if __name__ == '__main__':
    main()
