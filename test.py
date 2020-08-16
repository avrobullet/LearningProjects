import numpy as np
import databricks

dict = {
    'a':0,
    'b':0,
    'c':0
}
sentence = ['a b c d e f g']
for key in dict:
    map = np.isin(sentence[0].split(),key)
    dict[key] += sum(map)

print(dict)

