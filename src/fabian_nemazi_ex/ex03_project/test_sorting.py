__author__ = 'Fabian Nemazi'
__email__ = 'fabinema@nmbu.no'



def bubble_sort(in_data):
    s_data = list(in_data)
    for j in reversed(range(len(s_data))):
        for k in range(j):
            if s_data[k + 1] < s_data[k]:
                s_data[k], s_data[k + 1] = s_data[k + 1], s_data[k]
    return s_data


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort(()) == []
    assert bubble_sort([]) == []


def test_single():
    """Testing that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """Testing that the sorting function returns a new object."""
    first_list = [3, 2, 1]
    new_list = bubble_sort(first_list)
    assert new_list != first_list


def test_original_unchanged():
    """Testing that sorting leaves the original data unchanged."""
    first_list = [28, 3, 4, 10, 8]
    bubble_sort(first_list)
    assert first_list == [28, 3, 4, 10, 8]

def test_sort_sorted():
    """Testing that sorting works on sorted data."""
    assert bubble_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]



def test_sort_reversed():
    """Testing that sorting works on reverse-sorted data."""
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]



def test_sort_all_equal():
    """Testing that sorting handles data with identical elements."""
    assert bubble_sort([1, 1, 1, 3, 4, 10, 2, 3]) == [1, 1, 1, 2, 3, 3, 4, 10]



