import sys
from datetime import datetime

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton


# QWidget create windows, is  a class
# child class
# widgets are applied to grid


import sys
from datetime import datetime

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Age Calculator")

        grid = QGridLayout()

        # Create Widgets
        name_label = QLabel("Name")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Date of Birth (MM/DD/YYYY)")
        self.date_birth_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # grid.addWidget(Widget, row, column)
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        # setLayout is a method of QWidget
        self.setLayout(grid)

    def calculate_age(self):
        name = self.name_line_edit.text()
        date_of_birth = self.date_birth_line_edit.text()

        if not name or not date_of_birth:
            self.output_label.setText("Please enter both name and date of birth.")
            return

        try:
            current_year = datetime.now().year
            year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
            age = current_year - year_of_birth
            self.output_label.setText(f"{name} is {age} years old.")
        except ValueError:
            self.output_label.setText("Please enter a valid date of birth (MM/DD/YYYY).")


app = QApplication(sys.argv)

age_calculator = AgeCalculator()
age_calculator.show()

sys.exit(app.exec())

