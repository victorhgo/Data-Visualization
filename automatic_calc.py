""" We can create a range to plot a graphics"""
import matplotlib.pyplot as plotting

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plotting.scatter(x_values,y_values,s = 10,
                 c=y_values,edgecolors='none',cmap=plotting.cm.Blues)
plotting.title("Square",fontsize=12)
plotting.xlabel("Number",fontsize=12)
plotting.ylabel("Square of Number",fontsize=12)
""" To specify the interval of each axis: The axis function requires
four values: the minimum and maximum value for x and y axis"""
plotting.tick_params(axis='both',which='major',labelsize=7)
plotting.axis([0, 1100,0,1100000])
# plotting.show()

""" We can define colors using the c argument on scatter().
Colormap : cmap=plotting.cm.Blues"""

""" We can save the graphics by using the savefig() instead of show()
We can specify where it will be stored."""
plotting.savefig('squares_plot.png',bbox_inches='tight')