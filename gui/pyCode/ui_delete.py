# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uiCode/delete.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_remove(object):
    def setupUi(self, remove):
        remove.setObjectName("remove")
        remove.resize(398, 277)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        remove.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(remove)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(remove)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cid = QtWidgets.QLineEdit(remove)
        self.cid.setObjectName("cid")
        self.gridLayout.addWidget(self.cid, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(remove)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(remove)
        self.buttonBox.accepted.connect(remove.accept)
        self.buttonBox.rejected.connect(remove.reject)
        QtCore.QMetaObject.connectSlotsByName(remove)

    def retranslateUi(self, remove):
        _translate = QtCore.QCoreApplication.translate
        remove.setWindowTitle(_translate("remove", "Delete"))
        self.label.setText(_translate("remove", "Enter Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    remove = QtWidgets.QDialog()
    ui = Ui_remove()
    ui.setupUi(remove)
    remove.show()
    sys.exit(app.exec_())

