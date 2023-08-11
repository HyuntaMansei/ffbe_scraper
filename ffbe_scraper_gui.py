
import pandas as pd
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel, QTextEdit, QComboBox, QLineEdit, QPlainTextEdit, QTextBrowser, QSizePolicy
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QInputDialog
from PyQt5.QtCore import Qt, QObject, QEvent, QCoreApplication
from PyQt5 import QtWidgets, uic
import os
import re
import configparser
import win32gui
import win32process
import psutil
import sys
import threading
import pygetwindow as gw
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        # Declare variables
        self.driver = None

    def init_ui(self):
        # Load the UI file
        uic.loadUi('ffbe_scraper.ui', self)
        # self.db_config = configparser.ConfigParser()
        # self.db_config.read('./ignore/db_config.ini')
        # db_names = [i[0] for i in self.db_config.items()]
        # self.output(f"DB list: {db_names}")
        # self.cb_db_name.clear()
        # self.cb_db_name.addItems([""]+db_names)
        # self.rb_ignore.setChecked(True)
        self.show()
    def test(self):
        print("Tesintng")
    def load_driver(self):
        # Scrape naver cafe for unit and vc
        # for unit
        print("In func, load_driver")
        unit_url = "https://cafe.naver.com/wotvffbe?iframe_url=/ArticleList.nhn%3Fsearch.clubid=30004614%26search.menuid=65%26search.boardtype=I"
        self.driver = webdriver.Chrome()
        self.driver.get(unit_url)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.setWindowTitle("FFBE scraper v0.1")
    sys.exit(app.exec_())
