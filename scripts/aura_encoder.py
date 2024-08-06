#•❪❆ by SHARKstudio ❆❫•#

#◥▛▀▀▀▀▀▜ * ▛▀▀▀▀▀▜◤#
#     AURA ENGINE    #
#◢▙▄▄▄▄▄▟ * ▙▄▄▄▄▄▟◣#


#━━━━━━❪❆❫━━━━━━#


# ◣◤  •IMPORTING MODULES•  ◥◢
from tkinter import filedialog
from PIL import Image


# ◣◤  •OPENING TKINTER F-E•  ◥◢
def file_explorer():
    file_path = filedialog.askopenfilename(title="SELECT AN IMAGE TO CONVERT",
                                           filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    return file_path


# ◣◤  •GET IMG PATH & OPEN WITH PILLOW•  ◥◢
image_path = file_explorer()
if image_path:
    input_image = Image.open(image_path)

    # Get image resolution
    width = input_image.width
    height = input_image.height

    # If resolution to high to fit in Numworks memory, throw error
    if width * height > 4300:
        print("[ERROR:X0X0] your image is to big (exceeds 4300px).")
    else:
        # Create or get txt file
        output_file = open("colors.txt", "w")
        # Write resolution of image on first two lines (using 3 chars conventions)
        output_file.write(f"{width:03d}\n{height:03d}\n")

        # Get all pixels of images as tuples
        for y in range(input_image.height):
            for x in range(input_image.width):
                pixel_color = input_image.getpixel((x, y))

                # Separate tuple into three variables
                r = pixel_color[0]
                g = pixel_color[1]
                b = pixel_color[2]

                # Write color in new line using RRRGGGBBB format (on 0 to 255 range)
                color_string = f"{r:03d}{g:03d}{b:03d}\n"
                output_file.write(color_string)

        # Close files
        output_file.close()
        input_image.close()

        # Throw success message
        print("[OUTPUT:X0X0] successfully converted !")
