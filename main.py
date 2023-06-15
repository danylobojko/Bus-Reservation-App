# Import necessary modules from PyQt5.
from PyQt5 import QtCore, QtGui, QtWidgets
# Import the sys module which provides access to some variables used or maintained by the interpreter.
import sys
# Import the runUI function from the gui module located in the packages directory.
from packages.gui import runUI
# Import the DLLService class from the dll_service module located in the packages directory.
from packages.dll_service import DLLService

# Check if this script is being run as the main program.
if __name__ == '__main__':
    # If so, call the runUI function to launch the GUI.
    runUI()
