# import modules
from kandinsky import *

# draw image from file
def picture(file, x_offset=0, y_offset=0, scale=1):
    # set background to white
    fill_rect(0, 0, 320, 222, (255, 255, 255))

    # open given file
    file = open(file)

    # get resolution of image
    file.seek(1)
    res_x = int(file.read(4))
    file.seek(4)
    res_y = int(file.read(4))

    # init at right bit
    pxl_index = 9
    pxl_color = ["", "", ""]

    # draw depending on resolution
    for y in range(res_y):
        for x in range(res_x):
            # get current color from file
            for c in range(3):
                file.seek(pxl_index)
                pxl_color[c] = int(file.read(3))
                pxl_index += 3
                if c > 1:
                    pxl_index += 1
            # draw depending on scale and offset
            fill_rect(int(x_offset - (res_x / 2 * scale)) + int(x * scale),
                      int(y_offset - (res_y / 2 * scale)) + int(y * scale), int(scale), int(scale),
                      (pxl_color[0], pxl_color[1], pxl_color[2]))