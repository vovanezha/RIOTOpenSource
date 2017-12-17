# RIOTOpenSource
Open source application Rotate Image with Oblique Text. Based on OpenCV and PyQt5.

In the file RotateImg.py you can find the main algorithm. The basic principle of the algorithm it's transform the text in line and rotate the image on angle oblique:

1) Thresholding image. Was choosed <em>Adaptive Gaussian Thresholding</em> 'cause it was better then other methods.
2) Then, was applied some morphological transforms such as <em>closing</em> for filling the holes between and inside letters and <em>opening</em> for removing noise.
3) After that, was applied <em>Hough Transform</em> for finding lines and then detecting angle.
4) The final part, just rotate the image to the detected angle.

<img src="https://github.com/vovanezha/RIOTOpenSource/blob/master/images/test2.png" width="400" height="200" /><img src="https://github.com/vovanezha/RIOTOpenSource/blob/master/images/rot_test2.png" width="400" height="200" />

<img src="https://github.com/vovanezha/RIOTOpenSource/blob/master/images/test3.png" width="400" height="600" /><img src="https://github.com/vovanezha/RIOTOpenSource/blob/master/images/rot_test1.png" width="400" height="600" />
This algorithm is flavored with GUI in file MainApp.py. Simple and beautiful app which has 4 buttons: "Open", "Rotate", "Save" and "Exit".

![image](https://github.com/vovanezha/RIOTOpenSource/blob/master/gui.png)
But app has problem. The image will save in the directory, where is app, and you can't choose the directory. Sorry for that.

In the file PrimitiveRotateImg.py you find primitive algorithm :D. It's based on just threshold image, detect contours, draw rectangle, calculating angle and then rotate.

