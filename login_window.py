def login_window_def():
    import sys    
    from PyQt5.QtCore import Qt,QSize
    from qt_material import apply_stylesheet
    from PyQt5.QtWidgets import (QApplication,QLabel,QLineEdit,QMainWindow,QPushButton,QVBoxLayout,QWidget,QDialogButtonBox,QDialog)
    global var66
    var66=0
    class CustomDialog(QDialog):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("ERROR")

            QBtn = QDialogButtonBox.ok

            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            
            

            self.layout = QVBoxLayout()
            message = QLabel("Username or Password doesn't match!")
            self.layout.addWidget(message)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            

    class MainWindow(QMainWindow):
        
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Login Window")
            
            user_layout = QVBoxLayout()
            plain_layout = QVBoxLayout()
            pwd_layout = QVBoxLayout()
            plain2_layout = QVBoxLayout()
            buton_layout =QVBoxLayout()
            
            self.user_entry=QLineEdit()
            self.pwd_entry=QLineEdit()
            login_button=QPushButton('LOGIN')
            
            user_layout.addWidget(QLabel('USERNAME'))
            user_layout.addWidget(self.user_entry)
            
            plain_layout.addWidget(QLabel())

            pwd_layout.addWidget(QLabel('PASSWORD'))
            pwd_layout.addWidget(self.pwd_entry)

            plain2_layout.addWidget(QLabel())

            buton_layout.addWidget(login_button)
            login_button.clicked.connect(self.login_button_clicked)

            user_layout.addLayout(plain_layout)
            plain_layout.addLayout(pwd_layout)
            pwd_layout.addLayout(plain2_layout)
            plain2_layout.addLayout(buton_layout)
            
        
            widget=QWidget()
            widget.setLayout(user_layout)
            self.setCentralWidget(widget)
            self.setMinimumSize(QSize(300,250))

        def login_button_clicked(self):
            user_entry_text=self.user_entry.text()
            pwd_entry_text=self.pwd_entry.text()
            if user_entry_text=='user1' and pwd_entry_text=='pwd':
                global var66
                var66=2
                self.close()
            else:
                dlg=CustomDialog()
                dlg.exec()
            
            
        
        

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    window = MainWindow()
    window.show()
    app.exec()


    ji=var66
    if ji==2:
        from  option_window import option_window_def
        option_window_def()
        

