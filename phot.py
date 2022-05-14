import os

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout,
                             QFileDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image



app = QApplication([])
win = QWidget()
win.resize(700,400)
win.setWindowTitle('Editor')

lb_image = QLabel('Картинка')
btn_dir = QPushButton('Папка')
file_list = QListWidget()

btn_left = QPushButton('Лево')
btn_right = QPushButton('Право ')
btn_flip = QPushButton('Зеркально')
btn_shar = QPushButton('Резкость')
btn_bw = QPushButton('Ч/Б')

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(file_list)
col2.addWidget(lb_image, 90)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_shar)
row_tools.addWidget(btn_bw)


col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)

win.setLayout(row)
win.show()
workdir = ''

def filter(filenames, extensions):
    result = []
    for filename in filenames:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWordDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenameslist():
    extensions = ['.jpg','.png','.jpeg']
    chooseWordDir()
    filenames = filter(os.listdir(workdir), extensions)
    file_list.clear()
    for filename in filenames:
        file_list.addItem(filename)

btn_dir.clicked.connect(showFilenameslist)


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.dir = None
        self.save_dir = 'Modified/'


    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)



    def showImage(self, path):
        lb_image.hide()
        pixmapImage = QPixmap(path)
        w = lb_image.width()
        h = lb_image.height()
        pixmapImage = pixmapImage.scaled(w,h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapImage)
        lb_image.show()

def showChosenImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

workimage = ImageProcessor()

file_list.currentRowChanged.connect(showChosenImage)

app.exec()