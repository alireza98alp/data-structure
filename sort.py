from typing import List
from random import randint


def BubbleSort(L: List[int]) -> List[int]:
    for outer in range(len(L), 0, -1):
        for i in range(outer-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
    return L
