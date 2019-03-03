#-*- coding: utf-8 -*-

input = [10,3,500,7, 10, 44]
# input = [7,92,18,33,58,7,33,42, 100]

def findMin(arr):
    n = len(arr)
    minv = arr[0]
    for i in range(1, n):
        if(minv > arr[i]): minv = arr[i]
    return minv


print findMin(input)