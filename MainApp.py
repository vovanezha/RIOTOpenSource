from PIL import Image

import cv2
import numpy as np
import sys

from PyQt5.QtCore import QFileInfo, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QAction, QFileDialog,
                             QLabel, QMessageBox, QDesktopWidget)


def image_rotation(img_path):
    img = cv2.imread(img_path)
    img_copy = img.copy()
    img_copy = cv2.medianBlur(img, 5)

    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh = cv2.bitwise_not(thresh)

    kernel = np.ones((2, 2), np.uint8)

    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    average_theta = 0
    t = 0
    # Calculate lines
    lines = cv2.HoughLines(opening, 1, np.pi / 180, 275)

    for i in range(0, len(lines)):
        for rho, theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * a)
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * a)
            cv2.line(img_copy, (x1, y1), (x2, y2), (0, 255, 0), 1)
            average_theta += theta
            t += 1

    # Search the angle
    angle = ((average_theta / t) - (np.pi / 180 * 90)) * 180 / np.pi
    h, w = img.shape[:2]

    # Rotated the image
    M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    cv2.imshow('rotated', rotated)
    return rotated


class Main(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.form = QWidget(self)
        self.lbl = QLabel(self)

        self.icon = QIcon('/home/nezha/Изображения/rotate.png')

        exitAction = QAction(QIcon('/home/nezha/Изображения/exit.png'), 'Exit', self)
        exitAction.setStatusTip('Exit')
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.closeEvent)

        openAction = QAction(QIcon('/home/nezha/Изображения/open.png'), 'Open', self)
        openAction.setStatusTip('Open image')
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.file_dialog)

        self.rotateAction = QAction(QIcon('/home/nezha/Изображения/rotate.png'), 'Rotate', self)
        self.rotateAction.setStatusTip('Rotate the image')
        self.rotateAction.setShortcut('Ctrl+R')

        self.saveAction = QAction(QIcon('/home/nezha/Изображения/save.jpeg'), 'Save', self)
        self.saveAction.setStatusTip('Save the image')
        self.saveAction.setShortcut('Ctrl+S')

        self.statusBar()

        self.toolbar = self.addToolBar('Menu')
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(self.rotateAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addAction(exitAction)

        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(50, 50))
        self.setGeometry(300, 500, 500, 50)
        self.center()
        self.setWindowIcon(self.icon)
        self.show()

    def file_dialog(self):

        self.fpath = QFileDialog.getOpenFileName(self, 'Image file (*.jpg, *.png, *.jpeg)', '/home')[0]

        pixmap = QPixmap(self.fpath)

        self.lbl.setGeometry(0, 60, pixmap.width(), pixmap.height())
        self.lbl.setPixmap(pixmap)

        self.rotateAction.triggered.connect(lambda: image_rotation(self.fpath))
        self.saveAction.triggered.connect(lambda: self.save_img(image_rotation(self.fpath)))

        self.resize(pixmap.width() + 50, pixmap.height() + 100)

    def save_img(self, img_rotated):
        new_img = Image.fromarray(img_rotated)

        fname = QFileInfo(self.fpath).fileName()

        new_img.save(fname)

    def closeEvent(self, QCloseEvent):
        qst = QMessageBox.question(self, 'Message',
                                   'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if qst == QMessageBox.Yes:
            exit()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
