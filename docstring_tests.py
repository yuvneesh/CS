# Demonstrating testing functions with tests included within docstring

def is_a_triangle(a: float, b: float, c: float)->bool:
    """
    Returns true if there exists a triangle with non-zero side lengths a, b, and c
    >>> is_a_triangle(3,4,5)
    True
    >>> is_a_triangle(1,3,5)
    False
    >>> is_a_triangle(1,5,3)
    False
    >>> is_a_triangle(5,1,3)
    False
    """
    case1 = a + b > c
    case2 = a + c > b
    case3 = b + c > a

    return case1 and case2 and case3

# The test cases used for this function were constructed as follows:
# Test-1: Using side lengths of a known triangle. So we know that case1,case2,case3 are all True
# Test-2: only case1 fails
# Test-3: only case2 fails
# Test-4: only case3 fails
