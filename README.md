# RIOTOpenSource
Open source application Rotate Image with Oblique Text. Based on OpenCV and PyQt5.

In the file RotateImg.py you can find the main algorithm. It was made through:
1) Thresholding image. Was choosed adaptive Gaussian Thresholding 'cause it was better then other methods.
2) Then, was applied some morphological transforms such as <b>closing</b> for filling the holes between and inside letters and <b>opening</b> for removing noise.
