import numpy as np 


arr = np.random.randint(0,10, size=(10,10))

print(arr)

new_arr = np.rot90(arr, 1)

print(new_arr)