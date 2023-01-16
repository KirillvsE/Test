









import cv2


def crop_image(file_name, rows=1, columns=1, border=0, gap=0):
    # read image, file_name as string
    image = cv2.imread(file_name)

    # find height and width
    height = image.shape[0]
    width = image.shape[1]

    # boundary conditions check
    if (rows > width or rows <= 0) or (columns > height or columns <= 0):
        print("outside of pixel sizes or pixel range")
    elif border < 0 or border >= width // 2 or border >= height // 2:
        print("border out of range")
    elif gap < 0 or gap > (height - gap * rows) // 2 or gap > (width - gap * columns) // 2:
        print("gap out of range")
    else:
        # border
        bordered_image = image[0 + border:height - border, 0 + border:width - border]

        # find height and width
        height = bordered_image.shape[0]
        width = bordered_image.shape[1]

        # find cell size
        cell_height = (height - gap * rows) // rows
        cell_width = (width - gap * columns) // columns

        # crop cells
        cropped_pictures = []

        x = 0
        for count_rows in range(columns):
            y = 0
            for count_columns in range(rows):
                cropped = bordered_image[y:y + cell_height, x:x + cell_width]
                cropped_pictures.append(cropped)
                y = y + cell_height + gap
            x = x + cell_width + gap

        # adding incomplete cells
        if x < width:
            y = 0
            for count_columns in range(rows):
                print(x, ":", y)
                cropped = bordered_image[y:y + cell_height, x:width]
                cropped_pictures.append(cropped)
                y = y + cell_height + gap
        if y < height:
            x = 0
            for count_rows in range(columns):
                print(x, ":", y)
                cropped = bordered_image[y:height, x:x + cell_width]
                cropped_pictures.append(cropped)
                x = x + cell_height + gap

        return cropped_pictures
