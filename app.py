#! coding:utf-8

import sys
import os
import unittest

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtTest import QTest

from applogger import logger
print = logger.debug

from dragdroptreeview import DragDropTreeView, DragDropItemModel
from youtubeloader import YtDownloader

from UI import Ui_Form


class SimpleDialog(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # python3.x
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.treeview = DragDropTreeView()
        self.ui.verticalLayout.addWidget(self.ui.treeview)
        # カスタムItem Modelの作成。
        self.model = DragDropItemModel()
        # カスタムTreeviewの作成。-----------------------------------------------------
        self.ui.treeview.setModel(self.model)
        # カラムの幅を指定する。
        self.ui.treeview.setColumnWidth(0, 400)
        self.ui.treeview.setColumnWidth(1, 140)
        self.ui.treeview.setColumnWidth(2, 100)
        # -----------------------------------------------------------------------------
        self.load_setting()

        self.downloader = YtDownloader()
        self.downloader.setDaemon(False)
        self.downloader.start()

        global print
        print = self.debuglog

    @Slot()
    def debuglog(self, s):
        self.ui.textEdit_debug.append(s)

    @Slot()
    def on_btn_download(self):
        self.url = self.ui.lineEdit_url.text()
        self.ui.lineEdit_url.setText("")
        # QMessageBox.information(self, "Message", self.url)
        self.debuglog("Download Start => {}".format(self.url))
        self.downloader.download(self.url, self.savedir)

    @Slot()
    def on_btn_savedir(self):
        savedir = QFileDialog.getExistingDirectory(
            self, caption="保存先の指定", dir="./", options=QFileDialog.ShowDirsOnly)
        self.set_savedir(savedir)
        self.reload_treeview()

    def set_savedir(self, savedir):
        self.ui.lineEdit_savedir.setText(savedir)
        self.savedir=savedir
        self.reload_treeview()

    @Slot()
    def reload_treeview(self):
        # TODO:erro check
        while self.model.removeRows(0,1):
            pass
        if not os.path.exists(self.savedir):
            return
        files = os.listdir(self.savedir)
        for url in files:
            path = os.path.join(self.savedir, url)
            if os.path.isfile(path):
                self.model.addObject(QUrl("/"+url))

    def load_setting(self):
        setting = QSettings("setting.ini", QSettings.IniFormat)
        self.set_savedir(setting.value("savedir",""))
 
    def closeEvent(self, event):
        setting = QSettings("setting.ini", QSettings.IniFormat)
        setting.setValue("savedir", self.savedir)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SimpleDialog()
    dialog.show()
    sys.exit(app.exec_())
