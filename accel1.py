from microbit import *
import math

wid = 1.2
grid_size = 5

def calculate_pixel_brightness(x, y, center_x, center_y, width):
    """Calculates the brightness of a pixel based on a Gaussian distribution."""
    exponent = -((x - center_x)**2 + (y - center_y)**2) / (2 * (width/2)**2)
    brightness = int(math.exp(exponent) * 9)
    return max(0, min(9, brightness))  # Clamp brightness to 0-9

while True:
    # Read accelerometer values
    x_accel = accelerometer.get_x()
    y_accel = accelerometer.get_y()

    # Map accelerometer values to the center of the Gaussian
    # Adjust these scaling and offset values as needed to fine-tune the control
    center_x = (x_accel / 1000) * (grid_size - 1) / 2 + (grid_size - 1) / 2
    center_y = (y_accel / 1000) * (grid_size - 1) / 2 + (grid_size - 1) / 2

    full_image_str = ""
    for y in range(grid_size):
        row_str = ""
        for x in range(grid_size):
            pix = calculate_pixel_brightness(x, y, center_x, center_y, wid)
            row_str += str(pix)
            if x < grid_size - 1:
                row_str += ""  # No colon within the row
        full_image_str += row_str
        if y < grid_size - 1:
            full_image_str += ":"

    image = Image(full_image_str)
    display.show(image, delay=20, wait=True, loop=False, clear=False)
