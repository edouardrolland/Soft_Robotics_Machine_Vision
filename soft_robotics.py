

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def extract_coordinates(image_name):

    img = cv.imread(image_name)
    height, width = img.shape[:2]
    scale_percent = 40
    # Calculer les nouvelles dimensions de l'image
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    dim = (new_width, new_height)

    # Redimensionner l'image
    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    cv.imshow('Initial_Picture',resized)

    img_crop = resized[440:658,0:422]
    cv.imshow("Cropped_Picture",img_crop)
    img_crop = cv.medianBlur(img_crop, 7)

    img_hsv = cv.cvtColor(img_crop, cv.COLOR_BGR2HSV)
    cv.imshow("HSV colour space",img_hsv)

    # detecting points by color
    red_hsv_lower = np.array([0, 50, 50])
    red_hsv_higher = np.array([10, 255, 255])
    mask1 = cv.inRange(img_hsv, lowerb=red_hsv_lower, upperb=red_hsv_higher)

    red_hsv_lower = np.array([156, 50, 50])
    red_hsv_higher = np.array([180, 255, 255])
    mask2 = cv.inRange(img_hsv, lowerb=red_hsv_lower, upperb=red_hsv_higher)
    mask = mask1 + mask2
    cv.imshow("Detection", mask)

    # detecting contours
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    # finding centers of contours
    centers = []

    for cnt in contours:
        (x, y), radius = cv.minEnclosingCircle(cnt)
        center = (int(x), int(y))

        centers.append(center)

    # Initialiser les listes vides pour les coordonnées X et Y
    x_coords = []
    y_coords = []

    # Itérer sur chaque tuple dans la liste et extraire les coordonnées
    for coord in centers:
        x_coords.append(coord[0])
        y_coords.append(coord[1])


    # combiner les deux listes de coordonnées en une liste de tuples
    coords = list(zip(x_coords, y_coords))

    # trier la liste de tuples en fonction de la première coordonnée (X) en ordre croissant
    coords_sorted = sorted(coords, key=lambda x: x[0])

    # séparer les coordonnées triées en deux listes distinctes de X et de Y
    x_coords = [coord[0] for coord in coords_sorted]
    y_coords = [coord[1] for coord in coords_sorted]

    #plt.scatter(x_coords, y_coords)
    #plt.gca().invert_yaxis()
    #plt.axis("equal")
    #plt.grid()
    #plt.show()



    return [x_coords,y_coords]

