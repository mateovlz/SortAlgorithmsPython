from Methods import BubbleSort as bubble, QuickSort as quick, MergeSort as merge, SelectionSort as selection, \
    HeapSort as heap
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
    numTotalTests = 10
    for testCases in range(0, 30000, 3000):
        valueBubble = 0
        valueQuick = 0
        valueMerge = 0
        valueSelection = 0
        valueHeap = 0
        # It create a list within 3000 registers randomly,
        # with a range from 0 to 3000
        maximum = 3000
        randomList = []
        for i in range(0, maximum):
            randomList.append(random.randint(0, maximum))

        for test in range(0, numTotalTests):
            # print("--------------------------------------- BubbleSort -------------------------------")
            timeStart = time.time()
            bubblesort(randomList)
            timeEnds = time.time()
            valueBubble += (timeEnds - timeStart)
            # print("--------------------------------------- QuickSort -------------------------------")
            timeStart = time.time()
            quickort(randomList)
            timeEnds = time.time()
            valueQuick += (timeEnds - timeStart)
            # print("--------------------------------------- MergeSort -------------------------------")
            timeStart = time.time()
            mergesort(randomList)
            timeEnds = time.time()
            valueMerge += (timeEnds - timeStart)
            # print("--------------------------------------- SelectionSort -------------------------------")
            timeStart = time.time()
            selectionsort(randomList)
            timeEnds = time.time()
            valueSelection += (timeEnds - timeStart)
            # print("--------------------------------------- HeapSort -------------------------------")
            timeStart = time.time()
            heapsort(randomList)
            timeEnds = time.time()
            valueHeap += (timeEnds - timeStart)
        valueAverageBubble = valueBubble / numTotalTests
        valueAverageQuick = valueQuick / numTotalTests
        valueAverageMerge = valueMerge / numTotalTests
        valueAverageSelection = valueSelection / numTotalTests
        valueAverageHeap = valueHeap / numTotalTests
        print("Average; {}; Bubble; {}, Quick; {}; Merge; {}; Selection; {}; Heap; {} ;".format(testCases, round(
            valueAverageBubble, 4), round(valueAverageQuick, 4), round(valueAverageMerge, 4), round(
            valueAverageSelection, 4), round(valueAverageHeap, 4)))


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
