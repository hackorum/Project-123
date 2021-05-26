import numpy as np

data = np.load('image.npz', allow_pickle=True)
lst = data.files

for item in lst:
    print(item)
    print(data[item])
