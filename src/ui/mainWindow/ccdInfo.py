from PyQt5 import QtCore
from PyQt5 import QtWidgets

from src.controller.camera import Camera
from src.ui.commons.layout import set_hbox, set_lvbox


class CCDInfo(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(CCDInfo, self).__init__(parent)
        self.cam = Camera()
        self.init_widgets()

    def init_widgets(self):
        """ Function to initiate the Widgets of CCD Information """
        # Camera Firmware
        lf = QtWidgets.QLabel("Firmware:", self)

        # LineEdit to show Firmware version
        tfirm = QtWidgets.QLabel(self)

        # Camera Name
        ln = QtWidgets.QLabel("Camera:", self)

        self.cam.set_firmware_and_model_fields(lf, ln)
        # LineEdit to show camera model
        cn = QtWidgets.QLabel(self)
        cn.setAlignment(QtCore.Qt.AlignCenter)

        # Setting the layout
        self.setLayout(set_lvbox(set_hbox(lf, tfirm),
                                 set_hbox(ln, cn)))
