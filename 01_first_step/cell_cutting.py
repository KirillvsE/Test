# + read image
# + find height and wide
# + find cell size
# + crop cells
# +	add cells to list

import cv2


def get_cutting_pictures(row, column, image_name):
    # read image
    image = cv2.imread(image_name)

    # find height and wide
    height = image.shape[0]
    width = image.shape[1]

    # find cell size
    cell_height = height // row
    cell_width = width // column

    # crop cells
    x = 0
    cropped_cell = []
    while x + cell_height <= height:
        y = 0
        while y + cell_width <= width:
            cropped = image[y:y + cell_width, x:x + cell_height]
            y += cell_width

            # add cells to list
            cropped_cell.append(cropped)
        x += cell_height
    return cropped_cell


cell_list = get_cutting_pictures(3, 8, "72.jpg")

print(cell_list)
