import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate

import modules.date_search as ds
import modules.add_functions as af
import modules.data_iterator as d_iter
import modules.division_data as dd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 601)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)

        self.path = ""
        self.it = None

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 310, 613, 215))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 40, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.input_descr = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.input_descr.setFont(font)
        self.input_descr.setObjectName("input_descr")
        self.horizontalLayout_2.addWidget(self.input_descr)

        self.date = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date.setFont(font)
        self.date.setDate(QtCore.QDate(2008, 1, 10))
        self.date.setObjectName("date")
        self.horizontalLayout_2.addWidget(self.date)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.btn_get_data = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_get_data.clicked.connect(self.get_data)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_get_data.setFont(font)
        self.btn_get_data.setStyleSheet(
            "background-color: rgb(220, 220, 220);")
        self.btn_get_data.setObjectName("btn_get_data")
        self.horizontalLayout.addWidget(self.btn_get_data)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.info = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.info.setObjectName("info")
        self.verticalLayout.addWidget(self.info)
        self.next_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.next_button.setObjectName("next_button")
        self.next_button.clicked.connect(self.next_element)

        self.verticalLayout.addWidget(self.next_button)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(20, 100, 378, 178))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.div_text_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.div_text_label.setFont(font)
        self.div_text_label.setTextFormat(QtCore.Qt.AutoText)
        self.div_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.div_text_label.setIndent(10)
        self.div_text_label.setObjectName("div_text_label")
        self.verticalLayout_3.addWidget(self.div_text_label)
        self.btn_div_by_data_date = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.btn_div_by_data_date.setObjectName("btn_div_by_data_date")
        self.btn_div_by_data_date.clicked.connect(self.div_by_data_date)
        self.verticalLayout_3.addWidget(self.btn_div_by_data_date)
        self.btn_div_by_week = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.btn_div_by_week.setObjectName("btn_div_by_week")
        self.verticalLayout_3.addWidget(self.btn_div_by_week)
        self.btn_div_by_week.clicked.connect(self.div_by_week)
        self.btn_div_by_year = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.btn_div_by_year.setObjectName("btn_div_by_year")
        self.btn_div_by_year.clicked.connect(self.div_by_year)
        self.verticalLayout_3.addWidget(self.btn_div_by_year)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 281, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.upload_path)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_descr.setText(_translate("MainWindow", "Введите дату:"))
        self.btn_get_data.setText(_translate(
            "MainWindow", "Получить информацию"))
        self.info.setText(_translate("MainWindow", "Температура: -20 °C\n"
                                     "Давление: 765 мм.рт.ст.\n"
                                     "Ветер: В 2 м/c"))
        self.next_button.setText(_translate("MainWindow", " Следующая дата"))
        self.div_text_label.setText(_translate(
            "MainWindow", "Разделение основного датасета"))
        self.btn_div_by_data_date.setText(_translate(
            "MainWindow", " Разделить на файлы с датой и данными "))
        self.btn_div_by_week.setText(_translate(
            "MainWindow", "Разделить файлы по неделям"))
        self.btn_div_by_year.setText(_translate(
            "MainWindow", "Разделить файлы по годам"))
        self.pushButton.setText(_translate(
            "MainWindow", "Загрузить основной датасет"))

    def upload_path(self):
        self.path = QtWidgets.QFileDialog.getOpenFileName()[0]
        if self.path:
            try:
                self.it = d_iter.DataIterator(self.path)
            except:
                self.path = ""
                self.__warning_icon(
                    "Предупреждение", "Возможно, что вы выбрали файл не того формата")

    def get_data(self):
        try:
            if self.path:
                data = ds.search(self.path, self.date.date().toPyDate())
                self.info.setText(
                    f"Температура: {data[0]} °C\nДавление: {data[1]} мм.рт.ст.\nВетер: {data[2]} {data[3]} м/c")
            else:
                self.__warning_icon(
                    "Предупреждение", "Загрузите файл с исходным датасетом")
        except:
            self.info.setText("Информация за этот день отсутствует")

    def next_element(self):
        try:
            self.it.index = ds.find(self.path, self.date.date().toPyDate())
            data = next(self.it)
            self.info.setText(
                f"Температура: {data[1]} °C\nДавление: {data[2]} мм.рт.ст.\nВетер: {data[3]} {data[4]} м/c")
            date = list(map(int, data[0].split("-")))
            self.date.setDate(QDate(*date))
        except StopIteration:
            self.__warning_icon(
                "Предупреждение", "Элементов в датесете больше нет")
        except:
            self.__warning_icon(
                "Предупреждение", "Загрузите файл с исходным датасетом")

    def div_by_data_date(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory()
        if folderpath:
            dd.division_date_and_data(folderpath, self.path)
        else:
            self.__warning_icon(
                "Предупреждение", "Укажите папку, куда сохранить разделенные файлы")

    def div_by_week(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory()
        if folderpath:
            dd.division_by_week(folderpath, self.path)
        else:
            self.__warning_icon(
                "Предупреждение", "Укажите папку, куда сохранить разделенные файлы")

    def div_by_year(self):
        try:
            folderpath = QtWidgets.QFileDialog.getExistingDirectory()
            if folderpath:
                dd.division_by_year(folderpath, self.path)
            else:
                self.__warning_icon(
                    "Предупреждение", "Укажите папку, куда сохранить разделенные файлы")
        except:
            self.__warning_icon(
                "Предупреждение", "Загрузите файл с исходным датасетом")

    def __warning_icon(self, text, info):
        error = QtWidgets.QMessageBox()
        error.setIcon(QMessageBox.Warning)
        error.setWindowTitle(text)
        error.setText(info)
        error.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
