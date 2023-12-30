# Chapter 4

***What is recursion?***
Recursion is a technique by which a function makes one or more calls to itself during execution or by which a data structure relies upon smaller instances of the same type of structure in its representation.

***How do most modern programming languages support functional recursion?***
Using the identical mechanism used to support traditional forms of function calls. When one invocation of the function makes a recursive call, the invocation suspends until the recursive call completes.

***What are 4 examples of recursion?***
1. Factorial Function
2. English Ruler
3. Binary Search
4. File Systems

## 4.1 Illustrative Examples

### 4.1.1 The Factorial Function

***What is a factorial?***
The factorial of a positive integer *n*, denoted *n*!, is defined as the product of the integers from 1 to n. If *n*=0, then n! is defined as 1 by convetion. More formally for any intger n≥0,
$$
n! = \begin{cases}
    1 & \text{if } n = 0 \\
    n \cdot (n-1) \cdot (n-2) \cdot\cdot\cdot 3 \cdot 2 \cdot 1 & \text{if } n \geq 1
\end{cases}
$$

***What is the factorial used for?***
Used to know the number of ways you can arrange *n* distinct items into a sequence: the number of permutations of *n* items.

***What is the recursive defintion of the fatorial funtion?***
$$
n! = \begin{cases}
    1 & \text{if } n = 0 \\
    n \cdot (n-1)! & \text{if } n \geq 1
\end{cases}
$$

***How is a base case defined?***
A base case is defined non-recursively in terms of fixed quantities.

***How is the recursive case defined?***
You define a recursive case by appealing to the function definition.

#### A recursive Implementation of the Factorial Funtion

***What is a recursive Implementation of the factorial funtion?***
```python
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
```

***What does a recursion trace do?***
It illustrates the execution of a recursive funtion.Each entry of the trace corresponds to a recursive call. It illustrates the execution of a recursive function. Each entry of the trace corresponds to a recursive call. A downward arrow indicates each new recursive function call to a new invocation. When the function returns, you draw an arrow showing this return. You may indicate the return value alongside this arrow.
```
factorial(4)
    factorial(3)
        factorial(2)
            factorial(1)
                return 1
            return 2 * 1 = 2
        return 3 * 2 = 6
    return 4 * 6 = 24
```

***What structure is created each time a function (recursive or otherwise) is called that stores information about the progress of that invocation of the function? What does it include?***
Activation record, or frame. It includes a namespace for storing the function call's parameters, local variables, and information about which command in the function's body is executing.

***What happens when the execution of a function leads to a nested function call?***
The program suspends the execution of the former call, and its activation record stores the place in the source code where the flow of control should continue upon the return of the nested call.

### 4.1.2 Drawing an English Ruler

***What is the major tick length of an English Ruler?***
Lenght of the tick designating a whole inch.

***What is a minor tick on an English Ruler?***
A series of marks between whole inches placed at intervals of 1/2 inch, 1/4 inch, and so on.

***How do the tick marks of a ruler work?***
As the size of the interval decreases by half the tick length decreases by one.

#### A recursive Approach to Ruler Drawing
***What is a fractal?***
A shape that has a self-recursive structure at various levels of magnification.

***What is the fractal pattern of an English Ruler?***
An interval with a central tick length L≥1 is composed of L
- an interval with a central tick length L-1
- a single tick of length L
- an interval with a central tick length L-1

***What is Python Implementation of an English Ruler?***
```python
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
```

### 4.1.3 Binary Search
***What is binary search***
A recursive algorithm used to locate a target value efficiently within a sorted sequence of *n* elements.

***What is sequential search? What is the run time?***
Approach to searching for a target value in an unsorted sequence using a loop to examine every element until either finding the target or exhausting the data set. Runs in *O(n)*.

***What is the advantage of a sorted and indexable sequence?***
There is a more efficient algorithm for search.

***What is an element of a sequence called if, at the current stage of the search, we cannot rule out that this item matches the target?***
The candidate.

***What two parameters does binary search maintain? What is the initial condition? What is used to compare?***
low and high, such that all candidate entries have an index at least low and at most high. Initially, low = 0 and high = n-1. We compare the target value to the median candidate, that is, the item data[mid] with index mid = [(low+high)/2]

***What are the three cases to consider in binary search? When does an unsucesful search occur?***
- If the target equals data[mid], we have found the item we seek, and the search terminates successfully.
- If target < data[mid], then we recur on the first half of the sequence, that is, on the interval of indices from low to mid -1. 
- If target > data[mid], then we recur on the second half of the sequence, that is, on the interval of indices from mid +1 to high.
- An unsuccessful search occurs if low > high, as the interval [low, high] is empty.

***What is an implementation of binary search? What is the run time?***
```python
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
```
*O(log(n))*

### 4.1.4 File Systems
***What does a file system consist of?***
A top-level directory, and the contents of this directory are comprised of files and other directories, which, in turn, can contain files and other directories, and so on.

***What is the pseudo-code to compute cumulative disk space recursively for an entry?***
```code
Algorithm DiskUsage(path):
Input: A string designating a path to a file system entry
Output: The cumulative disk space used by that entry and any nested entries
total = size(path)
if path represents a directory then
    for each child entry stored within directory path do
        total = total + DiskUsage(child) {recursive call}
    return total
```

#### Python's OS Module
***What does `os.path.getsize(path)` do?***
Return the immediate disk usage (measured in bytes) for the file or directory that is identified by the string path.

***What does `os.path.isdir(path)` do?***
Return `True` if entry designated bys tring path is a directory; False otherwise.

***What does `os.listdir(path)` do?***
Return a list of string that are the names of all entires within a directory designated by string path.

***What does `os.path.join(path, filename)` do?***
Composes the path string and file name string using an appropriate operating system separatore between the two (e.g. the / character for a unix linus system and the \ character for windows). Returns the string that represents the full path to the file.

***How do you implement DiskUsage in Python?***
```python
def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)           # account for direct usage
    if os.path.isdir(path):                 # if this is a directory,
        for filename in os.listdir(path):   # then for each child:
            childpath = os.path.join(path, filename) # compose full path to child
            total += disk_usage(childpath)  # add child's usage to total
    print('{0:<7}'.format(total), path)     # descriptive output (optional)
    return total
```

## 4.2 Analyzing Recursive Algorithms

***How do you analyze run time for recursive algorithms?***
For each function invocation, we only account for the number of operations performed within the body of that activation. We can then account for the overall number of operations executed as part of the recursive algorithm by taking the sum of all activations of the number of operations during each activation.

#### Computing Factorials
***What is the run time of factorial?***
Factorials is O(n)
N+1 activations as parameters decrease from n in the first call to n-1 until reaching the base case. Each activation executes a constant number of operations.

#### Drawing an English Ruler
***What is the run time of English Ruler?***
Proof by induction
for c≥0 a call to draw_interval(c) results in precisely 2<sup>c</sup>-1 lines of output thus
$$
1 + 2(2^{c-1} - 1) = 1 + 2^{c} - 2 = 2^{c} - 1
$$

#### Performing Binary Search
***what is the run time of binary search?***
O(log(n))

#### Computing DiskUsage Space
***What is the run time of directory search?***
O(n)

## 4.3 Recursion Run Amok
***What makes recursion inefficient? How do you make recursion efficient?***
Multiple calls to the recur step. Reduce the recursive call invocaitons.

***What is an inefficient recursion for computing fibonnacci numbers? Why? What is the run time?***
```python
def unique3(S, start, stop):
    """Return True if there are no duplicate elements in slice S[start:stop]."""
    if stop - start <= 1: return True       # at most one item
    elif not unique3(S, start, stop-1): return False # first part has duplicate
    elif not unique3(S, start+1, stop): return False # second part has duplicate
    else: return S[start] != S[stop-1]      # do first and last differ?
```
The calls grow to geometric summation in the worst case.
O(2<sup>*n*</sup>)

***What is an inefficient recursion for computing fibonnacci numbers? Why? What is the run time?***
```def bad_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)
```
Computing the *n*<sup>th</sup> Fibonacci number creates exponential calls.
O(2<sup>*n*</sup>)

***What is an efficient recursion for computing fibonacci numbers? Why? What is the run time?***
```python
def good_fibonacci(n):
    """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)
```
Avoids duplicating work.
*O(n)*

***What is infinite recursion? What are examples of infinite recursion?***
When each recursive call makes another recursive call without ever reaching a base case creating an infinite series of such calls.
```python
def fib(n):
    return fib(n)

def binary_searrch
    # ...
    return binary_search(data, target, mid, high)
```

***How do you prevent infinite recursion***
Ensure that each recursive call is in some way progressing toward a base case.

***What error is received when Python's recursion limit is reached?***
RuntimeError with message "maximum recurion depth exceeded."

***How can you set Python recursion limit for legitimate computations?***
```python
import sys
old = sys.gerrecursionlimit()
sys.setrecursionlimit(1000000)
```

## 4.4 Further Examples of Recursion
### 4.4.1 Linear Recursion
***What is linear recursion? What are some exmaples?***
Recursive function designed sot hat each invocation of the body makes at most one new recursive call.
- Factorial
- Good Fibonacci
- Binary search

***What structure does and does linear recursion not reflect?***
Recursion trace, not the asymptotic analysis of the running time.

### Summing the Elements of a Sequence Recursively

***What is linear recursion helpful for?***
Processing a data Sequence such as a Python list.

***What is a recursive algorithm for computing the sum of a sequence? What is the run time?***
```python
def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]
```
*O(n)*

### Reversing a Sequence with Recursion

***What is an implementation to sum elements of a sequence recursively? What are the two implied base cases?***
```python
def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start < stop - 1:                    # if at least 2 elements:
        S[start], S[stop-1] = S[stop-1], S[start] # swap first and last
        reverse(S, start+1, stop-1)         # recur on rest
```
The implicit range is empty, or has one lement.
If n is even start-stop caise if n is odd start==stop-1.

***What is the definition and trivial implementation of computing powers? What is the memory?What is the run time?***
$$
power(x,n) = \begin{cases}
    1 & \text{if } n = 0 \\
    x \cdot power(x,n-1) & \text{otherwise. } 
\end{cases}
$$
```python
def power(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
```
- memory *O(n)*
- runtime *O(n)*

***What is a more efficient definition and implementation computing powers? What is the runtime? What is the memory?***
$$
power(x,n) = \begin{cases}
    1 & \text{if } n = 0 \\
    x \cdot (power(x,[n/2]))^2 & \text{if } n>0 \text{ is odd} \\
    (power(x,[n/2]))^2 & \text{if } \text{ is even}
\end{cases}
$$
```python
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
```
- memory *Olog(n)*
- runtime *Olog(n)*

## 4.4.2 Binary Recursion
***What is binary recursion?***
When a recursive function makes two recursive calls.

***What is an implimentation of binary sum? What is the memory? What is the runtime?***
```python
def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]."""
    if start >= stop:                       # zero elements in slice
        return 0
    elif start == stop - 1:                 # one element in slice
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
```
- memory *Olog(n)*
- runtime *O(n)*

## 4.4.3 Multiple Recursion
***What is multiple recursion?***
Process in which a funtion may make more than two recursive calls.

***What is a common application of multiple recursion?***
When we want to enumerate various configurations to solve a combinatorial puzzle.

***What is the pseudocode for PuzzleSOlve?***
#TODO

# 4.5 Designing Recursive Algorithms
***What is the typical form of a rucursion algorithm?***
- *Test for base case.* Begin bu testing a set of basecases. There should be at least oone. Base case defined so that every possible chain of recursive calls will eventually reach a abse case. The handling of each base cas shoul not use recursion.
- *Recur* if not base case perform one or more recursive calls. The recursive step may involve a test that decides which of several possible recursive call to make. We should define each possible recursive calls so that it makes progress towards the base case.

#### Paramterizing a Recursion
***How to design a recursive algorith problem?***
think of different ways we mi9ght define subproblmes that have the same general structures as the original problem. It's usfule to work out a few concrete examples to see how subporblmens should be designed.

***What might sometimes be needed to faciiliatet similar looking subproblems?***
Reparameterize the signature of the function?

***What is a patter to provide cleaner public interfaces to algorithms like binary search?***
Make one function for public us with the cleaner interface and the body invoking a nonpublic utility funtion havein desired recursive parameters.

## 4.6 Eliminating Tail Recursion
***What is the main benefit of a recursive approach to algorithm design?***
It allows us to succinctly take advantage ofa  repetitive structure present in many problems. The apporach can lead to more readable algorithm descriptions exploiting the repetitive structure in a recursive way whil still being quiete efficient.

***What is the cost of recursions?***
Maintaining activation records taht keep track of the state of each nested call.

***How can you reduce the memory usage?***
Storing only the minimal infomation necessary using the stack data sturcture to conver a recusive algorithm into a non recursive algoritm by managing the neeing of the recursive structure ourselves.
#TODO p178

***What is a tail recursion***
If any recursive call that is made from one context is the very last operation in that context with the return value of the recursive calll if any immeidately retunred by encosling recurion it must be linear.

***How can you reimplement tail recursions non-recursively?***
Enclosing the body ina  loop for repetition and replacing a recursive call with new parameters by reassignemetn of the existing parameters to those values.

***How do you implement a non-recursive binary search?***
#TODOp.179

***How do you implement a non-recursive reversal of elements?***
#TODOp.179