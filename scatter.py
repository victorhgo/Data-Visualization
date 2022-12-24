""" We can use scatter() to style individual points"""
import matplotlib.pyplot as plotting

"""plotting.scatter(2, 4)
plotting.show()"""

# We can style the output to make the graphics more interesting
""" s= is the size of used points"""
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plotting.scatter(x_values,y_values,s=50)
plotting.title("Square",fontsize=12)
plotting.xlabel("Number",fontsize=12)
plotting.ylabel("Square of Number",fontsize=12)
plotting.tick_params(axis='both',which='major',labelsize=7)
plotting.show()

