Timing
===========================
When using computer vision something that always has to be accounted for
is processing time.  If you are trying to make a person detector and the
vision system can only process one image per 5 seconds then a few people
could walk by the camera in the amount of time it would take to perform
that detection, making it not very useful.


Luckily SimpleCV has something built into the Shell that will help you
tune your programming in order to make things faster.

That function is called **timeit**.

Lets get a basic idea of how time it works.  We will randomly generate a
list of 10,000 numbers.


  >>> import numpy.random
	>>> randoms = randoms = [random.randint(0,1000) for r in xrange(10000)]
	>>> print randoms


As you can see we now have a bit list of random numbers.  Now what we want
to do is sort them.  First we need to define our sorting algorithm.  Keep
in mind we used bubble sort in this example as it is one of the slowest
sorting algorithms, but it was meant to show time differences.::


	def bubbleSort(the_list):
		length = len(the_list) - 1
		sorted = False

		while not sorted:
			sorted = True
			for i in range(length):
				if the_list[i] > the_list[i+1]:
					print "sorting"
					sorted = False
					the_list[i], the_list[i+1] = the_list[i+1], the_list[i]



Once our sorting algorithm is defined, we just run:

	>>> timeit bubblesort(randoms)



And should get an output similiar too::

	>>> timeit bubblesort(randoms)
	1000 loops, best of 3: 759 us per loop
	

So what this did is give us an idea of how long it will take. And as expected
bubble sort is quite slow.  So lets do the same thing using a much faster
sorting algorithm called quick sort.


First define the quicksort function::

	def qsort(L):
		if len(L)<2: return L
		pivot_element = random.choice(L)
		small = [i for i in L if i< pivot_element]
		medium = [i for i in L if i==pivot_element]
		large = [i for i in L if i> pivot_element]
		return qsort(small) + medium + qsort(large)


One thing that happens while running the sort, is that it does it **in-place**
so it messes up the randoms array.  So lets generate the random lits again but
make a copy to do the work on.

	>>> randoms = randoms = [random.randint(0,1000) for r in xrange(10000)]
	>>> bubblesort_list = numpy.copy(randoms)
	>>> quicksort_lits = numpy.copy(randoms)


Then just run timeit on these functions::

	>>> timeit bubblesort(bubblesort_list)
	1000 loops, best of 3: 759 us per loop
	>>> timeit qsort(quicksort_list)


As you can see the quicksort is much faster.  This should work in theory
for any type of function you write or use, so instead of bubblesort it
could be:

	>>> img = Image("simplecv")
	>>> timeit img.findBlobs()


:download:`Download the script <../code/timing.py>`
