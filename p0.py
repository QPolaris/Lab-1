#!/usr/bin/python3

# Answer code for testing purposes. Allows you to make use of the test/ folder.
# Anything outside of the starter/ and test/ folder is optional.


def binarySearch(A, k):
    """Apply binary search on array with the target number.

    Args:
        array: An array of integers in non-decreasing order.
        target: A int value which is target number.

    Return:
        Index of target number in array if find, otherwise, return -1.
    """
    
    #TODO: Implement without using python's in-built functiondef binary(A, k):
    def bSearch(A, k, low, high):
        if high == low:
            if A[low] == k:
                return low
            else:
                return -1
        mid = (low + high)//2
        if A[mid] == k:
            return mid
        elif A[mid] > k:
            if low == mid:
                return -1
            else:
                return bSearch(A, k, low, mid-1)
        else:
            return bSearch(A, k, mid+1, high)
    if isinstance(A, list) == False or isinstance(k, int) == False:
        return -1
    else:
        if len(A) == 0:
            return -1
        else:
            x = bSearch(A, k, 0, len(A)-1)
            return x

    
    
    
def linearSearch(A, k):
    """Apply linear search on array with the target number.

    Args:
        array: An array of integers in non-decreasing order.
        target: A int value which is target number.

    Return:
        Index of target number in array if find, otherwise, return -1.
    """

    #TODO: Implement without using python's in-built function
    if isinstance(A, list) == False or isinstance(k, int) == False:
        return -1
    else:
        for i in range(len(A)):
            if A[i] == k:
                return i
        return -1
