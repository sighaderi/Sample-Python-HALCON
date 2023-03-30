In this Python version of the code, we use the halcon module to initialize the Halcon library by setting the size of the window and opening it using halcon.hv_WindowSize() and halcon.hv_OpenWindow(). We then use a try-except block to catch any exceptions that may occur.
Inside the try block, we read an input image file using halcon.read_image(), threshold the image using halcon.threshold(), and save the result using halcon.write_image().
Finally, we close the Halcon library using halcon.hv_CloseWindow().
