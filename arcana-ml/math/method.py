"""
    Overview: This script contains well-known mathematicals functions.
"""

# need math module to use the exponential function
import math

def sigmoid(x):
    """
    Return the sigmoid of x. (float)
    Source: https://en.wikipedia.org/wiki/Sigmoid_function (en)
    """
    return 1 / (1+math.exp(-x))

def swish(x):
    """
    Return the swich of x. (float)
    Note: derivated method from simoid
    Source: https://arxiv.org/pdf/1710.05941v1.pdf (en)
    """
    return x * sigmoid(x)

def max(x1, x2):
    """
    Return the maximum value between x1, x2.
    Source: /
    """
    if x1 > x2:
        return x1
    else:
        return x2

def relu(x):
    """
    Return the rectified linear unit of x.
    Source: https://fr.wikipedia.org/wiki/Redresseur_(r%C3%A9seaux_neuronaux) (fr)
    """
    return max(0, x)

def leaky_relu(x, leak=0.01):
    """
    Return the leaky rectified linear unit of x.
    Note: leak default is 0.01
    Source: /
    """
    if relu(x) == 0:
        return leak * x

def tanh(x):
    """
    Return the hyperbolic tangent of x. (float)
    Source: https://fr.wikipedia.org/wiki/Tangente_hyperbolique (fr)
    """
    return (1-math.exp(-2*x)) / (1+math.exp(-2*x))

def softmax(z):
    """
    Return softmax of vector z.
    Note: need a vector as z value.
    Source: https://en.wikipedia.org/wiki/Softmax_function (en)
    """
    z_softmaxed = []
    #compute the sum of all exponential value of z vector
    sum_expo = sum([math.exp(x) for x in z])
    # compute for each value the new value that is exponential of old value divided by computed sum.
    for value in z:
        z_softmaxed.append( math.exp(value) / sum_expo )
    # assert that sum of softmaxed vector is 1 (we say that the vector is normalised).
    assert(sum(z_softmaxed) == 1)

    return z_softmaxed

def euclidian_distance(x1,x2):
	"""
	Compute the distance between x1 and x2 points 
	using Euclidian's distance.

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
	Compute the distance between x1 and x2 points 
	using Manhattan's distance.

	note: x1 and x2 need the have the same length
	
	Parameters:
	-----------
	x1: the first point coordinates (list)
	x2: the second point coordinates (list)

	Returns:
	--------
	dist: the distance between x1 and x2
	"""

	# init the distance between x1 and x2 to 0.
	dist = 0

	# for each dimensions of the points
	for i in range(len(x2)):
		# add absolute difference of  i eme componant of x1 and x2
		dist += abs(x1[i] - x2[i])

	return dist

def abs(number):
	"""
	Compute absolute value for a given number.

	Parameters:
	-----------
	number: a number (float)

	Return:
	-------
	number: the absolute value of number (float)
	"""

	if number < 0:
		number *= -1
	return number