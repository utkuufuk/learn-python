import matplotlib.pyplot as plt

values = list(range(1, 1001))
squares = [i ** 2 for i in values]

# simple line graph
plt.plot(values, squares, c='red', linewidth=5)                 # set line color and thickness
plt.title("Square Numbers", fontsize=24)                        # set figure title
plt.xlabel("Value", fontsize=14)                                # set title for the x-axis
plt.ylabel("Square of Value", fontsize=14)                      # set title for the y-axis
plt.tick_params(axis='both', labelsize=14)                      # set size of tick labels
plt.show()

# scatter plot
plt.scatter(values, squares, edgecolor='none', s=40)            # don't color edges and set dot size to 40
plt.axis([0, 1100, 0, 1100000])                                 # set range for each axis
plt.savefig('squares_scatter_plot.png', bbox_inches='tight')    # save the plot to a file (trim extra whitespace)
plt.show()
