import sys
import os
os.environ["QT_API"] = "pyqt6"
os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"

from qtpy import QtWidgets, QtCore
from qtpy.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QStyle
from qtpy.QtWebEngineWidgets import QWebEngineView
from qtpy.QtCore import Qt, QUrl
from qtpy.QtGui import QPixmap, QGuiApplication

class HackrylicWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setGeometry(0, 0, 1280, 720)
        self.setCentralWidget(self.main_widget)
        
        self.background_widget = QWidget(self.main_widget)
        self.background_widget.setGeometry(0, 0, self.width(), self.height())
        self.background = QLabel(self.background_widget)
        self.screenshot = QPixmap("screenshot.png")
        self.background.setPixmap(self.screenshot)  
        self.background.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add a blur effect to the screenshot used as background for the window
        blur = QtWidgets.QGraphicsBlurEffect()
        blur.setBlurRadius(15.0)
        self.background.setGraphicsEffect(blur)

        # Add a black semi-transparent layer over the background to darken it
        self.color_layer = QWidget(self.main_widget)
        self.color_layer.setStyleSheet("background-color: rgba(0, 0, 0, 200);")
        self.color_layer.setGeometry(self.rect())

        self.previousWindowState = self.windowState()

        # Put your other controls on top as children of `main_widget`. For example:
        # self.browser = QWebEngineView(self.main_widget)
        # self.browser.setGeometry(self.rect())
        # self.browser.page().setBackgroundColor(QtCore.Qt.GlobalColor.transparent)
        # self.browser.setUrl(QUrl("http://localhost:8080"))

    def resizeEvent(self, event):
        # Quick attempt to get the titlebar's height so that we can correctly offset the image. We do not actually
        # use it at the moment because my window manager hides title bars.
        titlebar_height = app.style().pixelMetric(QStyle.PixelMetric.PM_TitleBarHeight)

        self.background_widget.setGeometry(-self.x(), -self.y(), self.width()+self.x(), self.height()+self.y())
        self.color_layer.setGeometry(self.rect()) 
        super().resizeEvent(event)
    
    def moveEvent(self, event):
        titlebar_height = app.style().pixelMetric(QStyle.PixelMetric.PM_TitleBarHeight)
        self.background_widget.setGeometry(-self.x(), -self.y(), self.width()+self.x(), self.height()+self.y())
        super().moveEvent(event)

    def update_background(self):
        take_screenshot()
        self.screenshot = QPixmap("screenshot.png")
        self.background.setPixmap(self.screenshot)  

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.Type.WindowStateChange:
            # HACK: Update background when un-minimizing
            if ((self.previousWindowState & QtCore.Qt.WindowState.WindowMinimized) and
                (not self.windowState() or (self.windowState() & QtCore.Qt.WindowState.WindowMaximized))):
                self.update_background()
                super().changeEvent(event)

            self.previousWindowState = self.windowState()

def take_screenshot():
    screen_geometry = QGuiApplication.primaryScreen().geometry()
    # TODO: Check if this will work with multiple screens, probably not.
    screenshot = QGuiApplication.primaryScreen().grabWindow(0, screen_geometry.left(), screen_geometry.top(), screen_geometry.width(), screen_geometry.height())
    screenshot.save("screenshot.png")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    take_screenshot() # Take initial screenshot before showing the main window
    window = HackrylicWindow()
    window.show()
    sys.exit(app.exec())