'''
Exercise 10-3.
-------------
Write a function that takes a list of numbers and returns the cumulative sum; that is, a
new list where the ith element is the sum of the first i+1 elements from the original list.
For example, the cumulative sum of [1, 2, 3] is [1, 3, 6] .'''

def cumulativeSum(l):
    print('original list:',l)
    total = 0
    for i in range(len(l)):
        total += l[i]
        l[i] = total
    return l

print(cumulativeSum([1,2,3,10]))
