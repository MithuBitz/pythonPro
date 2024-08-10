import math
# Function Returning Multiple Values

def circle_calculations(radius):
    area = math.pi * (radius ** 2)
    area_formated = round(area, 2)
    circumferance = 2 * math.pi * radius
    circumferance_formatted = round(circumferance, 2)
    return area, circumferance, area_formated, circumferance_formatted


a, c, af, cf = circle_calculations(3) # Two output can be handled like this
print("Area: ", a, "Circumferance: ", c)
print("Formated Area: ", af, "Formatted Circumferance: ", cf)