# RIOTOpenSource
Open source application Rotate Image with Oblique Text. Based on OpenCV and PyQt5.

In the file RotateImg.py you can find the main algorithm. The basic principle of the algorithm it's transform the text in line and rotate the image on angle oblique:

1)Thresholding image. Was choosed <em>Adaptive Gaussian Thresholding</em> 'cause it was better then other methods.
2)Then, was applied some morphological transforms such as <em>closing</em> for filling the holes between and inside letters and <em>opening</em> for removing noise.
3)After that, was applied <em>Hough Transform</em> for finding lines and then detecting angle.
4)The final part, just rotate the image to the detected angle.

This algorithm is flavored with GUI in file MainApp.py. Simple and beautiful app which has 4 buttons: "Open", "Rotate", "Save" and "Exit".

![alt text](https://github.com/vovanezha/RIOTOpenSource/blob/master/gui.png)

