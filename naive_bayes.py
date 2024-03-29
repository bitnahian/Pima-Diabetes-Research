import csv
import math
import statistics


# For every attribute in the yes and no list, calculate the mean and variance using statistics lib
def cal_mean_var(dataset):
    list_mean = {}
    list_var = {}

    for i in range(len(dataset[0]) - 1):
        column = list(map(lambda row: float(row[i]), dataset))
        list_mean[i] = statistics.mean(column)
        list_var[i] = statistics.variance(column, list_mean[i])

    return list_mean, list_var


# Calculate the pdf for the no classifier given the specific value, the type of attribute, mean and variance
# Return the value for further calculation
def pdf(x, index, list_var, list_mean):
    power = math.pow((x - list_mean[index]), 2) / (2 * list_var[index])
    exponent_val = math.pow(math.e, -power)

    final_val = (1 / (math.sqrt(2 * list_var[index] * math.pi))) * exponent_val

    return final_val
