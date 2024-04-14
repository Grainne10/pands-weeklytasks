# Week 8.plottask.py  
# Program  should display a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

# author Grainne Boyle

import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)

# Define the range of x values
x = np.linspace(0, 10, 100 )

# Create a function - the variable h defines the function
h = x**3

# Create histogram with the data and plot the labels
plt.hist(data, color='yellow', edgecolor='black')
plt.ylabel('Frequency')
plt.xlabel('Values')
plt.title('Histogram of Normal Distribution and Plot of h(x) = x^3')
# Plot the function h(x) = x^3
plt.plot(x, h, color='green', label='h(x) = x^3')


# You can save the plot as a PNG file
plt.savefig('plot.png')
