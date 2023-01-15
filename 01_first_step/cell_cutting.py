# + read image
# + find height and width
# + find cell size
# + crop cells
# + add cells to list
# + boundary conditions check
# + add border
#   add gap
# the file should be in the same folder as the function

import cv2


def crop_image(file_name, rows=1, columns=1, border=0, gap=0):
    # read image, file_name as string
    image = cv2.imread(file_name)

    # find height and width
    width = image.shape[0]
    height = image.shape[1]

    # boundary conditions check
    if (rows > width or rows <= 0) or (columns > height or columns <= 0):
        print("outside of pixel sizes or pixel range")
    elif border < 0 or border >= width // 2 or border >= height // 2:
        print("border out of range")
    else:
        # border
        bordered_image = image[0 + border:width - border, 0 + border:height - border]

        # find height and width
        width = bordered_image.shape[0]
        height = bordered_image.shape[1]

        # find cell size
        cell_width = width // rows
        cell_height = height // columns

        # crop cells
        x = 0
        cropped_pictures = []
        while x + cell_height <= height:
            y = 0
            while y + cell_width <= width:
                cropped = bordered_image[y:y + cell_width, x:x + cell_height]
                y += cell_width

                # add cells to list
                cropped_pictures.append(cropped)
            x += cell_height
        return cropped_pictures
