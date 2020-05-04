import numpy as np

labels = np.array(
    [[1, 0, 0],
     [0, 1, 1],
     [1, 0, 1],
     [1, 1, 1],
     [1, 0, 1]]
)
N = np.size(labels,0)

test_array = [np.sum(labels, axis=0)]
test_array_demo = np.array([(N-elem)/N for elem in np.array(np.sum(labels, axis=0))])

labels = list(np.sum(labels, axis=0))
negative_class = np.array([(N-elem)/N for elem in labels])
postive_class = np.array([elem/N for elem in test_array])
print(test_array)
print(labels)
print(negative_class)
print(postive_class)
print("This:",test_array_demo)
print(N)
