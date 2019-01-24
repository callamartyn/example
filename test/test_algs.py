import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    x = np.array([1,2,4,0,1])
    empty = []
    single = [11]
    dup = [3, 12, 7, 7, -6, 9]
    odd = np.random.rand(11)
    even = np.random.rand(12)
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    #algs.bubblesort(x)
    # test that bubblesort is sorting array x correctly
    assert np.array_equal(algs.bubblesort(x), [0,1,1,2,4])
    assert np.array_equal(algs.bubblesort(empty), [])
    assert np.array_equal(algs.bubblesort(single), [11])
    assert np.array_equal(algs.bubblesort(dup), [-6, 3, 7, 7, 9, 12])
    algs.bubblesort(odd)
    assert odd[0] < odd[10]
    algs.bubblsort(even)
    assert even[0] < even[11]

def test_quicksort():

    x = np.array([1,2,4,0,1])
    # for now, just attempt to call the quicksort function, should
    # actually check output
    #algs.quicksort(x)

    # testing the quicksort is sorting array x correctly
    assert np.array_equal(algs.quicksort(x), [0,1,1,2,4])
