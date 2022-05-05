import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)   #her programda olması gerekir

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 1")

    pencere.show()

    sys.exit(app.exec_())    #her programda olması gerekir


Pencere()


