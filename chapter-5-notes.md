# Chapter 5 Array-Based Sequences
## 5.1 Python's Sequence Types

***What are the Python built-in sequence classes?***
- list
- tuple
- str

***What are the two most notable commonailities each sequence class supports?***
- indexing and accessing sequence element using seq[k]
- represented by low-level concept known as an array

#### Public Behaviors

***What can happen if important subltleties regarding beahaviors associated with these classes are misunderstood?***
Inadvertent bugs in the program.

#### Implementation Details
***What is encapsulation?***
Needing not to know about the internal details of an implementation.

#### Asymptotic and Experimental Aanalysis
***What do we rely on in descibing efficiency of various operations for Python's Sequene classes?***
Asymptotic Analysis

## 5.2 Low-Level Arrays
***What is the primary memomry of a computer composed of?***
bits

***What is a byte equivalent to?***
8 bits

***What is the memory address abstraction used for?***
keeps track of what information is stored in what byte

***What time can individual byte ememory be stored and retrieved?***
O(1)

***What is an array?***
A group of related variables stored one after another in a contiguous portion of memory.

***What is a cell in an array?***
location within an array

***What is an index in an array?***
describe location within the array

***How can the deisred memory address of an array be computed if cells have the same number of bytes?***
start + cellsize * index

### 5.2.1 Referential Arrays

***How does does Python represent a list or tuple instance?***
Using an internal storage mechanisfm of an array of ject references

***What are the number of bits used to store memory addresses in sequences?***
64 bits per address

***What happens to the references of a new list when you create it using slices***
The new list has references to the same elements that are in the original.

***What is a shallow copy?***
a new object referecing the same elements as in the first.

***Waht is a deep copy?***
a new list with new elements

***How does the extend command add elements from one list to the end of another?***
It receives references to those elements.

### 5.2.2 Compact Arrays in Python
***What is a acompact array?***
An array storing the bits that represent the primary data.

***What is a typecode for use in the Python array class from the array module?***
a character that designates the type of data that will be stored in the array.

## 5.3 Dynamic Arrays and Amortization
***What is a dynamic array?****
An array with no  apparent limit on overall capacity  byt maintaining an underlying array that oftern has greater capacity than the current lenght of the list. When capacity is exhausted a new larger array is initialized with the same prefix as the smaller one.

### 5.3.1 Implementing Dynamic Array
***What steps do you peform when an underlying list is full?***
1. Allocate a new array B with larger capacity
2. Set B[i] = A[i], for i = 0, ..., n-1, where n denotes current number of items.
3. Set A = B, that is, we henceforth use B as the array supporting the list.
4. Insert the new element in the new array.

### 5.3.2 Amortized Analysis of Dynamic Arrays
***What is a cyber dollar?***
Constant amount of computing time.

#### Geometric Increase in Capacity
***What is the key to performance of amortization?***
amount of additional space is proportional to the current size of the array.

#### Beware of Arithmetic Progression
***What results from a fixed increment for each resize?***
quadratic time in number of operations.

#### Memory Usage and Shrinking an Array
***What does an implementation of an array have to consider when removing elements?***
It will shrink underlying array on occassion to maintain amortized bound.

### 5.3.3 Python's List Class
## 5.4 Efficiency of Python's Sequnece Types
### 5.4.1 Python's List and Tuple Classes
***Aymptotic efficiency of nonmutating behaviors in lists and tuples***
|Operation|Running Time|
|-|-|
|len(data)|O(1)|
|data[j]|O(1)|
|data.count(value)|O(n)
|data.index(value)|O(k+1)|
|value in data|O(k+1)|
|data1 == data2 (similartly !=, <,<=,>,>=)|O(k+1)|
|data[j:k]|O(k-j+1)|
|data1+data2|O(n<sub>1</sub>+n<sub>2</sub>)|
|c * data| O(cn)|
### 5.4.2 Python's String Class
## 5.5. Using Array-Based Sequneces
### 5.5.1 Storing High Scores for a Game
### 5.5.2 Sorting a Sequence
***How do you express the insertion-sort algorithm?***
```
Input: Ana rray A of n comparable elements
Output: The array A with elements rearranged in nondecreasing order
for k from 1 to n-1 do
    Insert A[k] at its proper location within A[0], A[1],...,A[k]
```
### 5.5.3 Simple Cryptography
***What is cryptography?***
science of secret messages and their applicaitons

***What is encryption/decryption?***
Conversion of pliantext to ciphertext and back

## 5.6 Multidimensional Data Sets
***Wbat is a matrix?***
A two-dimensiona array

***How do you properly intialize a two dimensional list?***
`data = [[0] *c for j in range (r)]`