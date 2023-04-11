import os
from pinhead_coordinates import extract_coordinates
import matplotlib.pyplot as plt
import numpy as np
from circle_fit import standardLSQ
from circle_fit import plot_data_circle
from matplotlib.patches import Circle
from sympy import Circle, Point
import math
from bending_measurement import bending_calculations
from scipy import stats

path = r"C:\Users\edoua\Desktop\Soft Robotics\Python Bending\Images_Bis"

# Ouvrir le dossier et extraire les noms des fichiers
liste_fichiers = os.listdir(path)
liste_fichiers.sort()

# Afficher la liste des fichiers
Curves = []
for k in range(len(liste_fichiers)):
    Curves.append(extract_coordinates(path + "\\"  +liste_fichiers[k]))

#Sorting of points for a coherent display
for k in range(len(Curves)):
    x_temp = Curves[k][0]
    y_temp = Curves[k][1]

    if k == 7:
        Curves[k][0][-1], Curves[k][0][-2] = Curves[k][0][-2], Curves[k][0][-1]
        Curves[k][1][-1], Curves[k][1][-2] = Curves[k][1][-2], Curves[k][1][-1]

    if k > 7:
        Curves[k][0][-1], Curves[k][0][-2] = Curves[k][0][-2], Curves[k][0][-1]
        Curves[k][1][-1], Curves[k][1][-2] = Curves[k][1][-2], Curves[k][1][-1]
        Curves[k][0][0], Curves[k][0][1] = Curves[k][0][1], Curves[k][0][0]
        Curves[k][1][0], Curves[k][1][1] = Curves[k][1][1], Curves[k][1][0]

plt.figure("Extraction of gripper gaits")

#Plotting a skelleton representation

for k in range(len(Curves)):

    if k%2 == 0 :
        plt.plot(Curves[k][0], Curves[k][1], label = str(k*5) + ' ml')
        plt.scatter(Curves[k][0], Curves[k][1])

plt.title("Gripper gaits for different injected volume values",fontsize = 40)
plt.xlabel("x (pixels)", fontsize = 20)
plt.ylabel("y (pixels)", fontsize = 20)
plt.gca().invert_yaxis()
plt.axis("equal")
plt.grid()
plt.legend(loc='best', prop={'size': 15})
plt.show()

#Circular regression results


plt.figure("Circular Regression")
rayons = []
coords_circles = []
volumes = []
precisions = []
scale_ratio = 20/455

for k in range(len(Curves)):
    xc, yc, r, sigma = standardLSQ(list(zip(Curves[k][0], Curves[k][1])))
    rayons.append(r*scale_ratio)
    volumes.append(k*5)
    precisions.append(sigma)
    coords_circles.append([xc,yc])

    plt.plot(volumes, rayons)
    plt.grid()
    plt.title("Gripper tightening radius as a function of injected air volume", fontsize =40 )
    plt.xlabel("Volume of injected air (ml)",fontsize = 20)
    plt.ylabel("Gripper tightening radius (cm)",fontsize = 20)

plt.show()
plt.figure("Residual Error display")
plt.title("Evolution of the residual error for the different regressions", fontsize = 40 )
plt.xlabel("Volume (ml)", fontsize = 20)
plt.ylabel("Residual error", fontsize = 20)
plt.plot(volumes, precisions)
plt.grid()
plt.show()

#Circular regression display
plt.figure("Circular Regression Display")
for k in range(len(Curves)):
    xc, yc, r, sigma = standardLSQ(list(zip(Curves[k][0], Curves[k][1])))
    #plot_data_circle(list(zip(Curves[k][0], Curves[k][1])), xc, yc, r)
    plt.title("Circular Fitting for a volume of air of " + str(5*k) + " ml", fontsize=40)
    plt.gca().invert_yaxis()
plt.show()

#Bending Air Measurement

bending = []


for k in range(len(Curves)):

    x1 = Curves[k][0][0]
    y1 = Curves[k][1][0]

    x2 = Curves[k][0][2]
    y2 = Curves[k][1][2]


    x3 = Curves[k][0][-1]
    y3 = Curves[k][1][-1]

    extract_coordinates(path + "\\"  +liste_fichiers[k])
    res = bending_calculations(x1,y1,x2,y2,x3,y3)
    bending.append(res)


slope, intercept, r_value, p_value, std_err = stats.linregress(volumes[0:-2], bending[0:-2])

def f(x):
    return slope*x + intercept

X_regression = np.linspace(0,60,10)
Y_regression = [f(x) for x in X_regression]

plt.figure("Bending Measurements")
plt.scatter(volumes, bending)
plt.plot(X_regression, Y_regression, 'r--')
plt.title("Evolution of the bending angle", fontsize = 40)
plt.xlabel("Volume (ml)", fontsize = 20 )
plt.ylabel("bending angle (°)", fontsize = 20)
plt.text(40, 90, '$R^2 =$' + str(round(r_value,3)), fontsize=30, ha='center', va='center')
plt.grid()
plt.show()








