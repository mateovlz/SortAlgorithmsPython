from Methods import BubbleSort as bubble, QuickSort as quick, MergeSort as merge, SelectionSort as selection, \
    HeapSort as heap
import cProfile as profile
import random
import sys

# It create a list within 3000 registers randomly,
# with a range from 0 to 3000
maximum = 3000
randomList = []
for i in range(0, maximum):
    randomList.append(random.randint(0, maximum))

print("List to Order: {}".format(randomList))


def quickort():
    quick.quick_sort(randomList, 0, len(randomList) - 1)
    # print(randomList)


def bubblesort():
    bubble.bubble_sort(randomList)
    # print(randomList)


def mergesort():
    merge.merge_sort(randomList)
    # print(randomList)


def selectionsort():
    selection.selection_sort(randomList)
    # print(randomList)


def heapsort():
    heap.heap_sort(randomList)
    # print(randomList)


# The main method of the script
if __name__ == '__main__':
    # Setting the limit of recursion that python interpreter could do.
    sys.setrecursionlimit(maximum + maximum)
    # profile.run('start()')
    print("--------------------------------------- BubbleSort -------------------------------")
    profile.run('bubblesort()')
    print("--------------------------------------- QuickSort -------------------------------")
    profile.run('quickort()')
    print("--------------------------------------- MergeSort -------------------------------")
    profile.run('mergesort()')
    print("--------------------------------------- SelectionSort -------------------------------")
    profile.run('selectionsort()')
    print("--------------------------------------- HeapSort -------------------------------")
    profile.run('heapsort()')
