from unittest import TestCase, main
from sfp import tail, pipe


class testTail(TestCase):
    def test_should_get_tail_to_list(self):
        self.assertEqual(tail([1, 2, 3, 4]), [2, 3, 4])

    def test_should_get_tail_to_iterable(self):
        result = tail(iter([1, 2, 3, 4]))
        self.assertEqual(result, [2, 3, 4])

    def test_should_reaturn_blank_sequece(self):
        self.assertEqual(tail([]), [])


class testsPipe(TestCase):
    def test_pipe_should_return_a_callable(self):
        """Check if pipe is a closure."""
        _callable = pipe(lambda x: x)

        self.assertTrue(hasattr(_callable, '__call__'))

    def test_pipe_should_return_the_same_value_using_indentity_function(self):
        self.assertEqual(pipe(lambda x: x)(5), 5)

    def test_pipe_sequence_funtions_executions(self):
        resul = pipe(
            str.split,
            len,
            lambda x: x + 5
        )('eduardo mendes')

        self.assertEqual(resul, 7)


if __name__ == '__main__':
    main()
