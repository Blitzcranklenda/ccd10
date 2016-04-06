from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
                             QHBoxLayout)

from src.ui.commons.layout import add_all_to_vbox, set_wvbox
from src.ui.mainWindow.cameraInfo import CameraInfo
from src.ui.mainWindow.clock import Clock
from src.ui.mainWindow.shooter import Shooter
from src.ui.mainWindow.configsInfo import ConfigsInfo
from src.business.consoleThreadOutput import ConsoleThreadOutput


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Init the Layouts
        self.MainHBox = QHBoxLayout()   # Main Box
        self.VBox = QVBoxLayout()   # Vertical Box in the Left Box
        self.all_h_boxes = []
        self.console = ConsoleThreadOutput()

        self.MainHBox.addLayout(self.VBox)
        self.MainHBox.addStretch(1)
        self.MainHBox.addLayout(set_wvbox(self.console.get_widget_console(), Shooter(self)))

        add_all_to_vbox(self.VBox, Clock(self), ConfigsInfo(self), CameraInfo(self))
        self.VBox.addStretch(1)

        self.setLayout(self.MainHBox)
