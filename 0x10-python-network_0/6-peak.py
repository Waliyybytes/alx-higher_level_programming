#!/usr/bin/python3
""" finds the peak integer """


def find_peak(list_of_integers):
    """ finds peak integer of list """
    arr = list_of_integers
    if arr:
        if len(arr) == 1:
            return arr[0]
        if arr[0] > arr[1]:
            return arr[0]
        if arr[len(arr) - 1] > arr[len(arr) - 2]:
            return arr[len(arr) - 1]
        mid = len(arr) // 2
        if arr[mid - 1] >= arr[mid]:
            return find_peak(arr[0:mid])
        if arr[mid + 1] >= arr[mid]:
            return find_peak(arr[mid + 1:])
        return arr[mid]
