import csv
import itertools
import MyClassifier as mc

''' Reads from the given file name and produces folded lists
'''
def read_fold(filename):
    fold_no = -1
    folds = []
    with open(filename, 'r', newline = '') as myfile:
        reader = csv.reader(myfile, delimiter=',')
        for row in reader:
            if len(row) > 0:
                if 'fold' in row[0]:
                    fold_no += 1
                    folds.append([])
                    continue
                folds[fold_no].append(row)
    return folds
def calculate_accuracy(testing_set, outputs):
    size = len(testing_set)
    positive = 0
    # The last value is the yes/no
    for i, row in enumerate(testing_set):
        val = row[-1]
        if val == outputs[i]:
            positive += 1
    
    return positive/size

def test_accuracy(folds, classifier):
    accuracy = []
    for i in range(len(folds)):
        training_set = list(itertools.chain(*folds[:i], *folds[i+1:]))
        testing_set = folds[i]
        outputs = classifier(training_set, testing_set)
        accuracy.append(calculate_accuracy(testing_set, outputs))
    
    return mc.nb.statistics.mean(accuracy) 

if __name__ in "__main__":
    # Read in all the discretised data

    pima_discretised_folds = read_fold('pima-discretised-folds.csv') 
    pima_discretised_CFS_folds = read_fold('pima-discretised-CFS-folds.csv')
    pima_folds = read_fold('pima-folds.csv')
    pima_folds_CFS = read_fold('pima-CFS-folds.csv') 

    cross_validation_accuracy_dt = test_accuracy(pima_discretised_folds, mc.run_dt)
    cross_validation_accuracy_CFS_dt = test_accuracy(pima_discretised_CFS_folds, mc.run_dt)
    cross_validation_accuracy_nb = test_accuracy(pima_folds, mc.run_nb)
    cross_validation_accuracy_CFS_nb = test_accuracy(pima_folds_CFS, mc.run_nb) 

    print("cross validation accuracy for pima-discretised-folds.csv : {}".format(cross_validation_accuracy_dt))
    print("cross validation accuracy for pima-discretised-CFS-folds.csv : {}".format(cross_validation_accuracy_CFS_dt))
    print("cross validation accuracy for pima-folds.csv : {}".format(cross_validation_accuracy_nb))
    print("cross validation accuracy for pima-CFS-folds.csv : {}".format(cross_validation_accuracy_CFS_nb))

    
