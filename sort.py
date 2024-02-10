from typing import List


def bubbleSort(L: List[int]):
    for outer in range(len(L), 0, -1):
        for i in range(outer-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]


def selectSort(L: List[int]):
    for i in range(len(L)):
        min = i
        for j in range(i, len(L)):
            if L[j] < L[min]:
                min = j
        L[i], L[min] = L[min], L[i]
