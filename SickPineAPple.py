import os,sys
import addOrEdit,compare,alert_sys
from PySide2 import QtWidgets, QtGui

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self,icon,parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self,icon,parent)
        self.setToolTip(f'Sick PineAPple')
        menu = QtWidgets.QMenu(parent)
        add_known = menu.addAction("This is a trusted network")
        add_known.triggered.connect(lambda:addOrEdit.add_to_known())
        menu.addSeparator()
        compare_known = menu.addAction("Check Current Connection")
        compare_known.triggered.connect(lambda:alert_sys.alert())
        menu.addSeparator()
        check_list = menu.addAction("View Known Information")
        check_list.triggered.connect(lambda:compare.show_known_networks())
        menu.addSeparator()
        check_list = menu.addAction("Close Application")
        check_list.triggered.connect(lambda: self.exit_application())
        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self,reason):
        if reason == self.DoubleClick:
            compare.compare_to_known()
        # if reason == self.Trigger: for single click

    def exit_application(self):
        os.system('cmd /c "taskkill /IM "SickPineAPple.exe" /F"')
        sys.exit()
def main():
    while (True):
        app = QtWidgets.QApplication(sys.argv)
        w = QtWidgets.QWidget()
        tray_icon = SystemTrayIcon(QtGui.QIcon("pineapple_sick.jpg"), w)
        tray_icon.show()
        icon = QtGui.QIcon("pineapple_sick.ico")
        tray_icon.showMessage("Sick PineAPple","Monitoring Connections",icon)
        alert_sys.constant()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()