from PyQt5 import QtWidgets

from src.ui.commons.layout import set_lvbox, set_hbox
from src.ui.systemSettingsWindow.widgetsPath import WidgetsPath
from src.business.configuration.configSystem import ConfigSystem
from src.business.consoleThreadOutput import ConsoleThreadOutput


class SystemSettingsWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SystemSettingsWindow, self).__init__(parent)
        self.s = parent
        self.cs = ConfigSystem()
        self.console = ConsoleThreadOutput()

        # Creating Widgets
        self.wp = WidgetsPath(self)
        self.button_ok = QtWidgets.QPushButton('Salvar', self)
        self.button_cancel = QtWidgets.QPushButton('Cancelar', self)

        # Setting Up
        self.button_settings()
        self.setting_up()

        self.filling_fields()

    def button_settings(self):
        self.button_cancel.clicked.connect(self.s.close)
        self.button_ok.clicked.connect(self.ok_button)

    def ok_button(self):
        try:
            self.saving_settings()
            self.console.raise_text("Configurações Salvas com sucesso!", 1)
        except:
            self.console.raise_text("Não foi possível salvar as configurações do sistema.", 1)
        finally:
            self.s.close()

    def setting_up(self):
        self.setLayout(set_lvbox(set_hbox(self.wp),
                                 set_hbox(self.button_ok, self.button_cancel, stretch2=1)))

    def saving_settings(self):
        info = self.wp.get_values()
        self.cs.set_site_settings(info[0], info[1], info[2], info[3], info[4])
        self.cs.save_settings()

    def filling_fields(self):
        info = self.cs.get_site_settings()
        self.wp.set_values(info[0], info[1], info[2], info[3], info[4])
