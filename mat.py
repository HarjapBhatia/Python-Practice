#pip install matplotlib
from matplotlib import pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]
plt.plot(x,y)
plt.xlabel("age")
plt.title("linear graph")
plt.ylabel("year")
plt.show()  