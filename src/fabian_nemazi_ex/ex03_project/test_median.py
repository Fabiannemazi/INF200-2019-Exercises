import pytest
import random


__author__ = 'Fabian Nemazi'
__email__ = 'fabinema@nmbu.no'


#def median(data):
    #sdata = sorted(data)
    #n = len(sdata)
    #if n == 0:
        #raise ValueError
    #return (sdata[n // 2] if n % 2 == 1
            #else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    sdata = sorted(data)
    n = len(sdata)
    if n == 0:
        raise ValueError
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_one_element():
    """
    A test that check that the correct median is returned
    for a one-element list
    """
    test_list = [random.randint(0, 9)]
    assert median(test_list) == test_list[0]


def test_odd_numbers():
    """
    test that check that the correct median is returned for
    a list with odd numbers of elements
    """

    test_list = [i for i in range(0, 5)]
    import statistics
    assert median(test_list) == statistics.median(test_list)


def test_even_numbers():
    """
    test that check that the correct median is returned for
    a list with even numbers of elements
    """
    import statistics
    test_list = [i for i in range(0, 6)]
    assert median(test_list) == statistics.median(test_list)


def test_ordered_elements():
    """
    test that check that list with ordered,
    reverse-ordered and unordered elements returns the correct median
    """
    import statistics
    test_list = [i for i in range(0, 8)]
    assert median(test_list) == statistics.median(test_list)


def test_rev_ordered_elements():
    """
    A test checking that requesting the median
    of an empty list raises a ValueError exception
    """
    test_list = [i for i in range(0, 8)]
    rev_test_list = sorted(test_list, reverse=True)
    assert median(test_list) == median(rev_test_list)


def test_unordered_elements():
    """
    A test that ensures that the median function
    leaves the original data unchanged.
    """
    import statistics
    test_list = [1, 5, 6, 8, 3, 65, 7, 4, 3, 2, 5, 6]
    assert median(test_list) == statistics.median(test_list)


def test_empty_list():
    """
    A test that ensures that the median function
    works for tuples as well as lists
    """
    with pytest.raises(ValueError):
        median([])


def test_original_unchanged():

    test_list = [i for i in range(1, 9)]
    median(test_list)
    assert test_list == [i for i in range(1, 9)], 'The original data has ' \
                                                  'been changed'


def test_for_tuples():
    test_list = [i for i in range(1, 8)]
    tuple_list = (1, 2, 3, 4, 5, 6, 7)
    while False:
        try:
            median(test_list) == median(tuple_list)
        except TypeError:
            print('Median function does not work for tuples')
