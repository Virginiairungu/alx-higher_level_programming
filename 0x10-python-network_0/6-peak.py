#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    def binary_search_peak(low, high):
        mid = (low + high) // 2
        
        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        # If left neighbor is greater, the peak must be on the left side
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return binary_search_peak(low, mid - 1)
        # If right neighbor is greater, the peak must be on the right side
        else:
            return binary_search_peak(mid + 1, high)

    return binary_search_peak(0, len(list_of_integers) - 1)

