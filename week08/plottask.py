# This program should display a histogram of a normal distribution of a 1000 values,
# with a mean of 5 and standard deviation of 2,
# and a plot of the function h(x)=x^3 in the range 0 to 10
# Author: Joanna Kelly

import numpy as np
import matplotlib.pyplot as plt

mean = 5
std_dev = 2
number_of_values = 1000  #Labelling variables outside the function allows us to change the variables easily

np.random.seed(1)  #so that the values remain the same
normal_dist = np.random.normal(loc= mean, scale= std_dev, size= number_of_values) # Use random.normal to get a normal distributiion
#loc = mean
#scale = standard deviation
#size = the number of values or shape of the returned array

xpoints = np.array(range(0, 10))
ypoints = xpoints ** xpoints


plt.hist(normal_dist, color= "skyblue", label= "Histogram") #alpha sets the opacity of the histogram
#plt.plot(xpoints, ypoints, color = "hotpink", label= "h(x) = x^3")

plt.xlabel("x")
plt.ylabel("Frequency")
plt.title("Histogram and Plot of h(x) = x^3")
plt.legend()
plt.grid(True)

plt.show()

# Cannot get histogram and plot to show together, I imagine because of the huge difference in range.
# Not sure what to do :(