# Import necessary modules from PyQt5.
from PyQt5 import QtCore, QtGui, QtWidgets
from .gui_utils import GuiUtils
import sys


# Main UI class definition.
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Create an instance of GuiUtils
        self.guiUtils = GuiUtils()
        # Call the setupUi method of GuiUtils to set up the UI elements
        self.guiUtils.setupUi(MainWindow)
        # Call the retranslateUi method to set up translations
        self.retranslateUi(MainWindow)
        # Call the mainActivity method to set up main functionality
        self.mainActivity(MainWindow)

    def retranslateUi(self, MainWindow):
        # Call the retranslateUi method of GuiUtils to set up translations
        self.guiUtils.retranslateUi(MainWindow)

    def mainActivity(self, MainWindow):
        # Call the handleBuyButton method to connect the buy button to its handler function
        self.handleBuyButton()
        # Call the handleCancelButton method to connect the cancel button to its handler function
        self.handleCancelButton()

    def handleBuyButton(self):
        # Connect the clicked signal of the buy button to the handleBuyBtn method of GuiUtils
        self.guiUtils.buttonBuy.clicked.connect(self.guiUtils.handleBuyBtn)

    def handleCancelButton(self):
        # Connect the clicked signal of the cancel button to the handleCancelBtn method of GuiUtils
        self.guiUtils.buttonCancel.clicked.connect(
            self.guiUtils.handleCancelBtn)


def runUI():
    # Create a QApplication instance
    app = QtWidgets.QApplication(sys.argv)
    # Create a QMainWindow instance
    MainWindow = QtWidgets.QMainWindow()
    # Create an instance of Ui_MainWindow
    ui = Ui_MainWindow()
    # Call the setupUi method of Ui_MainWindow to set up the UI
    ui.setupUi(MainWindow)
    # Show the main window
    MainWindow.show()
    # Start the application event loop and exit when the loop is terminated
    sys.exit(app.exec_())
