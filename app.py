import cv2
import numpy as np
import svgwrite

def raster_to_vector(image_path, svg_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create SVG
    dwg = svgwrite.Drawing(svg_path)
    for contour in contours:
        points = [(point[0][0], point[0][1]) for point in contour]
        dwg.add(dwg.polygon(points))
    
    dwg.save()

raster_to_vector('input_image.png', 'output_image.svg')
