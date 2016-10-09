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

from Ui_Black import Ui_Form

from pytube import YouTube




class SimpleDialog(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # python3.x
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        

        # self.ui.treeview = DragDropTreeView()
        # self.ui.verticalLayout.addWidget(self.ui.treeview)
        
        # カスタムItem Modelの作成。
        self.model = DragDropItemModel()
        # カスタムTreeviewの作成。-----------------------------------------------------
        self.ui.treeview.setModel(self.model)
        # カラムの幅を指定する。
        self.ui.treeview.setColumnWidth(0, 150)
        self.ui.treeview.setColumnWidth(1, 80)
        self.ui.treeview.setColumnWidth(2, 50)
        # -----------------------------------------------------------------------------
        self.load_setting()

        self.downloader = YtDownloader()
        self.downloader.setDaemon(True)
        self.downloader.start()

        self.model_items = []

        self.ui.lineEdit_url.setText(
            "https://www.youtube.com/watch?v=RvVfgvHucRY")
        self.ui.lineEdit_url.clear()

    @Slot()
    def debuglog(self, s):
        # self.ui.textEdit_debug.append(s)
        pass

    @Slot()
    def on_btn_download(self):
        self.url = self.ui.lineEdit_url.text()
        self.ui.lineEdit_url.clear()

        # QMessageBox.information(self, "Message", self.url)
        # self.debuglog("Download Start => {}".format(self.url))

        item1, item2, item3 = self.model.addObject(QUrl("/"+self.url))

        item1.setText(self.url)
        item2.setText("  0%")
        item3.setText("-")

        self.downloader.download(url=self.url,
                                 out_dir=self.savedir,
                                 progress=item2.setText,
                                 finish=item3.setText)

    @Slot()
    def on_btn_savedir(self):
        savedir = QFileDialog.getExistingDirectory(
            self, caption="保存先の指定", dir=self.savedir, options=QFileDialog.ShowDirsOnly)
        self.set_savedir(savedir)

    def set_savedir(self, savedir):
        self.ui.lineEdit_savedir.setText(savedir)
        self.savedir = savedir

    def load_setting(self):
        setting = QSettings("setting.ini", QSettings.IniFormat)
        self.set_savedir(setting.value("savedir", "./"))

    def closeEvent(self, event):
        setting = QSettings("setting.ini", QSettings.IniFormat)
        setting.setValue("savedir", self.savedir)
        self.downloader.stop()

if __name__ == '__main__':

    import traceback
    try:
        app = QApplication(sys.argv)
        dialog = SimpleDialog()
        dialog.show()
        sys.exit(app.exec_())
    except:
       logger.error(traceback.format_exc())
       raise