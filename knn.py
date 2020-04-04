

import math


def distance(x1,x2):
	"""
	Compute the distance between x1 and x2 points.

	note: x1 and x2 need the have the same length
	
	Parameters:
	-----------
	x1: the first point coordinates (list)
	x2: the second point coordinates (list)

	Returns:
	--------
	dist: the distance between x1 and x2
	"""

	# --- EUCLIDIAN DISTANCE ---

	#init distance to 0
	dist = 0

	# for each index of points
	for i in range(len(x1)):
		# add the squared difference for the i index of x1 and x2
		dist += (x1[i] - x2[i]) ** 2  

	# square root of the distance 
	dist = math.sqrt(dist)

	return dist


def knn(dataset, k, querry_point, classification, neighbors = [], weighted = False):
	"""
	Implementations of the KNN algorithm
	for based instanced machine learning.

	using recursivity

	Parameters:
	-----------
	dataset: the dataset who contains several points like [[x values],y] (list)
	k: the number of neighbors used by the KNN algorithms (int)
	querry_point: the x/feature value which will be predicted (list)
	classification: True if the KKN is using for classification, False for the regression using.
	result: the result of the knn for the querry_point

	Returns:
	--------
	the result of knn for the querry_point
	"""


	# if algorithm is finish, then return the result wanted
	if k == 0:

		if not classification:

			# get the sum of all Y coordinate of the neighbors points
			sum = 0
			for pt in neighbors:
				sum += pt[-1]
			# result is the sum divide by the numbers of neightbours (= k)
			result = sum / k
			return result

		else:

			result = []

			for pt in neighbors:
				result.append(pt[-1])

			return max(set(result), key = result.count)


	else:

		min_point = dataset[0]

		for point in dataset:

			if distance(point[0], querry_point) <= distance(min_point[0], querry_point):

				min_point = point


		neighbors.append(min_point)
		dataset.remove(min_point)

		return knn(dataset, k-1, querry_point, classification, neighbors)




data = [[[42], 1],
		[[65], 1],
		[[50], 1],
		[[76], 1],
		[[96], 1],
		[[50], 1],
		[[91], 0],
		[[58], 1],
		[[25], 1],
		[[23], 1],
		[[75], 1],
		[[46], 0],
		[[87], 0],
		[[96], 0],
		[[45], 0],
		[[32], 1],
		[[63], 0],
		[[21], 1],
		[[26], 1],
		[[93], 0],
		[[68], 1],
		[[96], 0], ]

print(knn(data, 3, [33], True))










