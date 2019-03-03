#-*- coding: utf-8 -*-

# input = [10,3,500,7, 10, 44]
input = [7,92,18,33,58,7,33,42, 100]

def findMax(arr):
    maxv = 0
    for x in arr:
        if (maxv < x): maxv = x
    return maxv

def findIndexOfMax(arr):
    n = len(arr)
    maxIdx = 0
    for i in range(1, n):
        if (arr[maxIdx] < arr[i]): maxIdx = i
    return maxIdx
print findMax(input)
print findIndexOfMax(input)
