import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from sympy import Circle, Point
import numpy as np



def bending_calculations(x1,y1,x2,y2,x3,y3):


    # Calculation of the Euclidean distance between points
    a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Calculation of the half perimeter of the triangle
    s = (a + b + c) / 2

    # Calculating the radius of the circle
    radius = (a * b * c) / (4 * math.sqrt(s * (s - a) * (s - b) * (s - c)))

    point1 = Point(x1,y1)
    point2 = Point(x2,y2)
    point3 = Point(x3,y3)
    circle = Circle(point1, point2, point3)
    center = circle.center

    # Calculating the coordinates of the centre of the circle
    x_center = center.x
    y_center = center.y

    # Calculating the start and end angles of the arc
    v1 = (x1 - x_center, y1 - y_center)
    v2 = (x2 - x_center, y2 - y_center)
    v3 = (x3 - x_center, y3 - y_center)

    theta1 = math.atan2(v1[1], v1[0])
    theta2 = math.atan2(v3[1], v3[0])

    # Displaying the properties of the circle
    print("Circle center : (", x_center, ",", y_center, ")")
    print("Circle radius : ", radius)
    print("Bending angle : ", (theta2 - theta1) % (2 * math.pi), "radians")

    """
    # Drawing the arc in a graphics window
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    arc = Arc((x_center, y_center), radius*2, radius*2, theta2=theta2*180/math.pi, theta1=theta1*180/math.pi)
    ax.add_patch(arc)

    plt.scatter([x1, x2, x3], [y1, y2, y3])
    plt.scatter(center.x,center.y)
    plt.plot([x1,center.x],[y1, center.y], 'g--')
    plt.plot([x3,center.x],[y3, center.y], 'g--')
    plt.gca().invert_yaxis()
    plt.axis('equal')
    plt.grid()
    plt.show()
    """
    return (theta2 - theta1) % (2 * math.pi)*180/np.pi
