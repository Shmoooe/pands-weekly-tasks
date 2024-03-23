import numpy as np
import matplotlib.pyplot as plt

mean = 5
std_dev = 2
number_of_values = 1000

np.random.seed(1)
normal_dist = np.random.normal(loc=mean, scale=std_dev, size=number_of_values)

# Generate x values for the function h(x) = x^3
xpoints = np.linspace(0, 10)
ypoints = xpoints ** xpoints

# Create a new figure
plt.figure(figsize=(8, 6))

# Plot the histogram
plt.hist(normal_dist, bins=30, alpha=0.5, color='skyblue', label="Histogram")

# Plot the function
plt.plot(xpoints, ypoints, color="hotpink", label="h(x) = x^3")

# Add labels, title, legend, and grid
plt.xlabel('x')
plt.ylabel('Frequency / h(x)')
plt.title('Histogram and Plot of $h(x) = x^3$')
plt.legend()
plt.grid(True)

# Display the combined plot
plt.show()
