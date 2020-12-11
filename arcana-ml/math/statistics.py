"""
    Overview: This class contains method to make statistical measurement on data.
"""

def mean(array):
	"""
	Compute the mean for a given array

	Parameters:
	-----------
	array: a array which contains numbers (list)

	Return:
	-------
	sum/len(array): the mean of array (float)
	"""

	return sum(array) / len(array)