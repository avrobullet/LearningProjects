import numpy as np

labels = np.array(
    [[1, 0, 0],
     [0, 1, 1],
     [1, 0, 1],
     [1, 1, 1],
     [1, 0, 1]]
)

N = np.size(labels,0)
patient_1 = np.array(labels[0])
# x = lambda a : a + 10
def sensitivity(patient_1):
    total_positives_tested = sum(testing_positive for testing_positive in patient_1 if testing_positive==1)
    return np.true_divide(total_positives_tested, len(patient_1))

specificity = lambda testing_negative:sum(testing_negative for testing_negative in patient_1
                                                            if testing_negative==0)/len(patient_1)

print(sensitivity(patient_1), specificity(patient_1))
