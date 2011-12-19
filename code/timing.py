"""
What this example does is showcase the timing function in python
to help narrow down slow functions.

This example generates a list of 5000 random numbers then sorts them.

It shows bubblesort vs. quicksort.

#Please note this code has to be ran inside the SimpleCV shell to work

"""

print __doc__

#define our bubblesort algorithm
def bubbleSort(list_to_sort):
	the_list = list_to_sort
	length = len(the_list) - 1
	sorted = False
	while not sorted:
		sorted = True
		for i in range(length):
			if the_list[i] > the_list[i+1]:
				sorted = False
				the_list[i], the_list[i+1] = the_list[i+1], the_list[i]
	return the_list

#define quicksort algorithm
def qsort(L):
	if len(L)<2: return L
	pivot_element = random.choice(L)
	small = [i for i in L if i< pivot_element]
	medium = [i for i in L if i==pivot_element]
	large = [i for i in L if i> pivot_element]
	return qsort(small) + medium + qsort(large)


#generate a list of 10,000 random numbers
randoms = [random.randint(0,1000) for r in xrange(5000)]
bubble_list = numpy.copy(randoms)
quicksort_list = numpy.copy(randoms)

print "Running Bubble Sort"
timeit(bubbleSort(bubble_list))

print "Running Quick Sort"
timeit.timeit(qsort)
