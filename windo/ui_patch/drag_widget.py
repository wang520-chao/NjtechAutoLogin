from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from matplotlib.pyplot import close

class DragWidget(QWidget):
    """ 左键拖拽窗口 """
    def __init__(self):
        super().__init__()
        self.dragWidget()
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowOpacity(0.98)
        self.initCustomUI()

    def dragWidget(self):
        self.setMouseTracking(True)
        self.move_flag = False #拖拽窗口

    def initCustomUI(self):
        """添加窗口操作按钮"""
        
        self.setWindowFlags(Qt.FramelessWindowHint)

    def mousePressEvent(self, a0):
        if a0.button() == Qt.LeftButton:
            self.move_flag = True
            self.mos_x = a0.globalX()
            self.mos_y = a0.globalY()
            self.wdo_x = self.x()
            self.wdo_y = self.y()
    
    def mouseMoveEvent(self, a0):
        if self.move_flag:
            move_x = a0.globalX() - self.mos_x
            move_y = a0.globalY() - self.mos_y
            new_x = self.wdo_x + move_x
            new_y = self.wdo_y + move_y
            self.move(new_x, new_y)
    
    def mouseReleaseEvent(self, a0):
        self.move_flag = False



if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    wdo = DragWidget()

    wdo.show()

    sys.exit(app.exec_())