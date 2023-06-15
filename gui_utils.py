# Import necessary modules from PyQt5.
from PyQt5 import QtCore, QtGui, QtWidgets
from .dll_service import DLLService


# Class for handling GUI.
class GuiUtils:
    def __init__(self):
        # Create an instance of DLLService
        self.dllService = DLLService()

    # Handler for the buy button.
    def handleBuyBtn(self):
        try:
            # Get input from the user
            bus = int(self.inputBusBuy.text())
            seat = int(self.inputSeatBuy.text())

            # Buy ticket using the DLLService
            result = self.dllService.buyTicket(bus, seat)

            # Update the ticket labels
            self.handleTicketsList()

            # Show the result in the notifications label
            self.notificationsLabel.setText(result)

            # Clear the input fields
            self.inputBusBuy.setText('')
            self.inputSeatBuy.setText('')
        except Exception as e:
            self.notificationsLabel.setText('Error occurred')
            print(e)

    # Handler for the cancel button.
    def handleCancelBtn(self):
        try:
            # Get input from the user
            bus = int(self.inputBusCancel.text())
            seat = int(self.inputSeatCancel.text())

            # Cancel ticket using the DLLService
            result = self.dllService.cancelTicket(bus, seat)

            # Update the ticket labels
            self.handleTicketsList()

            # Show the result in the notifications label
            self.notificationsLabel.setText(result)

            # Clear the input fields
            self.inputBusCancel.setText('')
            self.inputSeatCancel.setText('')
        except Exception as e:
            self.notificationsLabel.setText('Error occurred')
            print(e)

    # Function to render the tickets list.
    def handleTicketsList(self):
        try:
            # Remove all existing ticket labels
            self.removeAllLabels()

            # Get all tickets from the DLLService
            result = self.dllService.getAllTickets()

            # Create a label for each ticket
            for ticket in result:
                bus = ticket['bus']
                seat = ticket['seat']
                text = f'Bus: {bus}, Seat: {seat}'
                self.createTicketLabel(text)

        except Exception as e:
            self.notificationsLabel.setText('Error occurred')
            print(e)

    # Function for removing all ticket labels from the layout.
    def removeAllLabels(self):
        # Remove all existing ticket labels from the layout
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.removeWidget(
                self.verticalLayout_3.itemAt(i).widget())

    # Function for creating a ticket label.
    def createTicketLabel(self, text):
        # Create a QLabel for displaying a ticket and add it to the layout
        label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        label.setMinimumSize(QtCore.QSize(0, 30))
        label.setMaximumSize(QtCore.QSize(16777215, 30))
        label.setBaseSize(QtCore.QSize(0, 30))
        label.setStyleSheet("height: 30px;")
        label.setAlignment(QtCore.Qt.AlignLeading |
                           QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        label.setObjectName("labelBusInfo")
        label.setText(text)
        self.verticalLayout_3.addWidget(label)

    # UI, provided by Qt Designer (/ui/ui.ui - Qt Designer or /ui/ui.py - compiled to python code).

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 637)
        MainWindow.setStyleSheet("background: #fafafa;\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
                                         "    border-radius: 5px;\n"
                                         "    padding: 5px;\n"
                                         "    color: #111;\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit {\n"
                                         "    border: 1px solid #ccc;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton {\n"
                                         "    background: #2980b9;\n"
                                         "    color: #fff;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background: #3498db;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 60, 160, 140))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inputBusBuy = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inputBusBuy.setStyleSheet("")
        self.inputBusBuy.setObjectName("inputBusBuy")
        self.verticalLayout.addWidget(self.inputBusBuy)
        self.inputSeatBuy = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inputSeatBuy.setStyleSheet("")
        self.inputSeatBuy.setObjectName("inputSeatBuy")
        self.verticalLayout.addWidget(self.inputSeatBuy)
        self.buttonBuy = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonBuy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBuy.setStyleSheet("")
        self.buttonBuy.setObjectName("buttonBuy")
        self.verticalLayout.addWidget(self.buttonBuy)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(260, 60, 160, 140))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.inputBusCancel = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.inputBusCancel.setStyleSheet("")
        self.inputBusCancel.setObjectName("inputBusCancel")
        self.verticalLayout_2.addWidget(self.inputBusCancel)
        self.inputSeatCancel = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.inputSeatCancel.setStyleSheet("")
        self.inputSeatCancel.setObjectName("inputSeatCancel")
        self.verticalLayout_2.addWidget(self.inputSeatCancel)
        self.buttonCancel = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.buttonCancel.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonCancel.setStyleSheet("")
        self.buttonCancel.setObjectName("buttonCancel")
        self.verticalLayout_2.addWidget(self.buttonCancel)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(40, 250, 381, 370))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 370))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 371, 360))
        self.scrollAreaWidgetContents.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 220, 91, 31))
        self.label_3.setObjectName("label_3")
        self.notificationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.notificationsLabel.setGeometry(QtCore.QRect(40, 10, 381, 41))
        self.notificationsLabel.setText("")
        self.notificationsLabel.setObjectName("notificationsLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set fixed size for MainWindow.
        MainWindow.setFixedSize(MainWindow.size())

        # Stick elements to top.
        self.verticalLayout_3.setAlignment(QtCore.Qt.AlignTop)

        # Render tickets list.
        self.handleTicketsList()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Book ticket"))
        self.inputBusBuy.setPlaceholderText(_translate("MainWindow", "Bus"))
        self.inputSeatBuy.setPlaceholderText(_translate("MainWindow", "Seat"))
        self.buttonBuy.setText(_translate("MainWindow", "Book"))
        self.label_2.setText(_translate("MainWindow", "Cancel ticket"))
        self.inputBusCancel.setPlaceholderText(_translate("MainWindow", "Bus"))
        self.inputSeatCancel.setPlaceholderText(
            _translate("MainWindow", "Seat"))
        self.buttonCancel.setText(_translate("MainWindow", "Cancel"))
        self.label_3.setText(_translate("MainWindow", "Your tickets:"))
