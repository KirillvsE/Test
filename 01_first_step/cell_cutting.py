
import cv2


def crop_image(file_name, rows=1, columns=1, border=0, gap=0, cell=(None, None)):
    # read image, file_name as string
    image = cv2.imread(file_name)

    # find height and width
    height = image.shape[0]
    width = image.shape[1]

    # boundary conditions check
    if border < 0 or border >= width // 2 or border >= height // 2:
        print("border out of range or ")
    else:
        # border
        bordered_image = image[0 + border:height - border, 0 + border:width - border]

        # find height and width
        height = bordered_image.shape[0]
        width = bordered_image.shape[1]

        if (rows > height or rows <= 0) or (columns > width or columns <= 0):
            print("outside of pixel sizes or pixel range")
        elif gap < 0 or ((height - gap * (rows - 1)) // rows) < 1 or ((width - gap * (columns - 1)) // columns) < 1:
            print("gap out of range or ")

        else:
            if cell != (None, None):
                cell_width = cell[0]
                cell_height = cell[1]

                rows = height // (cell_height + gap)
                columns = width // (cell_width + gap)

            else:
                # find cell size
                cell_height = (height - gap * (rows - 1)) // rows
                cell_width = (width - gap * (columns - 1)) // columns

            # crop cells
            cropped_pictures = []

            x = 0
            y = 0
            for count_columns in range(columns):
                y = 0
                for count_rows in range(rows):
                    cropped = bordered_image[y:y + cell_height, x:x + cell_width]
                    cropped_pictures.append(cropped)
                    y = y + cell_height + gap
                x = x + cell_width + gap

            # adding incomplete cells
            if x < width:
                y = 0
                for count_rows in range(rows):
                    cropped = bordered_image[y:y + cell_height, x:width]
                    cropped_pictures.append(cropped)
                    y = y + cell_height + gap
            if y < height:
                x = 0
                for count_columns in range(columns):
                    cropped = bordered_image[y:height, x:x + cell_width]
                    cropped_pictures.append(cropped)
                    x = x + cell_width + gap

            return cropped_pictures
