import os
import numpy as np
import halcon

# Initialize the Halcon library
halcon.hv_WindowSize(0, 0, 640, 480)
halcon.hv_OpenWindow(0, 0, 640, 480, 'visible')

try:
    # Read the input image
    image = halcon.read_image('input_image.png')

    # Threshold the image
    thresholded = halcon.threshold(image, 128, 255)

    # Save the result
    halcon.write_image(thresholded, 'output_image.png')

except halcon.HalconException as e:
    print(f'An exception occurred: {e}')
    os._exit(1)

finally:
    # Close the Halcon library
    halcon.hv_CloseWindow()

