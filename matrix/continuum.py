"""
Defines a color continuum
"""

continuum = (
    (4, 4, 74),
    (0, 21, 97),
    (1, 42, 132),
    (1, 70, 171),
    (0, 100, 214),
    (2, 100, 147),
    (0, 97, 86),
    (1, 95, 45),
    (0, 92, 17),
    (5, 116, 13),
    (80, 149, 4),
    (167, 188, 0),
    (255, 228, 1),
    (249, 156, 0),
    (232, 91, 1),
    (217, 37, 0),
    (206, 0, 2),
    (206, 0, 10),
    (206, 0, 23),
    (207, 0, 44)
)

def get_color(in_val, min_val=0, max_val=100):
    """
    Returns a color within the scale
    """
    width = max_val - min_val
    unit = width / len(continuum)
    return continuum[min(int(in_val / unit), 19)]
