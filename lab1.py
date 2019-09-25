def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""

    # None checking
    if int_list is None:
        raise ValueError()
    max_item = None
    for i in int_list:
        if max_item is None or i > max_item:
            max_item = i
    return max_item


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError()
    if len(int_list) == 0:
        return []
    x, *xs = int_list
    return reverse_rec(xs) + [x]


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return None

    assert low <= high, 'Low must be less than high'
    assert 0 <= low, 'Low is not in range'
    assert high < len(int_list), 'High not in range'

    if low == high:
        if int_list[low] == target:
            return low
        else:
            return None
    mid = (low + high) // 2
    low_val = int_list[low]
    mid_val = int_list[mid]
    high_val = int_list[high]

    assert low_val <= mid_val <= high_val, 'List is not sorted'

    if low_val == target:
        return low
    if high_val == target:
        return high
    if low_val <= target <= mid_val:
        return bin_search(target, low, mid, int_list)
    if mid_val <= target <= high_val:
        return bin_search(target, mid, high, int_list)
    return None
