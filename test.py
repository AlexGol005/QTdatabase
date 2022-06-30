import os

import PySide2
import PySide2.QtWidgets as qtw
import PySide2.QtGui as qtg

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Лабораторное оборудование')
        self.setLayout(qtw.QVBoxLayout())
        my_label = qtw.QLabel('Выберите СИ')
        my_label.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(my_label)



        my_button = qtw.QPushButton('Нажми меня')
        my_button.clicked.connect(lambda: press_it())
        self.layout().addWidget(my_button)


        # my_entry = qtw.QLineEdit()
        # my_entry.setObjectName('название')
        # my_entry.setText('введите название')
        # self.layout().addWidget(my_entry)

        # my_combo = qtw.QComboBox(self)
        # my_combo.setEditable(True)
        # my_combo.insertPolicy = qtw.QComboBox.InsertAtTop
        # my_combo.addItem('Весы', 1)
        # my_combo.addItem('Барометр', 2)
        # my_combo.addItem('Гигрометр', 3)
        # my_combo.addItem('Вискозиметр', 4)
        # my_combo.addItem('Секундомер', 5)
        # my_combo.addItem('Термометр', 6)
        # self.layout().addWidget(my_combo)

        my_spin = qtw.QSpinBox(self)
        my_spin.setPrefix('#')
        my_spin.setSuffix('штук')
        my_spin.setValue(10)
        my_spin.setMaximum(100)
        my_spin.setMinimum(0)
        my_spin.setSingleStep(5)
        my_spin.setFont(qtg.QFont("Helvetica", 18))


        self.layout().addWidget(my_spin)

        self.show()

        # def press_it():
        #     my_label.setText(f'Вы выбрали {my_spin.currentText()}!')
        def press_it():
            my_label.setText(f'Вы выбрали {my_spin.value()}!')






app = qtw.QApplication([])
mw = MainWindow()


app.exec_()