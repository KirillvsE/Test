# + read image
# + find height and width
# + find cell size
# + crop cells
# + add cells to list
# + boundary conditions check
# the file should be in the same folder as the function

import cv2


def get_crop(image, width, height, column, row):
    # find cell size
    cell_height = height // column
    cell_width = width // row

    # crop cells
    x = 0
    cropped_pictures = []
    while x + cell_height <= height:
        y = 0
        while y + cell_width <= width:
            cropped = image[y:y + cell_width, x:x + cell_height]
            y += cell_width

            # add cells to list
            cropped_pictures.append(cropped)
        x += cell_height
    return cropped_pictures


def get_cropping_pictures(row, column, file_name):
    # read image, file_name as string
    image = cv2.imread(file_name)

    # find height and width
    width = image.shape[0]
    height = image.shape[1]

    # boundary conditions check
    if row > width or 0 >= row or column > height or column <= 0:
        print("outside of pixel sizes or pixel range")
    else:
        return get_crop(image, width, height, column, row)
