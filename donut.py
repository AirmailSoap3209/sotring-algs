import math
import time
import os

A = 0  # rotation angle around the X axis
B = 0  # rotation angle around the Y axis

# screen size
width, height = 40, 22

# characters for shading
chars = ".,-~:;=!*#$@"

while True:
    # clear screen
    os.system("cls" if os.name == "nt" else "clear")
    
    z = [0] * 1760  # z-buffer
    b = [' '] * 1760  # output buffer

    # loop over donut circle
    for j in range(0, 628, 7):  # j rotation step
        for i in range(0, 628, 2):  # i rotation step
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e

            # calculate x, y, and z
            x = int(width / 2 + 30 * D * (l * h * m - t * n))
            y = int(height / 2 + 15 * D * (l * h * n + t * m))
            o = int(x + width * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

            if 0 <= y < height and 0 <= x < width and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    # print frame
    print("\033[H", end='')
    for k in range(len(b)):
        print(b[k], end='' if (k + 1) % width else '\n')

    # update angles for rotation
    A += 0.04
    B += 0.02
    time.sleep(0.03)
