# 4.1.1 The factorial funtion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# 4.1.2 Drawing an English ruler
def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)."""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:                   # stop when length drops to 0
        draw_interval(center_length - 1)    # recursively draw top ticks
        draw_line(center_length)            # draw center tick
        draw_interval(center_length - 1)    # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')            # draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)     # draw interior ticks for inch
        draw_line(major_length, str(j))     # draw inch j line and label

# 4.1.3 Binary search
def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False                        # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:             # found a match
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)

# 4.1.4 File system
import os
def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)           # account for direct usage
    if os.path.isdir(path):                 # if this is a directory,
        for filename in os.listdir(path):   # then for each child:
            childpath = os.path.join(path, filename) # compose full path to child
            total += disk_usage(childpath)  # add child's usage to total
    print('{0:<7}'.format(total), path)     # descriptive output (optional)
    return total

# 4.3 Recursion Run Amok
def unique3(S, start, stop):
    """Return True if there are no duplicate elements in slice S[start:stop]."""
    if stop - start <= 1: return True       # at most one item
    elif not unique3(S, start, stop-1): return False # first part has duplicate
    elif not unique3(S, start+1, stop): return False # second part has duplicate
    else: return S[start] != S[stop-1]      # do first and last differ?

# An ineffficient recursive function for computing the Fibonacci number
def bad_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)

# An efficient recursive function for computing the Fibonacci number
def good_fibonacci(n):
    """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)

# Summing the elements of a Sequence Recursively
def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

# Reversing a Sequence with Recursion
def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start < stop - 1:                    # if at least 2 elements:
        S[start], S[stop-1] = S[stop-1], S[start] # swap first and last
        reverse(S, start+1, stop-1)         # recur on rest

# Recursive Algorithms for Computing Powers
# Code fragment 4.11
def power(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

# Code fragment 4.12
def power2(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power2(x, n//2)           # rely on truncated division
        result = partial * partial
        if n % 2 == 1:                      # if n odd, include extra factor of x
            result *= x
        return result
# 4.4.2 Binary Recursion
def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]."""
    if start >= stop:                       # zero elements in slice
        return 0
    elif start == stop - 1:                 # one element in slice
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

    