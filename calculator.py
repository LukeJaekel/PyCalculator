from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(237, 334)
        Calculator.setMaximumSize(QtCore.QSize(237, 334))
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy)
        self.button3.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 4, 2, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        self.button2.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 4, 1, 1, 1)
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 4, 0, 1, 1)
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy)
        self.button7.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.button7.setObjectName("button7")
        self.gridLayout.addWidget(self.button7, 2, 0, 1, 1)
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy)
        self.button5.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.button5.setObjectName("button5")
        self.gridLayout.addWidget(self.button5, 3, 1, 1, 1)
        self.buttonPercent = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonPercent.sizePolicy().hasHeightForWidth())
        self.buttonPercent.setSizePolicy(sizePolicy)
        self.buttonPercent.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.buttonPercent.setObjectName("buttonPercent")
        self.gridLayout.addWidget(self.buttonPercent, 1, 2, 1, 1)
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy)
        self.button9.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.button9.setObjectName("button9")
        self.gridLayout.addWidget(self.button9, 2, 2, 1, 1)
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy)
        self.button4.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.button4.setObjectName("button4")
        self.gridLayout.addWidget(self.button4, 3, 0, 1, 1)
        self.buttonDivide = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDivide.sizePolicy().hasHeightForWidth())
        self.buttonDivide.setSizePolicy(sizePolicy)
        self.buttonDivide.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.buttonDivide.setObjectName("buttonDivide")
        self.gridLayout.addWidget(self.buttonDivide, 4, 3, 1, 1)
        self.buttonSubtract = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSubtract.sizePolicy().hasHeightForWidth())
        self.buttonSubtract.setSizePolicy(sizePolicy)
        self.buttonSubtract.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.buttonSubtract.setObjectName("buttonSubtract")
        self.gridLayout.addWidget(self.buttonSubtract, 2, 3, 1, 1)
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy)
        self.button8.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.button8.setObjectName("button8")
        self.gridLayout.addWidget(self.button8, 2, 1, 1, 1)
        self.buttonPlusMinus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonPlusMinus.sizePolicy().hasHeightForWidth())
        self.buttonPlusMinus.setSizePolicy(sizePolicy)
        self.buttonPlusMinus.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.buttonPlusMinus.setObjectName("buttonPlusMinus")
        self.gridLayout.addWidget(self.buttonPlusMinus, 1, 1, 1, 1)
        self.buttonC = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonC.sizePolicy().hasHeightForWidth())
        self.buttonC.setSizePolicy(sizePolicy)
        self.buttonC.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.buttonC.setObjectName("buttonC")
        self.gridLayout.addWidget(self.buttonC, 1, 0, 1, 1)
        self.buttonMultiply = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonMultiply.sizePolicy().hasHeightForWidth())
        self.buttonMultiply.setSizePolicy(sizePolicy)
        self.buttonMultiply.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.buttonMultiply.setObjectName("buttonMultiply")
        self.gridLayout.addWidget(self.buttonMultiply, 3, 3, 1, 1)
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy)
        self.button6.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.button6.setObjectName("button6")
        self.gridLayout.addWidget(self.button6, 3, 2, 1, 1)
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAdd.sizePolicy().hasHeightForWidth())
        self.buttonAdd.setSizePolicy(sizePolicy)
        self.buttonAdd.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.buttonAdd.setObjectName("buttonAdd")
        self.gridLayout.addWidget(self.buttonAdd, 1, 3, 1, 1)
        self.button0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy)
        self.button0.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.button0.setObjectName("button0")
        self.gridLayout.addWidget(self.button0, 5, 0, 1, 2)
        self.buttonDecimal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDecimal.sizePolicy().hasHeightForWidth())
        self.buttonDecimal.setSizePolicy(sizePolicy)
        self.buttonDecimal.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.buttonDecimal.setObjectName("buttonDecimal")
        self.gridLayout.addWidget(self.buttonDecimal, 5, 2, 1, 1)
        self.buttonEquals = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonEquals.sizePolicy().hasHeightForWidth())
        self.buttonEquals.setSizePolicy(sizePolicy)
        self.buttonEquals.setStyleSheet("QPushButton {\n"
"background-color: #3B185F;\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(122, 51, 243);\n"
"border: 1px solid grey;\n"
"padding: 5px;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.buttonEquals.setObjectName("buttonEquals")
        self.gridLayout.addWidget(self.buttonEquals, 5, 3, 1, 1)
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.display.setFont(font)
        self.display.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.display.setStyleSheet("QLineEdit {\n"
"background-color: rgb(104, 104, 104);\n"
"border: 1px solid gray;\n"
"color: #ffffff;\n"
"padding: 5px;\n"
"}")
        self.display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display.setObjectName("display")
        self.gridLayout.addWidget(self.display, 0, 0, 1, 4)
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 237, 24))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)
        
        self.button1.clicked.connect(self.num1)
        self.button2.clicked.connect(self.num2)
        self.button3.clicked.connect(self.num3)
        self.button4.clicked.connect(self.num4)
        self.button5.clicked.connect(self.num5)
        self.button6.clicked.connect(self.num6)
        self.button7.clicked.connect(self.num7)
        self.button8.clicked.connect(self.num8)
        self.button9.clicked.connect(self.num9)
        self.button0.clicked.connect(self.num0)
        self.buttonEquals.clicked.connect(self.equals)
        self.buttonAdd.clicked.connect(self.add)
        self.buttonSubtract.clicked.connect(self.subtract)
        self.buttonMultiply.clicked.connect(self.multiply)
        self.buttonDivide.clicked.connect(self.divide)
        self.buttonDecimal.clicked.connect(self.decimal)
        self.buttonPlusMinus.clicked.connect(self.plusMinus)
        self.buttonPercent.clicked.connect(self.percentage)

        self.buttonC.clicked.connect(self.clear)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)


    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        translate = QtCore.QCoreApplication.translate
        self.button1.setText(translate("Calculator", "1"))
        self.button2.setText(translate("Calculator", "2"))
        self.button3.setText(translate("Calculator", "3"))
        self.button4.setText(translate("Calculator", "4"))
        self.button5.setText(translate("Calculator", "5"))
        self.button6.setText(translate("Calculator", "6"))
        self.button7.setText(translate("Calculator", "7"))
        self.button8.setText(translate("Calculator", "8"))
        self.button9.setText(translate("Calculator", "9"))
        self.button0.setText(translate("Calculator", "0"))
        self.buttonDecimal.setText(translate("Calculator", "."))
        self.buttonEquals.setText(translate("Calculator", "="))
        self.buttonAdd.setText(translate("Calculator", "+"))
        self.buttonSubtract.setText(translate("Calculator", "-"))
        self.buttonMultiply.setText(translate("Calculator", "*"))
        self.buttonDivide.setText(translate("Calculator", "/"))
        self.buttonPercent.setText(translate("Calculator", "%"))
        self.buttonC.setText(translate("Calculator", "C"))
        self.buttonPlusMinus.setText(translate("Calculator", "+/-"))
        self.display.setText(translate("Calculator", ""))

    def decimal(self):
        number = self.display.text()
        temp = number.split()
        
        if "+" in number:
            temp = number.split("+")
        elif "-" in number:
            temp = number.split("-")
        elif "*" in number:
            temp = number.split("*")
        elif "/" in number:
            temp = number.split("/")
        
        if "." in temp[-1]:
            pass
        else:
            self.display.setText(f'{number}.')

    def num1(self):

        number = self.display.text()
        self.display.setText(number + "1")

    def num2(self):
        number = self.display.text()
        self.display.setText(number + "2")

    def num3(self):
        number = self.display.text()
        self.display.setText(number + "3")

    def num4(self):
        number = self.display.text()
        self.display.setText(number + "4")

    def num5(self):
        number = self.display.text()
        self.display.setText(number + "5")

    def num6(self):
        number = self.display.text()
        self.display.setText(number + "6")

    def num7(self):
        number = self.display.text()
        self.display.setText(number + "7")

    def num8(self):
        number = self.display.text()
        self.display.setText(number + "8")

    def num9(self):
        number = self.display.text()
        self.display.setText(number + "9")

    def num0(self):
        number = self.display.text()
        self.display.setText(number + "0")

    def equals(self):

        number = self.display.text()

        try:

            number = eval(number)
            number = str(number)
            self.display.setText(number)

        except Exception as e:
            self.display.setText("Error")

    def add(self):

        number = self.display.text()
        self.display.setText(number + "+")

    def subtract(self):
        number = self.display.text()
        self.display.setText(number + "-")

    def multiply(self):
        number = self.display.text()
        self.display.setText(number + "*")

    def divide(self):
        number = self.display.text()
        self.display.setText(number + "/")
        
    def plusMinus(self):
        number = self.display.text()
        
        if "-" in number:
            self.display.setText(number.replace("-", ""))
        else:
            self.display.setText(f'-{number}')
            
    def percentage(self):
        try:
            number = int(self.display.text())
            number /= 100
            self.display.setText(str(number))
        except:
            self.display.setText("Error")

    def back(self):

        number = self.display.text()
        number = number[1:]
        self.display.setText(number)

    def clear(self):
        self.display.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
