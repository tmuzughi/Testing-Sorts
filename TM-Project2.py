# Author: Tarik Muzughi
# Date: 10/21/19
# Class: 3130 Piatnitskaia
# Program tests the efficiency of six sorting algorithms by averaging run times taken for
# sorting arrays of sizes 1000, 10000, and 100000.

import sys
from timeit import default_timer as timer
from random import randint

#################BEGIN SELECTION SORT#####################
#  source: https://www.geeksforgeeks.org/selection-sort/
def selectionSort(A):

    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

            # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]

#################BEGIN INSERTION SORT#####################
#  source: https://www.geeksforgeeks.org/insertion-sort/
#  author: Mohit Kumra

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#################BEGIN BUBBLE SORT W/ COUNTING############
# source: https://www.geeksforgeeks.org/bubble-sort/
# author: Shreyanshi Arun

# An optimized version of Bubble Sort
def bubbleSortSwaps(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break


#################BEGIN BUBBLE SORT W/0 COUNTING###########
# source: https://www.geeksforgeeks.org/bubble-sort/

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

##################BEGIN QUICKSORT#########################
# source: https://www.geeksforgeeks.org/quick-sort/
# author: Mohit Kumra

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Function to do Quick sort
def quickSort(arr, low, high):
    while low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        if (pi - low < high - pi):
            quickSort(arr, low, pi - 1)
            low = pi + 1;
        else:
            quickSort(arr, pi + 1, high)
            high = pi - 1;
        # Separately sort elements before
        # partition and after partition



##################BEGIN MERGE SORT########################
# source: https://www.geeksforgeeks.org/merge-sort/
# author: Mayank Khanna

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

##################GENERATE RANDOM ARRAY###############
def generateRandom(N):
    someArray = [0] * N
    for i in range(N):
        value = randint(1, 10000)
        someArray[i] = value
    return someArray
#################GENERATE SORTED ARRAY################
def generateSorted(N):
    someArray = [0] * N
    if N <= 10000:
        for i in range(0, N):
            someArray[i] = i + 1
        return someArray
    if N == 100000:
        k = 1
        j = 0
        for i in range(0, N):
            someArray[i] = k
            j += 1
            if (j > 9):
                k += 1
                j = 0
        return someArray
########GENERATE ALMOST SORTED ARRAY###################
def generateAlmost(N):
    someArray = generateSorted(N)
    for i in range(0, N):
        if ((i + 1) % 10 == 0):
            someArray[i] = randint(1, 10000)
    return someArray
###############TEST SELECTION SORT#####################
def testSelection():
    ##############RANDOM################
    random1k = generateRandom(1000)
    random10k = generateRandom(10000)
    random100k = generateRandom(100000)

    random1kTime = 0
    for i in range(0, 5):
        start = timer()
        selectionSort(random1k)
        end = timer()
        random1kTime += (end - start)
    print("Selection Sort average time (random 1k): %f" % (random1kTime/5.0))

    random10kTime = 0
    for i in range(0, 5):
        start = timer()
        selectionSort(random10k)
        end = timer()
        random10kTime += (end - start)
    print("Selection Sort average time (random 10k): %f" % (random10kTime / 5.0))

    random100kTime = 0
    for i in range(0, 5):
        start = timer()
        selectionSort(random100k)
        end = timer()
        random100kTime += (end - start)
    print("Selection Sort average time (random 100k): %f" % (random100kTime / 5.0))
    ############SORTED##################
    sorted1k = generateSorted(1000)
    sorted10k = generateSorted(10000)
    sorted100k = generateSorted(100000)

    sorted1kTime = 0
    for i in range(0, 5):
        start = timer()
        selectionSort(sorted1k)
        end = timer()
        sorted1kTime += (end - start)
    print("Selection Sort average time (sorted 1k): %f" % (sorted1kTime / 5.0))

    sorted10kTime = 0
    for i in range(0, 5):
        start = timer()
        selectionSort(sorted10k)
        end = timer()
        sorted10kTime += (end - start)
    print("Selection Sort average time (sorted 10k): %f" % (sorted10kTime / 5.0))

    sorted100kTime = 0
    for i in range(0, 5):
        start = timer()
        selectionSort(sorted100k)
        end = timer()
        sorted100kTime += (end - start)
    print("Selection Sort average time (sorted 100k): %f" % (sorted100kTime / 5.0))
    ############ALMOST##################
    almost1k = generateAlmost(1000)
    almost10k = generateAlmost(10000)
    almost100k = generateAlmost(100000)

    almost1kTime = 0
    for i in range(0, 5):
        start = timer()
        selectionSort(almost1k)
        end = timer()
        almost1kTime += (end - start)
    print("Selection Sort average time (almost 1k): %f" % (almost1kTime / 5.0))

    almost10kTime = 0
    for i in range(0, 5):
        start = timer()
        selectionSort(almost10k)
        end = timer()
        almost10kTime += (end - start)
    print("Selection Sort average time (almost 10k): %f" % (almost10kTime / 5.0))

    almost100kTime = 0
    for i in range(0, 5):
        start = timer()
        selectionSort(almost100k)
        end = timer()
        almost100kTime += (end - start)
    print("Selection Sort average time (almost 100k): %f" % (almost100kTime / 5.0))
###############TEST INSERTION SORT#####################
def testInsertion():
    ##############RANDOM################
    random1k = generateRandom(1000)
    random10k = generateRandom(10000)
    random100k = generateRandom(100000)

    random1kTime = 0
    for i in range(0, 5):
        start = timer()
        insertionSort(random1k)
        end = timer()
        random1kTime += (end - start)
    print("Insertion Sort average time (random 1k): %f" % (random1kTime/5.0))

    random10kTime = 0
    for i in range(0, 5):
        start = timer()
        insertionSort(random10k)
        end = timer()
        random10kTime += (end - start)
    print("Insertion Sort average time (random 10k): %f" % (random10kTime / 5.0))

    random100kTime = 0
    for i in range(0, 5):
        start = timer()
        insertionSort(random100k)
        end = timer()
        random100kTime += (end - start)
    print("Insertion Sort average time (random 100k): %f" % (random100kTime / 5.0))
    ############SORTED##################
    sorted1k = generateSorted(1000)
    sorted10k = generateSorted(10000)
    sorted100k = generateSorted(100000)

    sorted1kTime = 0
    for i in range(0, 5):
        start = timer()
        insertionSort(sorted1k)
        end = timer()
        sorted1kTime += (end - start)
    print("Insertion Sort average time (sorted 1k): %f" % (sorted1kTime / 5.0))

    sorted10kTime = 0
    for i in range(0, 5):
        start = timer()
        insertionSort(sorted10k)
        end = timer()
        sorted10kTime += (end - start)
    print("Insertion Sort average time (sorted 10k): %f" % (sorted10kTime / 5.0))

    sorted100kTime = 0
    for i in range(0, 5):
        start = timer()
        insertionSort(sorted100k)
        end = timer()
        sorted100kTime += (end - start)
    print("Insertion Sort average time (sorted 100k): %f" % (sorted100kTime / 5.0))
    ############ALMOST##################
    almost1k = generateAlmost(1000)
    almost10k = generateAlmost(10000)
    almost100k = generateAlmost(100000)

    almost1kTime = 0
    for i in range(0, 5):
        start = timer()
        insertionSort(almost1k)
        end = timer()
        almost1kTime += (end - start)
    print("Insertion Sort average time (almost 1k): %f" % (almost1kTime / 5.0))

    almost10kTime = 0
    for i in range(0, 5):
        start = timer()
        insertionSort(almost10k)
        end = timer()
        almost10kTime += (end - start)
    print("Insertion Sort average time (almost 10k): %f" % (almost10kTime / 5.0))

    almost100kTime = 0
    for i in range(0, 5):
        start = timer()
        insertionSort(almost100k)
        end = timer()
        almost100kTime += (end - start)
    print("Insertion Sort average time (almost 100k): %f" % (almost100kTime / 5.0))
###############TEST BUBBLE SORT W/ SWAPS#####################
def testBubbleSwaps():
    ##############RANDOM################
    random1k = generateRandom(1000)
    random10k = generateRandom(10000)
    random100k = generateRandom(100000)

    random1kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSortSwaps(random1k)
        end = timer()
        random1kTime += (end - start)
    print("Bubble Sort w/ Swaps average time (random 1k): %f" % (random1kTime / 5.0))

    random10kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSortSwaps(random10k)
        end = timer()
        random10kTime += (end - start)
    print("Bubble Sort w/ Swaps average time (random 10k): %f" % (random10kTime / 5.0))

    random100kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSortSwaps(random100k)
        end = timer()
        random100kTime += (end - start)
    print("Bubble Sort w/ Swaps average time (random 100k): %f" % (random100kTime / 5.0))
    ############SORTED##################
    sorted1k = generateSorted(1000)
    sorted10k = generateSorted(10000)
    sorted100k = generateSorted(100000)

    sorted1kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSortSwaps(sorted1k)
        end = timer()
        sorted1kTime += (end - start)
    print("Bubble Sort w/ Swaps average time (sorted 1k): %f" % (sorted1kTime / 5.0))

    sorted10kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSortSwaps(sorted10k)
        end = timer()
        sorted10kTime += (end - start)
    print("Bubble Sort w/ Swaps average time (sorted 10k): %f" % (sorted10kTime / 5.0))

    sorted100kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSortSwaps(sorted100k)
        end = timer()
    sorted100kTime += (end - start)
    print("Bubble Sort w/ Swaps average time (sorted 100k): %f" % (sorted100kTime / 5.0))
    ############ALMOST##################
    almost1k = generateAlmost(1000)
    almost10k = generateAlmost(10000)
    almost100k = generateAlmost(100000)

    almost1kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSortSwaps(almost1k)
        end = timer()
        almost1kTime += (end - start)
    print("Bubble Sort w/ Swaps average time (almost 1k): %f" % (almost1kTime / 5.0))

    almost10kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSortSwaps(almost10k)
        end = timer()
        almost10kTime += (end - start)
    print("Bubble Sort w/ Swaps average time (almost 10k): %f" % (almost10kTime / 5.0))

    almost100kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSortSwaps(almost100k)
        end = timer()
    almost100kTime += (end - start)
    print("Bubble Sort w/ Swaps average time (almost 100k): %f" % (almost100kTime / 5.0))
###############TEST BUBBLE SORT W/O SWAPS#####################
def testBubble():
    ##############RANDOM################
    random1k = generateRandom(1000)
    random10k = generateRandom(10000)
    random100k = generateRandom(100000)

    random1kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSort(random1k)
        end = timer()
        random1kTime += (end - start)
    print("Bubble Sort w/o Swaps average time (random 1k): %f" % (random1kTime/5.0))

    random10kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSort(random10k)
        end = timer()
        random10kTime += (end - start)
    print("Bubble Sort w/o Swaps average time (random 10k): %f" % (random10kTime / 5.0))

    random100kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSort(random100k)
        end = timer()
        random100kTime += (end - start)
    print("Bubble Sort w/o Swaps average time (random 100k): %f" % (random100kTime / 5.0))
    ############SORTED##################
    sorted1k = generateSorted(1000)
    sorted10k = generateSorted(10000)
    sorted100k = generateSorted(100000)

    sorted1kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSort(sorted1k)
        end = timer()
        sorted1kTime += (end - start)
    print("Bubble Sort w/o Swaps average time (sorted 1k): %f" % (sorted1kTime / 5.0))

    sorted10kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSort(sorted10k)
        end = timer()
        sorted10kTime += (end - start)
    print("Bubble Sort w/o Swaps average time (sorted 10k): %f" % (sorted10kTime / 5.0))

    sorted100kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSort(sorted100k)
        end = timer()
        sorted100kTime += (end - start)
    print("Bubble Sort w/o Swaps average time (sorted 100k): %f" % (sorted100kTime / 5.0))
    ############ALMOST##################
    almost1k = generateAlmost(1000)
    almost10k = generateAlmost(10000)
    almost100k = generateAlmost(100000)

    almost1kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSort(almost1k)
        end = timer()
        almost1kTime += (end - start)
    print("Bubble Sort w/o Swaps average time (almost 1k): %f" % (almost1kTime / 5.0))

    almost10kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSort(almost10k)
        end = timer()
        almost10kTime += (end - start)
    print("Bubble Sort w/o Swaps average time (almost 10k): %f" % (almost10kTime / 5.0))

    almost100kTime = 0
    for i in range(0, 5):
        start = timer()
        bubbleSort(almost100k)
        end = timer()
    almost100kTime += (end - start)
    print("Bubble Sort w/o Swaps average time (almost 100k): %f" % (almost100kTime / 5.0))
###############TEST QUICK SORT#####################
def testQuick():
    ##############RANDOM################
    random1k = generateRandom(1000)
    random10k = generateRandom(10000)
    random100k = generateRandom(100000)

    random1kTime = 0
    for i in range(0, 5):
        start = timer()
        quickSort(random1k, 0, len(random1k)-1)
        end = timer()
        random1kTime += (end - start)
    print("Quick Sort average time (random 1k): %f" % (random1kTime/5.0))

    random10kTime = 0
    for i in range(0, 5):
        start = timer()
        quickSort(random10k, 0, len(random10k)-1)
        end = timer()
        random10kTime += (end - start)
    print("Quick Sort average time (random 10k): %f" % (random10kTime / 5.0))

    random100kTime = 0
    for i in range(0, 5):
        start = timer()
        quickSort(random100k, 0, len(random100k)-1)
        end = timer()
        random100kTime += (end - start)
    print("Quick Sort average time (random 100k): %f" % (random100kTime / 5.0))
    ############SORTED##################
    sorted1k = generateSorted(1000)
    sorted10k = generateSorted(10000)
    sorted100k = generateSorted(100000)

    sorted1kTime = 0
    for i in range(0, 5):
        start = timer()
        quickSort(sorted1k, 0, len(sorted1k)-1)
        end = timer()
        sorted1kTime += (end - start)
    print("Quick Sort average time (sorted 1k): %f" % (sorted1kTime / 5.0))

    sorted10kTime = 0
    for i in range(0, 5):
        start = timer()
        quickSort(sorted10k, 0, len(sorted10k)-1)
        end = timer()
        sorted10kTime += (end - start)
    print("Quick Sort average time (sorted 10k): %f" % (sorted10kTime / 5.0))

    sorted100kTime = 0
    for i in range(0, 5):
        start = timer()
        quickSort(sorted100k, 0, len(sorted100k)-1)
        end = timer()
        sorted100kTime += (end - start)
    print("Quick Sort average time (sorted 100k): %f" % (sorted100kTime / 5.0))
    ############ALMOST##################
    almost1k = generateAlmost(1000)
    almost10k = generateAlmost(10000)
    almost100k = generateAlmost(100000)

    almost1kTime = 0
    for i in range(0, 5):
        start = timer()
        quickSort(almost1k, 0, len(almost1k)-1)
        end = timer()
        almost1kTime += (end - start)
    print("Quick Sort average time (almost 1k): %f" % (almost1kTime / 5.0))

    almost10kTime = 0
    for i in range(0, 5):
        start = timer()
        quickSort(almost10k, 0, len(almost10k)-1)
        end = timer()
        almost10kTime += (end - start)
    print("Quick Sort average time (almost 10k): %f" % (almost10kTime / 5.0))

    almost100kTime = 0
    for i in range(0, 5):
        start = timer()
        quickSort(almost100k, 0, len(almost100k)-1)
        end = timer()
        almost100kTime += (end - start)
    print("Quick Sort average time (almost 100k): %f" % (almost100kTime / 5.0))
###############TEST MERGE SORT#####################
def testMerge():
    ##############RANDOM################
    random1k = generateRandom(1000)
    random10k = generateRandom(10000)
    random100k = generateRandom(100000)

    random1kTime = 0
    for i in range(0, 5):
        start = timer()
        mergeSort(random1k)
        end = timer()
        random1kTime += (end - start)
    print("Merge Sort average time (random 1k): %f" % (random1kTime/5.0))

    random10kTime = 0
    for i in range(0, 5):
        start = timer()
        mergeSort(random10k)
        end = timer()
        random10kTime += (end - start)
    print("Merge Sort average time (random 10k): %f" % (random10kTime / 5.0))

    random100kTime = 0
    for i in range(0, 5):
        start = timer()
        mergeSort(random100k)
        end = timer()
        random100kTime += (end - start)
    print("Merge Sort average time (random 100k): %f" % (random100kTime / 5.0))
    ############SORTED##################
    sorted1k = generateSorted(1000)
    sorted10k = generateSorted(10000)
    sorted100k = generateSorted(100000)

    sorted1kTime = 0
    for i in range(0, 5):
        start = timer()
        mergeSort(sorted1k)
        end = timer()
        sorted1kTime += (end - start)
    print("Merge Sort average time (sorted 1k): %f" % (sorted1kTime / 5.0))

    sorted10kTime = 0
    for i in range(0, 5):
        start = timer()
        mergeSort(sorted10k)
        end = timer()
        sorted10kTime += (end - start)
    print("Merge Sort average time (sorted 10k): %f" % (sorted10kTime / 5.0))

    sorted100kTime = 0
    for i in range(0, 5):
        start = timer()
        mergeSort(sorted100k)
        end = timer()
        sorted100kTime += (end - start)
    print("Merge Sort average time (sorted 100k): %f" % (sorted100kTime / 5.0))
    ############ALMOST##################
    almost1k = generateAlmost(1000)
    almost10k = generateAlmost(10000)
    almost100k = generateAlmost(100000)

    almost1kTime = 0
    for i in range(0, 5):
        start = timer()
        mergeSort(almost1k)
        end = timer()
        almost1kTime += (end - start)
    print("Merge Sort average time (almost 1k): %f" % (almost1kTime / 5.0))

    almost10kTime = 0
    for i in range(0, 5):
        start = timer()
        mergeSort(almost10k)
        end = timer()
        almost10kTime += (end - start)
    print("Merge Sort average time (almost 10k): %f" % (almost10kTime / 5.0))

    almost100kTime = 0
    for i in range(0, 5):
        start = timer()
        mergeSort(almost100k)
        end = timer()
    almost100kTime += (end - start)
    print("Merge Sort average time (almost 100k): %f" % (almost100kTime / 5.0))
################RESULTS########################

start = timer()

testSelection()
testInsertion()
testBubble()
testBubbleSwaps()
testQuick()
testMerge()

end = timer()
print("Total program time: %f" % (end - start))
