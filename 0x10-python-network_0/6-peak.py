#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None

    def binary_search_peak(low, high):
        mid = (low + high) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return binary_search_peak(low, mid - 1)
        else:
            return binary_search_peak(mid + 1, high)

    return binary_search_peak(0, len(list_of_integers) - 1)

