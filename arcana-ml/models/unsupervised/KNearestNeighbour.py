from .model import Model
from .math.method import *
from .math.statistics import *
import copy

class KNN(Model):
    """
    """

    def __init__(self, data, k=3, classification=True, distance):
        super().__init__(data)
        self.predict_data = copy.deepcopy(data)
        self.k = k
        self.classification = classification
        self.distance = distance
        self.neighbors = []

    def train(self):
        # no train needed for unsupervised algorithm
        pass

    def predict(self, new_entry, k=self.k):
        """ Recursive algorithm.
        """
        # Default case
        # if algorithm is finish, then return the result wanted
        if k == 0:
            # reset the deep copy
            self.predict_data = copy.deepcopy(self.data)
            # regression problem
            if not self.classification:
                # return mean of neighbors
                return mean_y(self.neighbors)
            # classification problem
            else:
                # get all most present labels in the neighbors
                result = [pt[-1] for pt in self.neighbors]
                return max(set(result), key = result.count)        

        # Inductive case
	    else:
            # init most 
            min_point = self.predict_data[0]
            # get the minimum distance of the dataset
            for point in self.predict_data:
                if distance(point[0], new_entry) <= self.distance(min_point[0], new_entry):
                    min_point = point

            # add min point to neighbors list
            self.neighbors.append(min_point)
            # remove the min_point from dataset
            self.predict_data.remove(min_point)

            return predict(self, new_entry, k=(k-1))
