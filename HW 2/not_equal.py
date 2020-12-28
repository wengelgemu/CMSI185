'''
not_equal.py
Name: Wengel Gemu
Collaborators:
Date: September 16, 2019
Desscription: This program implements our own version of the != operator.
'''


def not_equal():
	# assigning values for two equal and two non equal variables
	a = 2
	b = 2
	c = 4
	d = 6

	# testing equivalency of a and b variables
	if a == b:
		not_equal_test1 = True
		print("a = " + str(a))
		print("b = " + str(b))
	else:
		not_equal_test1 = False
		print("a = " + str(a))
		print("b = " + str(b))

	return not_equal_test1

	# testing equivalency of c and d variables
	if c == d:
		not_equal_test2 = True
		print("c = " + str(c))
		print("d = " + str(d))
	else:
		not_equal_test2 = False
		print("c = " + str(c))
		print("d = " + str(d))

	return not_equal_test2

print(not_equal())
