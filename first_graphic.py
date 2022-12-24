import matplotlib.pyplot as plotting

""" Let's start our test by generating a simple linear graphic. After
testing it, we will proceed to create a more informative data visualization."""

# Our data will be the sequence 1, 2, 3, 4 and 5 squared as data for the graphics.
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plotting.plot(input_values,squares, linewidth = 3)
""" Let's put a title on our graphic and name the axis"""
plotting.title("Square numbers",fontsize = 12)
plotting.xlabel("Number",fontsize=12)
plotting.ylabel("Square of number",fontsize=12)
""" Define the mark stamp size"""
plotting.tick_params(axis='both',labelsize=7)
plotting.show()




