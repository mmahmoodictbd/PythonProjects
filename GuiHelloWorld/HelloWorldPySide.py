#
#  PySide Hello World App
#

import sys

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QLabel
from PySide.QtCore import *
from PySide.QtGui import *

# Create a Qt application
app = QApplication(sys.argv)

# Create a Label and show it
label = QLabel("<font color=red size=40>Hello World</font>")
label.show()

# Enter Qt application main loop
app.exec_()
sys.exit()