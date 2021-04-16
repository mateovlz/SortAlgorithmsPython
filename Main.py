from Methods import BubbleSort as bubble, QuickSort as quick, MergeSort as merge, SelectionSort as selection, HeapSort as heap
import cProfile as profile
import sys

maximum = 2000
array = list(range(0,maximum))

def quickort():
    quick.quick_sort(array, 0, len(array) - 1)
    #print(array)

def bubblesort():
    bubble.bubble_sort(array)
    #print(array)

def mergesort():
    merge.merge_sort(array)
    #print(array)

def selectionsort():
    selection.selection_sort(array)
    #print(array)

def heapsort():
    heap.heap_sort(array)
    #print(array)

if __name__ == '__main__':
    sys.setrecursionlimit(maximum +1000)
    #profile.run('start()')
    print("--------------------------------------- BubbleSort -------------------------------")
    profile.run('bubblesort()')
    print("--------------------------------------- SortAlgorithms -------------------------------")
    profile.run('quickort()')
    print("--------------------------------------- MergeSort -------------------------------")
    profile.run('mergesort()')
    print("--------------------------------------- SelectionSort -------------------------------")
    profile.run('selectionsort()')
    print("--------------------------------------- HeapSort -------------------------------")
    profile.run('heapsort()')
