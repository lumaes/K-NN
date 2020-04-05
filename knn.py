
def knn(dataset, querry_point, k, classification, distance , neighbors = [], weighted = False):
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
			#return the mean of all y points
			return mean_y(neighbors)
		else:
			result = [pt[-1] for pt in neighbors]
			return max(set(result), key = result.count)
	else:

		min_point = dataset[0]

		for point in dataset:
			if distance(point[0], querry_point) <= distance(min_point[0], querry_point):

				min_point = point

		neighbors.append(min_point)
		dataset.remove(min_point)

		return knn(dataset, querry_point, k=(k-1), classification=classification, distance=distance , neighbors= neighbors)


def euclidian_distance(x1,x2):
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

	#init distance to 0
	dist = 0

	# for each index of points
	for i in range(len(x2)):
		# add the squared difference for the i index of x1 and x2
		dist += (x1[i] - x2[i]) ** 2  

	# square root of the distance 
	dist = dist ** (1/2)

	return dist


def manhattan_distance(x1, x2):
	"""
	"""

	# init the distance between x1 and x2 to 0.
	dist = 0

	# for each dimensions of the points
	for i in range(len(x2)):
		# add absolute difference of  i eme componant of x1 and x2
		dist += abs(x1[i] - x2[i])

	return dist

def abs(number):
	if number < 0:
		number *= -1
	return number

def mean_y(array):
	sum = 0
	for pt in array:
		#get the y value for each point
		sum += pt[-1]

	return sum / len(array)

def main():
	#data set
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

	result = knn(data, [33], k=3, classification=True, distance=manhattan_distance)

	print(result)


if __name__ == '__main__':
    main()