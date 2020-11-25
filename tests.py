import solution
import starter_code
import naive_solution

#Test 1
array = [1,2,3,4,5,6,7]
print("Test 1")
print("a =", array)
a = starter_code.max_partition(array)

if (a == 7): 
	print("Test 1 passed!\n")
else:
	print("Test 1 failed!")
	print("Expected:", 7)
	print("Actual:", a, "\n")

#Test 2
array = [7,6,5,4,3,2,1]
print("Test 2")
print("a =", array)
a = solution.max_partition(array)

if (a == 1): 
	print("Test 2 passed!\n")
else:
	print("Test 3 failed!")
	print("Expected:", 1)
	print("Actual:", a, '\n')

#Test 3
array = [5,6,4,7,6,9,9,9,9,9,9,10,13,21,13]
print("Test 3")
print("a =", array)
a = solution.max_partition(array)

if (a == 11): 
	print("Test 3 passed!\n")
else:
	print("Test 3 failed!")
	print("Expected:", 11)
	print("Actual:", a,"\n")

#Test 4
array = [0]*50000
array += [1]*50000
print("Test 4")
print("a = A big array with 0s and 1s")
a = solution.max_partition(array)

if (a == 100000): 
	print("Test 4 passed!\n")
else:
	print("Test 4 failed!")
	print("Expected:", 100000)
	print("Actual:", a, "\n")



