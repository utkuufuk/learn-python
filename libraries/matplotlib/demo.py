import matplotlib.pyplot as plt
from numpy import *

values = list(range(1, 1001))
squares = [i ** 2 for i in values]

# simple line graph
plt.figure();
plt.plot(values, squares, c='red', linewidth=5)                 # set line color and thickness
plt.title("Square Numbers", fontsize=24)                        # set figure title
plt.xlabel("Value", fontsize=14)                                # set title for the x-axis
plt.ylabel("Square of Value", fontsize=14)                      # set title for the y-axis
plt.tick_params(axis='both', labelsize=14)                      # set size of tick labels

# scatter plot
plt.figure();
plt.scatter(values, squares, edgecolor='none', s=40)            # don't color edges and set dot size to 40
plt.axis([0, 1100, 0, 1100000])                                 # set range for each axis
plt.savefig('squares_scatter_plot.png', bbox_inches='tight')    # save the plot to a file (trim extra whitespace)

# multiple plots in one figure
plt.figure();
x = [1, 2, 3, 2, 1]
y = [1, 3, 2, 3, 1]
plt.subplot(2, 1, 1)                                            # rows=2, cols=1, active plot=1
plt.plot(x)
plt.subplot(2, 1, 2)                                            # rows=2, cols=1, active plot=2
plt.plot(y)

# legend
plt.figure();
x = linspace(0, 2 * pi, 50)                                     # create linearly spaced values
plt.plot(sin(x))
plt.plot(cos(x))
plt.legend(['sin', 'cos'], loc='best')                          # put the legend to a convenient location

# display all plots
plt.show()
