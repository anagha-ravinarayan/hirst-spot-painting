import colorgram


def get_random_color_tuples():
    colorgram_colors = colorgram.extract('resources/image.jpg', 30)
    colors = []

    for color in colorgram_colors:
        colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

    return colors
