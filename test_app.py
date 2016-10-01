#! coding:utf-8

import sys
import unittest

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtTest import QTest

from app import SimpleDialog
from applogger import logger
print = logger.debug

app = QApplication(sys.argv)

class TestApp(unittest.TestCase):

    def setUp(self):
        self.widget = SimpleDialog()
        self.ui = self.widget.ui

    def text_edittext_url(self):
        edtext = self.ui.lineEdit_url
        test_url = "http://youtube.com"

        edtext.clear()
        QTest.keyClicks(edtext, test_url)
        self.assertEqual(edtext.text(), test_url)

    def test_btn_download(self):
        # テキストエディットにURLをセット
        edtext = self.ui.lineEdit_url
        test_url = "http://youtube.com"

        edtext.setText(test_url)

        # ボタン押下
        btn = self.ui.btn_download

        QTest.mouseClick(btn, Qt.LeftButton)
        # スロットが呼ばれる
        self.assertEqual(self.widget.url, edtext.text())

if __name__ == '__main__':
    unittest.main()
