from operator import add, sub
from unittest import TestCase, main
from sfp import tail, pipe, zipwith


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


class TestZipWith(TestCase):
    def test_should_concat_two_sequences_using_add(self):
        zip_function = zipwith(add)
        self.assertEqual(list(zip_function([1, 2, 3], [4, 5, 6])),
                         [5, 7, 9])

    def test_should_works_when_len_of_iterables_is_not_the_same(self):
        zip_function = zipwith(sub)
        lst_a = [0, 1, 2]
        lst_b = [0, 1, 2, 3]
        expected = [0, 0, 0]
        self.assertEqual(list(zip_function(lst_a, lst_b)), expected)

    def test_pipe_should_return_a_callable(self):
        """Check if pipe is a closure."""
        _callable = zipwith(lambda x: x)

        self.assertTrue(hasattr(_callable, '__call__'))


if __name__ == '__main__':
    main()
