# We know that a sorted partition can be made at index i
# if the max of all elements before i (including i) 
# is smaller than the min of all elements after i. 

# Thus, we dynamically store the before max and after min 
# for each index in two arrays. The two arrays can be found 
# with a forwardscan and a backward scan of a, while keeping
# track of max_so_far and min_so_far. 
# Runtime: (3n) = O(n). 

def max_partition(a):

	n = len(a)

	# forward scan
	max_front = []
	max_so_far = float("-inf")
	for i in range(n):
		if a[i] > max_so_far:
			max_so_far = a[i]
		max_front.append(max_so_far)


	# backward scan
	min_back = []
	min_so_far = float("inf")
	for i in range(n-1):
		if a[n-i-1] < min_so_far: 
			min_so_far = a[n-i-1]
		# this inserts to the front, as we're scanning backwards
		min_back.insert(0, min_so_far)

	# Now we do a forward scan, and for each index whose before max
	# is smaller than its after min, we increment number of subarrays by 1.
	partitions = 1
	# Note that when we say partition at index i, we divide the array at i,
	# incrementing the number of subarrays by 1. Thus, it doesn't make sense 
	# to partition on the last element since there're no elements after that. 
	for i in range(n-1):
		if max_front[i] <= min_back[i]:
			partitions += 1
	return partitions
		
