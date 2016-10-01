# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created: Sat Oct  1 21:20:18 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(658, 467)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QtGui.QFormLayout.WrapLongRows)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setObjectName("formLayout")
        self.label_url = QtGui.QLabel(Form)
        self.label_url.setObjectName("label_url")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_url)
        self.lineEdit_url = QtGui.QLineEdit(Form)
        self.lineEdit_url.setMinimumSize(QtCore.QSize(350, 0))
        self.lineEdit_url.setDragEnabled(True)
        self.lineEdit_url.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lineEdit_url)
        self.btn_download = QtGui.QPushButton(Form)
        self.btn_download.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_download.setObjectName("btn_download")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.btn_download)
        self.label_savedir = QtGui.QLabel(Form)
        self.label_savedir.setObjectName("label_savedir")
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.label_savedir)
        self.lineEdit_savedir = QtGui.QLineEdit(Form)
        self.lineEdit_savedir.setMinimumSize(QtCore.QSize(350, 0))
        self.lineEdit_savedir.setObjectName("lineEdit_savedir")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lineEdit_savedir)
        self.btn_opendir = QtGui.QPushButton(Form)
        self.btn_opendir.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_opendir.setCheckable(False)
        self.btn_opendir.setObjectName("btn_opendir")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.btn_opendir)
        self.verticalLayout.addLayout(self.formLayout)
        self.textEdit_debug = QtGui.QTextEdit(Form)
        self.textEdit_debug.setEnabled(False)
        self.textEdit_debug.setObjectName("textEdit_debug")
        self.verticalLayout.addWidget(self.textEdit_debug)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_download, QtCore.SIGNAL("released()"), Form.on_btn_download)
        QtCore.QObject.connect(self.btn_opendir, QtCore.SIGNAL("released()"), Form.on_btn_savedir)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_url.setText(QtGui.QApplication.translate("Form", "YoutubeのURLを入れてください", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_url.setText(QtGui.QApplication.translate("Form", "https://www.youtube.com/watch?time_continue=233&v=spnjTzuVBO0", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_download.setText(QtGui.QApplication.translate("Form", "download", None, QtGui.QApplication.UnicodeUTF8))
        self.label_savedir.setText(QtGui.QApplication.translate("Form", "保存先のフォルダを入力してください", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_savedir.setText(QtGui.QApplication.translate("Form", "デスクトップ", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_opendir.setText(QtGui.QApplication.translate("Form", "参照", None, QtGui.QApplication.UnicodeUTF8))

