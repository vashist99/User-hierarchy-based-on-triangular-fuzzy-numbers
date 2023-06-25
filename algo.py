import numpy as np
import math
import time

input_array = np.random.randint(
    1000000000, size=(10000000, 3, 3)).astype("float")
weights_array = np.array([0.2, 0.3, 0.5])

start_time = time.time()
# normalization begin
collection_of_sum = []
sum = 0
for j in range(input_array.shape[1]):
    for i in range(3):
        for k in range(input_array.shape[0]):
            sum += math.pow(input_array[k, j, i], 2)

        collection_of_sum.append(sum)
        #input_array[k, j, i] = 0
        sum = 0

# Alternative
# collection_of_sum = np.sum(input_array, axis=0)
# print(len(collection_of_sum))

collection_of_sum = np.sqrt(collection_of_sum)

sum_index = 0
for j in range(input_array.shape[1]):
    for i in range(3):
        for k in range(input_array.shape[0]):
            input_array[k, j, i] = input_array[k, j, i] / \
                collection_of_sum[sum_index]
        sum_index += 1

# print(input_array)

# normalization end

# multiplication by weights begin.
for k in range(input_array.shape[0]):
    for j in range(input_array.shape[1]):
        for i in range(3):
            input_array[k, j, i] = input_array[k, j, i]*weights_array[j]

# print(input_array)
# multiplication by weights end

# find Positive Ideal Solution Begin.
X = np.max(input_array, axis=0)
print()
# find Positive Ideal Solution End

# find distance from PIS begin
distance = []
for k in range(input_array.shape[0]):
    for j in range(input_array.shape[1]):
        d = math.sqrt((1/3)*(math.pow(input_array[k, j, 0] - X[j, 0], 2)+math.pow(
            input_array[k, j, 1] - X[j, 1], 2)+math.pow(input_array[k, j, 2] - X[j, 2], 2)))
    distance.append(d)
    d = 0

# print(len(distance))
# find distance from PIS end

# sort
distance.sort()

end_time = time.time()

print("time elapsed: ", end_time-start_time)
