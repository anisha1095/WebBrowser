import sys,private_window,final
from PyQt4 import QtCore, QtGui, QtWebKit

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    main = final.Browser()
    main.show()
    sys.exit(app.exec_())