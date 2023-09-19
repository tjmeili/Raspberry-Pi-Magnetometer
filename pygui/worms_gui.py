import sys
from PyQt5.QtCore import QMetaObject, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QWidget,
                             QSizePolicy,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLabel,
                             QSpacerItem,
                             QLineEdit,
                             QPushButton)


class WormsMainWindow(QMainWindow):

    time = -1

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Worms")
        self.resize(400, 350)
        self.initUI()
        self.initListeners()

    def initUI(self):
        #Window Layout
        self.centralwidget = QWidget(self)
        self.verticalLayout1 = QVBoxLayout(self.centralwidget)
        self.verticalLayout1.setContentsMargins(25, 5, 25, 5)
        self.verticalLayout1.setSpacing(10)

        self.titleHorizontalLayout = QHBoxLayout()

        self.titleHorizontalLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.titleLabel = QLabel("Worms")
        font = QFont()
        #font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.titleHorizontalLayout.addWidget(self.titleLabel)

        self.titleHorizontalLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.verticalLayout1.addLayout(self.titleHorizontalLayout)
        self.verticalLayout1.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.timeInputHorizontalLayout = QHBoxLayout()

        # Time input box
        self.timeLineEdit = QLineEdit(self.centralwidget)
        # so its not super wide
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.timeLineEdit.sizePolicy().hasHeightForWidth())
        self.timeLineEdit.setSizePolicy(sizePolicy)
        self.timeLineEdit.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(30)
        self.timeLineEdit.setFont(font)
        self.timeInputHorizontalLayout.addWidget(self.timeLineEdit)

        # ms Label
        self.msLabel = QLabel("ms")
        font = QFont()
        #font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.msLabel.setFont(font)
        self.msLabel.setObjectName("msLabel")
        self.timeInputHorizontalLayout.addWidget(self.msLabel)

        self.timeInputHorizontalLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.verticalLayout1.addLayout(self.timeInputHorizontalLayout)

        # Fire button container
        self.fireHorizontalLayout = QHBoxLayout()
        self.fireHorizontalLayout.setContentsMargins(-1, 10, -1, 10)

        # Fire Button
        self.fireButton = QPushButton("Fire")
        self.fireButton.setSizePolicy(sizePolicy)
        self.fireButton.setMinimumSize(QSize(150, 0))
        font = QFont()
        #font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.fireButton.setFont(font)
        self.fireHorizontalLayout.addWidget(self.fireButton)

        self.fireHorizontalLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.verticalLayout1.addLayout(self.fireHorizontalLayout)

        self.verticalLayout1.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label to test ui components
        self.testLabel = QLabel("Test LABEL for numbers and stuff 123")
        font = QFont()
        #font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.testLabel.setFont(font)
        self.verticalLayout1.addWidget(self.testLabel)

        self.setCentralWidget(self.centralwidget)
        self.show()

    def initListeners(self):
        self.fireButton.clicked.connect(lambda: self.fireButtonClicked)

    def fireButtonClicked(self):
        #check to see if time entered is a positive integer
        #display in testLabel (or do stuff with input)
        input = self.timeLineEdit.text()
        if len(input) > 0:
            try:
                timeInput = int(self.timeLineEdit.text())
                self.testLabel.setText(str(timeInput)) if timeInput > 0 else self.testLabel.setText("Negative time???")
                self.time = timeInput
            except ValueError:
                self.testLabel.setText("NOT A NUMBER BRO. GOTTA BE A NUMBER.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = WormsMainWindow()
    sys.exit(app.exec_())
