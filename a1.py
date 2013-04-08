def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(0)
    0
    >>> num_buses(51)
    2
    >>> num_buses(50)
    1
    >>> num_buses(1000)
    20
    """
    if n % 50 == 0:
        return n / 50
    else:
        return n / 50 + 1


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([])
    (0.0, 0.0)
    >>> stock_price_summary([0.01])
    (0.01, 0.0)
    >>> stock_price_summary([-0.32])
    (0.0, -0.32)
    """
    
    positive_changes = 0.0
    negative_changes = 0.0
    
    if price_changes:
        for item in price_changes:
            if item > 0:
                positive_changes += item
            else:
                negative_changes += item
    return (positive_changes, negative_changes)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    
    if L:
        if len(L) > 1:
            temp = L[0]
            L[0] = L[1]
            L[1] = temp


if __name__ == '__main__':
    import doctest
    doctest.testmod()
