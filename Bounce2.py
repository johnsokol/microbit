from microbit import *
import math
import time

wid = 1.2

xv = 3.7
yv = 4.1
xlim_bounce = 5  # Corresponds to the center of the 0-50 range
ylim_bounce = 5
ctx = xlim_bounce
cty = ylim_bounce
grid_size = 5

while True:
    ctx += xv
    cty += yv

    # Bouncing logic based on the conceptual 0-50 range
    if ctx > (50 - xlim_bounce):
        xv = -xv
    if ctx < xlim_bounce:
        xv = -xv
    if cty > (50 - ylim_bounce):
        yv = -yv
    if cty < ylim_bounce:
        yv = -yv

    # Calculate the center of the Gaussian on the 5x5 grid (0 to 4)
    tx = ctx / 10    # Subtract half of (grid_size - 1) to center
    ty = cty / 10  

    full_image_str = ""
    for y in range(grid_size):
        row_str = ""
        for x in range(grid_size):
            pix = int(math.exp(-pow(x - tx, 2) / wid) * math.exp(-pow(y - ty, 2) / wid) * 9)
            row_str += str(pix)
            if x < grid_size - 1:
                row_str += ""  # No colon within the row
        full_image_str += row_str
        if y < grid_size - 1:
            full_image_str += ":"

    image = Image(full_image_str)
    display.show(image, delay=50, wait=True, loop=False, clear=False)
    time.sleep(0.05)
