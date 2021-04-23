from Methods import BubbleSort as bubble, QuickSort as quick, MergeSort as merge, SelectionSort as selection, \
    HeapSort as heap
import cProfile as profile
import random
import sys
import time


def quickort(randomList):
    quick.quick_sort(randomList, 0, len(randomList) - 1)
    # print(randomList)


def bubblesort(randomList):
    bubble.bubble_sort(randomList)
    # print(randomList)


def mergesort(randomList):
    merge.merge_sort(randomList)
    # print(randomList)


def selectionsort(randomList):
    selection.selection_sort(randomList)
    # print(randomList)


def heapsort(randomList):
    heap.heap_sort(randomList)
    # print(randomList)


def statistics():
    numTotalTest = 10
    for iteration in range(0, numTotalTest):
        print(
            "---------------------------------------------- Iteration Number {} ----------------------------------------------".format(
                iteration))
        # It create a list within 3000 registers randomly,
        # with a range from 0 to 3000
        maximum = 3000
        randomList = []
        for i in range(0, maximum):
            randomList.append(random.randint(0, maximum))
        randomListCopy = randomList.copy()
        print("--------------------------------------- BubbleSort -------------------------------")
        profile.runctx('bubblesort(randomList)', globals(), {'randomList': randomListCopy})
        randomListCopy = randomList.copy()
        print("--------------------------------------- QuickSort -------------------------------")
        profile.runctx('quickort(randomList)', globals(), {'randomList': randomListCopy})
        randomListCopy = randomList.copy()
        print("--------------------------------------- MergeSort -------------------------------")
        profile.runctx('mergesort(randomList)', globals(), {'randomList': randomListCopy})
        randomListCopy = randomList.copy()
        print("--------------------------------------- SelectionSort -------------------------------")
        profile.runctx('selectionsort(randomList)', globals(), {'randomList': randomListCopy})
        randomListCopy = randomList.copy()
        print("--------------------------------------- HeapSort -------------------------------")
        profile.runctx('heapsort(randomList)', globals(), {'randomList': randomListCopy})


# The main method of the script
if __name__ == '__main__':
    # Setting the limit of recursion that python interpreter could do.
    maximunIterations = 10000
    sys.setrecursionlimit(maximunIterations + maximunIterations)
    print("Starts the processing...")
    timeStart = time.time()
    statistics()
    endStart = time.time()
    print("It last: {} Seconds".format(endStart - timeStart))
