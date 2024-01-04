# R-4.1 Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements. What is your running time and space usage?
# Tip: Don't forget about the sapce used by the function stack
# A:
# Input: a sequence S of n elements and a maximum element
# Output: the maximum element in S
# if n == 0: return max_element # base case (empty sequence)
# else: # recursive case (non-empty sequence)
#     if max_element is None: # first iteration (max_element is None)
#         max_element = S[n-1] # set max_element to the last element in S (n-1) 
#     elif S[n-1] > max_element: # if the last element in S is greater than max_element 
#         max_element = S[n-1] # set max_element to the last element in S (n-1) 
#     return maximum_element(S, n-1, max_element) # recursive call with n-1 and max_element as arguments 
# 
# Running time: O(n)
# Space usage: O(n)
def maximum_element(S, n, max_element=None): # max_element is None so that the first iteration can set max_element to the last element in S (n-1)
    """Return the maximum element in a sequence, S, of n elements."""
    if n == 0: # base case (empty sequence)
        return max_element # return max_element
    else: # recursive case (non-empty sequence)
        if max_element is None: # first iteration (max_element is None)
            max_element = S[n-1] # set max_element to the last element in S (n-1)
        elif S[n-1] > max_element: # if the last element in S is greater than max_element
            max_element = S[n-1] # set max_element to the last element in S (n-1)
        return maximum_element(S, n-1, max_element) # recursive call with n-1 and max_element as arguments

# R-4.2 Draw the recursion trace for the computation of power(2,5), using the traditional function implemented in Code Fragment 4.11.
# Tip: This is probably the first power algorithm you were taught.
# A:
# power(2, 5) = 2 * power(2, 4) = 2 * 16 = 32
#  power(2, 4) = 2 * power(2, 3) = 2 * 8 = 16
#   power(2, 3) = 2 * power(2, 2) = 2 * 4 = 8
#    power(2, 2) = 2 * power(2, 1) = 2 * 2 = 4 
#     power(2, 1) = 2 * power(2, 0) = 2 * 1 = 2
#      power(2, 0) = 1 # base case

# R-4.3 Draw the recursion trace for the computation of power(2,18), using the repeated squaring algorithm, as implemented in Code Fragment 4.12.
# Tip: Be sure to get the integer division right.
# A:
# power(2, 18) = power(2, 9) * power(2, 9) = 512 * 512 = 262144
#  power(2, 9) = power(2, 4) * power(2, 4) * power(2, 1) = 16 * 16 * 2 = 512
#   power(2, 4) = power(2, 2) * power(2, 2) = 4 * 4 = 16
#    power(2, 2) = power(2, 1) * power(2, 1) = 2 * 2 = 4
#     power(2, 1) = power(2, 0) * power(2, 0) * power(2, 1) = 1 * 1 * 2 = 2
#      power(2, 0) = 1 # base case
    
# R-4.4 Draw the recursion trace for the execution of function reverse(S, 0, 5) (Code Fragment 4.10) on S = [4, 3, 6, 2, 6].
# Tip: You can model your figure after Figure 4.11.
# A:
# reverse(S, 0, 5) # S = [4, 3, 6, 2, 6] # start = 0, stop = 5
#  reverse(S, 1, 4) # S = [(6), 3, 6, 2, (4)] # start = 1, stop = 4
#   reverse(S, 2, 3) # S = [(6), (3), 6, (2), (4)] # start = 2, stop = 3 (len(S)) # base case (start >= stop - 1)

# R-4.5 Draw the recursion trace for the execution of function PuzzleSolve(3, S, U) (Code Fragment 4.14), where S is empty and U = {a, b, c, d}.
# Tip: You should draw small boxes or use a big paper, as there are a lot of recursive calls.
# A:
# PuzzleSolve(3, S, U) # S = [], U = {a, b, c, d} # k = 3 (len(S)) # recursive case (k > 1)
    # PuzzleSolve(2, [a], {b, c, d}) # S = [a], U = {b, c, d} # k = 2 # recursive case (k > 1)
        # PuzzleSolve(1, [a, b], {c, d}) # S = [a, b], U = {c, d} # k = 1 # base case (k == 1) # abc, abd
        # PuzzleSolve(1, [a, c], {b, d}) # S = [a, c], U = {b, d} # k = 1 # base case (k == 1) # acb, acd
        # PuzzleSolve(1, [a, d], {b, c}) # S = [a, d], U = {b, c} # k = 1 # base case (k == 1) # adb, adc
    # PuzzleSolve(2, [b], {a, c, d}) # S = [b], U = {a, c, d} # k = 2 # recursive case (k > 1)
        # PuzzleSolve(1, [b, a], {c, d}) # S = [b, a], U = {c, d} # k = 1 # base case (k == 1) # bac, bad
        # PuzzleSolve(1, [b, c], {a, d}) # S = [b, c], U = {a, d} # k = 1 # base case (k == 1) # bca, bcd
        # PuzzleSolve(1, [b, d], {a, c}) # S = [b, d], U = {a, c} # k = 1 # base case (k == 1) # bda, bdc
    # PuzzleSolve(2, [c], {a, b, d}) # S = [a], U = {b, c, d} # k = 2 # recursive case (k > 1)
        # PuzzleSolve(1, [c, a], {b, d}) # S = [c, a], U = {b, d} # k = 1 # base case (k == 1) # cab, cad
        # PuzzleSolve(1, [c, b], {a, d}) # S = [c, b], U = {a, d} # k = 1 # base case (k == 1) # cba, cbd
        # PuzzleSolve(1, [c, d], {a, b}) # S = [c, d], U = {a, b} # k = 1 # base case (k == 1) # cda, cdb
    # PuzzleSolve(2, [d], {a, b, c}) # S = [a], U = {b, c, d} # k = 2 # recursive case (k > 1)
        # PuzzleSolve(1, [d, a], {b, c}) # S = [d, a], U = {b, c} # k = 1 # base case (k == 1) # dac, dab
        # PuzzleSolve(1, [d, b], {a, c}) # S = [d, b], U = {a, c} # k = 1 # base case (k == 1) # dba, dbc
        # PuzzleSolve(1, [d, c], {a, b}) # S = [d, c], U = {a, b} # k = 1 # base case (k == 1) # dca, dcb

def PuzzleSolve(k, S, U):
    """Print all k-length extensions made from elements in S and U."""
    if k == 1: # base case (k == 1)
        for x in U: # for each element in U
            print(S + [x]) # print all k-length extensions made from elements in S and U
    else: # recursive case (k > 1)
        for x in U: # for each element in U
            PuzzleSolve(k-1, S+[x], U-{x}) # recursive call with k-1, S+[x], and U-{x} as arguments

# R-4.6 Describe a recursive function for computing the nth Harmonic number, Hn = ∑ni=1 1/i.
# Tip: Start with the last term.
# A:
# Input: an integer n
# Output: the nth Harmonic number
# if n == 1: return 1 # base case (n == 1)
# else: return 1/n + harmonic_number(n-1) # recursive case (n > 1)
#
# Running time: O(n)
# Space usage: O(n)
def harmonic_number(n):
    """Return the nth Harmonic number."""
    if n == 1: # base case (n == 1)
        return 1 # return 1
    else: # recursive case (n > 1)
        return 1/n + harmonic_number(n-1) # recursive call with n-1 as argument

# R-4.7 Describe a recursive function for converting a string of digits into the integer it represents. For example, 13531 represents the integer 13,531.
# Tip: Process the string from left to right.
# A:
# Input: a string of digits
# Output: the integer it represents
# if n==0: return 0 # base case (empty string)
# else: return string_to_integer(s, n-1) * 10 + int(s[n-1]) # recursive case (non-empty string)
# 
# Running time: O(n)
# Space usage: O(n)
def string_to_integer(s, n):
    """Return the integer represented by a string of digits."""
    if n == 0: # base case (empty string)
        return 0 # return 0
    else: # recursive case (non-empty string)
        return string_to_integer(s, n-1) * 10 + int(s[n-1]) # recursive call with n-1 as argument

# R-4.8 Isabel has an interesting way of summing up the values in a sequence A of n integers, where n is a power of two.
# She creates a new sequence B of half the size of A and sets B[i] = A[2i]+A[2i+1], for i = 0,1,...,(n/2)−1.
# If B has size 1, then she outputs B[0]. Otherwise, she replaces A with B, and repeats the process.
# What is the running time of her algorithm?
# A: O(n) where n is a power of two (n = 2^k) because the algorithm divides the sequence in half each time it is called.
#

# C-4.9 Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loops.
# Tip: Consider returning a tuple, which contains both the minimum and maximum value.
# A:
# Input: a sequence S of n elements and a minimum and maximum element (min_element, max_element)
# Output: the minimum and maximum element in S (min_element, max_element)
# if n == 0: return min_element, max_element # base case (empty sequence)
# else: # recursive case (non-empty sequence)
#   if min_element is not Not None and min_element < S[n-1] then min_element = min_element else min_element = S[n-1]
#   if max_element is not Not None and max_element > S[n-1] then max_element = max_element else max_element = S[n-1]
#   return minimum_and_maximum_element(S, n-1, min_element, max_element) # recursive call with n-1, min_element, and max_element as arguments
#
# Running time: O(n)
# Space usage: O(n)
def min_max_element(S, n, min_element=None, max_element=None):
    """Return the minimum and maximum element in a sequence, S, of n elements."""
    if n == 0: # base case (empty sequence)
        return min_element, max_element # return min_element, max_element
    else:
        min_element = min_element if min_element and min_element < S[n-1] else S[n-1]
        max_element = max_element if max_element and max_element > S[n-1] else S[n-1]
        return min_max_element(S, n-1, min_element, max_element)

# C-4.10 Describe a recursive algorithm to compute the integer part of the base-two logarithm of n using only addition and integer division.
# Tip: The integer part of the base - two logarithm of n is the number of times n can be divided by 2 before getting a value that is less than 2.
# A:
# Input: an integer n
# Output: the integer part of the base-two logarithm of n (log2(n)) using only addition and integer division (//) 
# if n < 2: return 0 # base case (n < 2)
# else: return log2(n//2) + 1 # recursive case (n >= 2) # recursive call with n//2 as argument
# 
# Running time: O(n) where n is the integer part of the base-two logarithm of n (log2(n))
# Space usage: O(n) where n is the integer part of the base-two logarithm of n (log2(n))
def log2(n): 
    """Return the integer part of the base-two logarithm of n using only addition and integer division."""
    if n < 2: # base case (n < 2) 
        return 0 # return 0
    else: # recursive case (n >= 2) 
        return log2(n//2) + 1 # recursive call with n//2 as argument

# C-4.11 Describe an efficient recursive function for solving the element uniqueness problem, which runs in time that is at most O(n^2) in the worst case without using sorting.
# Tip: Consider reducing the task of telling if the elements of a sequence are unique to the problem of determining if the last n-1 elements are all unique and different than the first element.
# A:
# Input: a sequence S of n elements and a boolean unique (unique = True)
# Output: True if all elements in S are unique, False otherwise (unique)
# if n == 0: return unique # base case (empty sequence)
# else: # recursive case (non-empty sequence)
#   if S[n-1] in S[0:n-1]: unique = False else unique = True # if the last element in S is in the first n-1 elements of S then unique = False else unique = True
#   return unique_elements(S, n-1, unique) # recursive call with n-1 and unique as arguments
#
# Running time: O(n^2)
# Space usage: O(n^2)
def unique_elements(S, n):
    """Return True if all elements in S are unique, False otherwise."""
    if n == 0: # base case (empty sequence)
        return True # return True
    else: # recursive case (non-empty sequence)
        for i in range(0, n-1):
            if S[n-1] == S[i]: # if the last element in S is equal to any element in S[0:n-1]
                return False
        return unique_elements(S, n-1)

# C-4.12 Give a recursive algorithm to compute the produce of two positive integers m and n, usning only addition and subtraction.
# Tip: You need sutraction to count down from m or n and attion to do the arithmetic needed to get the right answer.
# A:
# Input: two positive integers m and n and a product (product = 0)
# Output: the product of m and n (product) using only addition and subtraction
# if n == 0: return product # base case (n == 0) 
# else: return product + m + multiply(m, n-1) # recursive case (n > 0) # recursive call with n-1 and product + m as arguments 
#
# Running time: O(n) where n is the product of m and n (m*n)
# Space usage: O(n) where n is the product of m and n (m*n)
def multiply(m, n, product=0):
    """Return the product of two positive integers m and n using only addition and subtraction."""
    if n == 0: # base case (n == 0) 
        return product # return product
    else: # recursive case (n > 0) 
        return multiply(m, n-1, product + m) # recursive call with n-1 and product + m as arguments

# C-4.13 In Section 4.2 we prove by induction that the number of lines printed by a call to draw interval(c) is 2^c−1.
    # Another interesting question is how many dashes are printed during that process.
    # Prove by induction that the number of dashes printed by draw interval(c) is 2^(c+1) - c - 2.
# Tip: Define a recurence equation
# A:
# Base case: c = 0 # 2^(c+1) - c - 2 = 2^(0+1) - 0 - 2 = 2 - 0 - 2 = 0
# Inductive step: c = k + 1
# 2^((k+1)+1) - (k+1) - 2
# 2^(k+2) - (k + 1) - 2
# 2^2 * 2^k - k - 3
# 4 * 2^k - k - 3

# C-4.14 In the Towers of Hanoi puzzle, we are given a platform with three pegs, a, b, and c, sticking out of it.
# On peg a is a stack of n disks, each larger than the next, so that the smallest is on the top and the largest is on the bottom.
# The puzzle is to move all the disks from peg a to peg c, moving one disk at a time, so that we never place a larger disk on top of a smaller one.
# See Figure 4.15 for an example of the case n = 4. Describe a recursive algorithm for solving the Towers of Hanoi puzzle for arbitrary n.
# Tip: Consider first moving all but the largest disk from peg a to another peg using the third peg as temporary storage.
# A:
# Input: a stack of n disks on peg a and pegs b and c (b and c are empty)
# Output: a stack of n disks on peg c (a and b are empty)
# if n == 1: move disk from peg a to peg c # base case (n == 1)
# else: # recursive case (n > 1)
#   move n-1 disks from peg a to peg b using peg c as temporary storage
#   move disk from peg a to peg b
#   move n-1 disks from peg c to peg b using peg a as temporary storage
#
# Running time: O(2^n)
# Space usage: O(2^n)
def towers_of_hanoi(n, a, b, c):
    """Move n disks from peg a to peg c using peg b as temporary storage."""
    if n == 1: # base case (n == 1)
        print('move disk from peg {0} to peg {1}'.format(a, b)) # move disk from peg a to peg b
    else: # recursive case (n > 1)
        towers_of_hanoi(n-1, a, c, b) # move n-1 disks from peg a to peg b using peg c as temporary storage
        print('move disk from peg {0} to peg {1}'.format(a, c)) # move disk from peg a to peg c
        towers_of_hanoi(n-1, c, b, a) # move n-1 disks from peg c to peg b using peg a as temporary storage

# C-4.15 Write a recursive function that will output all the subsets of a set of n elements (without repeating any subsets).
# Tip: Start by removing the first element x and computing all the sub-sets that don't contain x.
# A:
# Input: a set S of n elements, a number of elements n, and a subset s (s = [])
# Output: all the subsets of S without repeating any subsets (subsets)
# if n == 0: print s # base case (empty set)
# else: # recursive case (non-empty set)
#   for each element x in S:
#       S_minus_x = S - {x}
#       generate_subsets(S_minus_x, n - 1, s + [x])
#
# Running time: O(n^2) where n is the number of elements in S
# Space usage: O(n^2) where n is the number of elements in S
def generate_subsets(S, n, s): # s = [] so that the first iteration can set s to the first element in S
    print(s) # print s
    if n == 0: # base case (empty set)
        return # return
    for x in S: # for each element x in S
        S_minus_x = S - {x} # S_minus_x = S - {x}
        generate_subsets(S_minus_x, n - 1, s + [x]) # recursive call with S_minus_x, n - 1, and s + [x] as arguments

# C-4.16 Write a short recursive Python function that takes a cdharacter string s and outputs its reverse.
# For example the reverse of pots&pans would be snap&stop.
# Tip: You can use syntax print(ch, end='') to print one character at a time without extraneous spaces.
# A:
# Input: a character string s and length n
# Output: the reverse of s
# if n == 0: print empty string # base case (empty string)
# else: # recursive case (non-empty string)
#   print s[n-1] # print the last character in s
#   reverse(s, n-1) # recursive call with n-1 as argument
#
# Running time: O(n)
# Space usage: O(n)
def reverse(s, n):
    """Print the reverse of a character string s."""
    if n == 0: # base case (empty string)
        print() # print empty string
    else: # recursive case (non-empty string)
        print(s[n-1], end='') # print the last character in s
        reverse(s, n-1) # recursive call with n-1 as argument
        
# C-4.17 Write a short recursive Python function that determines if a string s is a palindrome, that is, it is equal to its reverse.
# For example, racecar and gohangasalamiimalasagnahog are palindromes.
# Tip: Check the equality of the first and last characters and recur (but be careful to return the correct value for both odd and even length strings).
# A:
# Input: a character string s start and stop indices (start = 0, stop = n-1) and a boolean is_palindrome (is_palindrome = True)
# Output: True if s is a palindrome, False otherwise)
# if start >= stop: return True # base case (start >= stop)
# else: # recursive case (start < stop)
#   if s[start] != s[stop]: is_palindrome = False else is_palindrome = True # if the first character in s is not equal to the last character in s then is_palindrome = False else is_palindrome = True
#   return palindrome(s, start+1, stop-1, is_palindrome) # recursive call with start+1, stop-1, and is_palindrome as arguments
#
# Running time: O(n)
# Space usage: O(n)
def palindrome(s, start, stop):
    """Return True if s is a palindrome, False otherwise."""
    if start >= stop: # base case (start >= stop)
        return True # return True
    else: # recursive case (start < stop)
        if s[start] == s[stop-1]: # if the first character in s is equal to the last character in s
            return palindrome(s, start+1, stop-1) # recursive call with start+1 and stop-1 as arguments
        else: # if the first character in s is not equal to the last character in s
            return False # return False

# C-4.18 Use recursion to write a Python function for determining if a string s has more vowels than consonants.
# Tip: Write your recursive function to first count vowels and consonants.
# A:
# Input: a character string s
# Output: True if s has more vowels than consonants, False otherwise
# if n==0: return vowels count, consonants count # base case (empty string)
# else: # recursive case (non-empty string)
#   if s[n-1] in vowels: vowels count += 1 else consonants count += 1 # if the last character in s is in vowels then vowels count += 1 else consonants count += 1
#   return vowels_and_consonants_count(s, n-1, vowels_count, consonants_count) # recursive call with n-1, vowels_count, and consonants_count as arguments
#
# Running time: O(n)
# Space usage: O(n)
def more_vowels_than_consonants(s, n, vowels_count=0, consonants_count=0):
    """Return True if s has more vowels than consonants, False otherwise."""
    if n == 0: # base case (empty string)
        return vowels_count > consonants_count # return True if vowels_count > consonants_count, False otherwise
    else: # recursive case (non-empty string)
        vowels = 'aeiouAEIOU' # vowels
        if s[n-1] in vowels: # if the last character in s is in vowels
            vowels_count += 1 # vowels count += 1
        else: # if the last character in s is not in vowels
            consonants_count += 1 # consonants count += 1
        return more_vowels_than_consonants(s, n-1, vowels_count, consonants_count) # recursive call with n-1, vowels_count, and consonants_count as arguments
        
# C-4.19 Write a short recursive Python function that rearranges a sequence of integer values so that all the even values appear before all the odd values.
# Tip: Consider whether the last element is odd or even and then put it at the appropriate location based on this and recur.
# A:
# Input: a sequence S of n elements, low and high indices (low = 0, high = n-1)
# Output: a sequence of integer values so that all the even values appear before all the odd values
# if low >= high: return S # base case (low >= high)
# else: # recursive case (low < high)
#   if S[high] % 2 == 0: # if the last element in S is even
#       S[low], S[high] = S[high], S[low] # swap the first and last elements in S
#       return rearrange_even_odd(S, low+1, high) # recursive call with low+1 and high as arguments
#   else: # if the last element in S is odd
#       return rearrange_even_odd(S, low, high-1) # recursive call with low and high-1 as arguments
#
# Running time: O(n)
# Space usage: O(n)
def rearrange_even_odd(S, low, high):
    """Return a sequence of integer values so that all the even values appear before all the odd values."""
    if low >= high: # base case (low >= high)
        return S # return S
    else: # recursive case (low < high)
        if S[high] % 2 == 0: # if the last element in S is even
            S[low], S[high] = S[high], S[low] # swap the first and last elements in S
            return rearrange_even_odd(S, low+1, high) # recursive call with low+1 and high as arguments
        else: # if the last element in S is odd
            return rearrange_even_odd(S, low, high-1) # recursive call with low and high-1 as arguments

# C-4.20 Given an unsorted sequence, S, of integers and an integer k,
# describe a recursive algorithm for rearranging the elements in S so that all elements less than or equal to k come before any element larger than k.
# What is the running time of your algorithm on a sequence of n values?
# Tip: Begin by comparing the first and last elements in a range of indices in A.
# A:
# Input: a sequence S of n elements, low and high indices (low = 0, high = n-1), and an integer k
# Output: a sequence of integers where all elements less than or equal to k come before any element larger than k
# if low >= high: return S # base case (low >= high)
# else: # recursive case (low < high)
#   if S[high] <= k: # if the last element in S is less than or equal to k
#       S[low], S[high] = S[high], S[low] # swap the first and last elements in S
#       return rearrange_elements(S, low+1, high, k) # recursive call with low+1, high, and k as arguments
#   else: # if the last element in S is greater than k
#       return rearrange_elements(S, low, high-1, k) # recursive call with low, high-1, and k as arguments
#
# Running time: O(n)
# Space usage: O(n)
def rearrange_elements(S, low, high, k):
    """Return a sequence of integers where all elements less than or equal to k come before any element larger than k."""
    if low >= high: # base case (low >= high)
        return S # return S
    else: # recursive case (low < high)
        if S[high] <= k: # if the last element in S is less than or equal to k
            S[low], S[high] = S[high], S[low] # swap the first and last elements in S
            return rearrange_elements(S, low+1, high, k) # recursive call with low+1, high, and k as arguments
        else: # if the last element in S is greater than k
            return rearrange_elements(S, low, high-1, k) # recursive call with low, high-1, and k as arguments
        
# C-4.21 Suppose you are given an n-element sequence, S, containing distinct integers that are listed in increasing order.
# Given a number k, describe a recursive algorithm to find two integers in S that sum to k, if such a pair exists.
# What is the running time of your algorithm?
# Tip: The beggining and the end of a range of indices in s can be used as arguments to your recursive function.
# A:
# Input: a sequence S of n elements, low and high indices (low = 0, high = n-1), and an integer k
# Output: two integers in S that sum to k, if such a pair exists
# if low >= high: return None # base case (low >= high)
# else: # recursive case (low < high)
#   if S[low] + S[high] == k: return S[low], S[high] # if the first and last elements in S sum to k then return the first and last elements in S
#   elif S[low] + S[high] < k: return find_sum(S, low+1, high, k) # if the first and last elements in S sum to less than k then recursive call with low+1, high, and k as arguments
#   else: return find_sum(S, low, high-1, k) # if the first and last elements in S sum to greater than k then recursive call with low, high-1, and k as arguments
#
# Running time: O(n)
# Space usage: O(n)
def find_sum(S, low, high, k):
    """Return two integers in S that sum to k, if such a pair exists."""
    if low >= high: # base case (low >= high)
        return None # return None
    else: # recursive case (low < high)
        if S[low] + S[high] == k: # if the first and last elements in S sum to k
            return S[low], S[high] # return the first and last elements in S
        elif S[low] + S[high] < k: # if the first and last elements in S sum to less than k
            return find_sum(S, low+1, high, k) # recursive call with low+1, high, and k as arguments
        else: # if the first and last elements in S sum to greater than k
            return find_sum(S, low, high-1, k) # recursive call with low, high-1, and k as arguments

# C-4.22 Develop a nonrecursive implementation of the version of power from Code Fragment 4.12 that uses repeated squaring.
# Tip: You can rely on bitwise operations to interpret n in binary.
# A:
# Input: two integers x and n
# Output: x^n
# result = 1
# while n > 0:
#   if n % 2 == 1: result *= x
#   x *= x
#   n //= 2
# return result
#
# Running time: O(n)
# Space usage: O(n)
def power(x, n):
    """Return x^n."""
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result

# P-4.23 Implement a recursive function with signature find(path, filename) that reports all entries of the file system rooted at the given path having the given file name.
# Tip: Review use of the os module.

# P-4.24 Write a program for solving summation puzzles by enumerating and testing all possible configurations.
# Using your program, solve the three puzzles given in Section 4.4.3.
# Tip: Use recursion in your main solution engine.
        
# P-4.25 Provide a nonrecursive implementation of the draw interval function for the English ruler project of Section 4.1.2.
# There should be precisely 2^c−1 lines of output if c represents the length of the center tick.
# If incrementing a counter from 0 to 2^c−2, the number of dashes for each tick line should be exactly one more than the number of consecutive 1’s at the end of the binary representation of the counter.
# Tip: Consider a small example to see why the binary representation of the counter is relevant.

# P-4.26 Write a program that can solve instances of the Tower of Hanoi problem (from Exercise C-4.14).
# Tip: Note the recursive nature of the problem.

# P-4.27 Python's os module provides a function with signature walk(path) that is a generator yielding the tuple (dirpath, dirnames, filenames) for each subdirectory of the directory identified by string path, such that string dirpath is the full path to the subdirectory, dirnames is a list of the names of the subdirectories within dirpath, and filenames is a list of the names of non-directory entries of dirpath.
# For example, when visiting the cs016 subdirectory of the file system shown in Figure 4.6, the walk would yield ('/user/rt/courses/cs016', ['homeworks', 'programs'], ['grades']) Give your own implementation of such a walk function.
# Tip: Review use of the other methods of the os module.