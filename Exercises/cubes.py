""" Write the first 5000 numbers cubed"""
import matplotlib.pyplot as plotting

x_axis = list(range(1,5001))
y_axis = [x**3 for x in x_axis]

plotting.scatter(x_axis,y_axis,s = 10,c='green',edgecolors='none')

plotting.title('Cubes from 1 to 5000',fontsize=12)
plotting.xlabel('Numbers',fontsize=12)
plotting.ylabel('Cube of Number',fontsize=12)
plotting.tick_params(axis='both',which='major',labelsize=7)

plotting.savefig('Generated/cubes.png',bbox_inches='tight')