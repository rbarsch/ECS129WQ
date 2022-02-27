import random
import numpy as np
import matplotlib.pyplot as plt
import math 

sphere_storage = []
random_plots = []
x_list = []
y_list = []
z_list = []

class Point (object):
    def __init__(self, x, y, z, radius):
        self.x, self.y, self.z, self.radius = x,y,z,radius   

def main():
    #function will read all file lines and push data into a singular class
    filename = input("Please provide data file: ")
    f = open(filename, 'r')
    num_protein = f.readline()

    for line in f:
        cur_coords = line
        # split each line by whitespace and get the 3-D coordinates and radius
        # idea is combine these into a single list to be easier
        x,y,z,rad = cur_coords.split()
        x_list.append(float(x)+float(rad))
        y_list.append(float(y)+float(rad))
        z_list.append(float(z)+float(rad))
        x_list.append(float(x)-float(rad))
        y_list.append(float(y)-float(rad))
        z_list.append(float(z)-float(rad))
        # store each point in the object
        cur_point = Point(x,y,z,rad)
        # add object to an array of points
        sphere_storage.append(cur_point) 
        #increments counter
    f.close()
    return

def max_min():
    xmax = max(x_list)
    xmin = min(x_list)
    ymax = max(y_list)
    ymin = min(y_list)
    zmax = max(z_list)
    zmin = min(z_list)
    return xmax,xmin,ymax,ymin,zmax,zmin

def random_points(xmax,xmin,ymax,ymin,zmax,zmin):
    n_input = int(input("Please give N number of points: "))
    for i in range(n_input):
        #is it good to add to a outside list from a fxn for storage?
        random_plots.append((random.randrange(int(math.floor(xmin)),int(math.ceil(xmax))),random.randrange(int(math.floor(ymin)),int(math.ceil(ymax))),random.randrange(int(math.floor(zmin)),int(math.ceil(zmax)))))
        # random_plots.append(random.randrange(int(math.floor(xmin))),int(math.ceil(xmax)))),random.randrange(int((math.floor(ymin)),int((math.ceil(ymax))))))
    return n_input

def overlap_check():
    #right now this only checks if something is inside another circle, not if its in the union of multiple circles
    union_of_circle = 0
    for out in random_plots:
        for center in sphere_storage:
            if (((float(out[0]) - float(center.x))**2) + ((float(out[1]) - float(center.y))**2) + ((float(out[2]) - float(center.z))**2)) <= float(center.radius)**2:
                union_of_circle += 1
                break
    return union_of_circle

def protein_vol(xmax,xmin,ymax,ymin,zmax,zmin,union_of_circle,n_input):
#equation is (xmax-xmin)(ymax-ymin)(zmax-zmin)(points in union of balls/total of point)
#easier way to turn everything into a float at once?
    volume_of_protein = (xmax-xmin)*(ymax-ymin)*(zmax-zmin)*(union_of_circle/n_input)
    return volume_of_protein

def plot_data():
# will plot and display all data points
# blue is sample_data points
    for sphere in sphere_storage:
        plt.scatter(float(sphere.x),float(sphere.y), c = 'blue')
# red is random points
    for points in random_plots:
        plt.scatter(float(points[0]),float(points[1]), c = 'red')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('sample_data')
    plt.show()

#will auto run main fxn at start of program being run
if __name__ == "__main__":
    #reads file and applies class and puts data into list
    main()   
    #find mins and max of all data
    xmax,xmin,ymax,ymin,zmax,zmin = max_min()
    print(xmax,xmin,ymax,ymin,zmax,zmin)
    #request from user number of random points wanted
    n_input = random_points(xmax,xmin,ymax,ymin,zmax,zmin)
    # checks for all points that are in union of a circle
    # test_max_min()
    union_of_circle = overlap_check()
    #calculates volume of our protein
    volume_of_protein = protein_vol(xmax,xmin,ymax,ymin,zmax,zmin,union_of_circle,n_input)
    #plots all data by center points only
    print("# of points in union of circle: ", union_of_circle)
    print("volume of protein: ",volume_of_protein)
    #run comment this for data to be plotted, does make running program a bit slower in test
    # plot_data()