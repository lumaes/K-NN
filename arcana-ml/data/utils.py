def feature_array_from_dataset(dataset, column_index):
    """
    """
    result = []
    # for each entry of the dataset
    for subarray in dataset:
        # check if wanted column index is in the size of the dataset
        if len(subarray) > column_index and column_index >= 0:
            # append the value to the result
            result.append(subarray[column_index])
    # return the result
    return result

def split_feature_from_label(dataset, column_index):
    """
    """

    new_dataset = []

    # for each entry of the dataset
    for subarray in dataset:
        # check if wanted column index is in the size of the dataset
        if len(subarray) > column_index and column_index >= 0:
            

