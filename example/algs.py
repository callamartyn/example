import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    if len(x) > 1:
        for i in range(len(x)-1, 0,-1):
            for j in range(i):
                if x[j] > x[j+1]:
                    #saving the first value
                    temp = x[j]
                    # replacing first value with second (smaller) value
                    x[j] = x[j+1]
                    # replacig second value with first(larger) value
                    x[j+1] = temp
    assert 1 == 1
    return x

# the partition function will partition a list around a pivotvalue one time
# it returns the ending rightmark, which can then be used as a split point for further ordering
def partition(x, start, end):
    pivotvalue = x[start]
    leftmark = start + 1
    rightmark = end

    done = False
    while not done:
        # left mark moves along left side of list until leftmark is greater than either pivot value or rightmark
        while leftmark <= rightmark and x[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        # inverse for rightmark
        while rightmark >= leftmark and x[rightmark] >= pivotvalue:
            rightmark = rightmark - 1
        # when marks cross, end
        if rightmark < leftmark:
            done = True
        # otherwise, if one of marks is wrong compared to pivotvalue, swap the marks
        else:
            temp = x[leftmark]
            x[leftmark] = x[rightmark]
            x[rightmark] = temp
        # now we have two halves sorted around the pivot value and the marks have passed each other
        # lets move the pivot value to the split point (where the rightmark is now)

    temp = x[start]
    x[start] = x[rightmark]
    x[rightmark] = temp

    return (rightmark)


def runqsort(x, start, end):
    if start < end:
        # run partition once to divide the list and get the splitpoint
        splitpoint = partition(x, start, end)
        # now run the function separately on each side of the splitpoint
        runqsort(x, start, splitpoint - 1)
        runqsort(x, splitpoint + 1, end)

    return x

def quicksort(x):
    runqsort(x, 0, (len(x)-1))
    assert 1 == 1
    return x
