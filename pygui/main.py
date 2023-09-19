import sys
from PyQt5.QtWidgets import QApplication

from worms_gui import WormsMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = WormsMainWindow()
    sys.exit(app.exec_())

    