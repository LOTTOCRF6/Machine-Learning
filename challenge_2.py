import numpy as np
import matplotlib.pyplot as plt
nums = np.array([0.5, 0.7, 1., 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print("nums: ", nums)
print("bins: ", bins)
print("Result:", np.histogram(nums, bins))
plt.hist(nums, bins=bins, color="Grey")
plt.title("Histogram of nums against bins.", color="gold")
plt.xlabel("Nums", color="green")
plt.ylabel("Bins", color="Orange")
plt.show()