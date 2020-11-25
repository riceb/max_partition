# Naively scan each index to check for partitionability. 
# Runtime: O(n^2)
def max_partition(a):
	partitions = 1
	n = len(a)
	# Note that we go up to index i-1 because 
	# we don't partition at index n-1.
	for i in range(n-1):
		# Compare the max of the elements before index i
		# and the min of the elements after index i. If 
		# the former is smaller, we can partition at this
		# index, thus incrementing number of subarrays.
		if max(a[0:i+1]) <= min(a[i+1:n]):
			partitions += 1
	return partitions