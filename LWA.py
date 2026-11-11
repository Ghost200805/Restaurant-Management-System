def lWA_Def():
    import sys
    from qt_material import apply_stylesheet
    from PyQt5.QtCore import Qt,QSize
    from PyQt5.QtWidgets import (QApplication,QLabel,QLineEdit,QMainWindow,QPushButton,QVBoxLayout,QWidget,QDialogButtonBox,QDialog,QAction,QToolBar)
    global var66
    var66=0
    class CustomDialog(QDialog):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("ERROR")

            QBtn = QDialogButtonBox.Ok 

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
            toolbar = QToolBar()
            self.addToolBar(toolbar)
            button_action2 = QAction("Option Window", self)
            toolbar.addAction(button_action2)
            button_action3 = QAction("User Logout", self)
            toolbar.addAction(button_action3)
            self.setWindowTitle("Admin Login Window")
            
            user_layout = QVBoxLayout()
            plain_layout = QVBoxLayout()
            pwd_layout = QVBoxLayout()
            plain2_layout = QVBoxLayout()
            buton_layout =QVBoxLayout()
            
            self.user_entry=QLineEdit()
            self.pwd_entry=QLineEdit()
            login_button=QPushButton('LOGIN')
            
            user_layout.addWidget(QLabel('ADMIN USERNAME'))
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
            self.setMinimumSize(QSize(300,300))
            button_action2.triggered.connect(self.go_to_optio_window)     
            button_action3.triggered.connect(self.logout) 

        def login_button_clicked(self):
            user_entry_text=self.user_entry.text()
            pwd_entry_text=self.pwd_entry.text()
            if user_entry_text=='admin' and pwd_entry_text=='owner':

                global var66
                var66=5
                self.close()
            else:
                dlg=CustomDialog()
                dlg.exec()
        def go_to_optio_window(self):
            global var66
            var66=2
            self.close() 
        def logout(self):
            global var66
            var66=1
            self.close()       
            
            
            
        
            

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')

    

    window = MainWindow()
    window.show()

    app.exec() 
    ji=var66
    if ji==1:
        from login_window import login_window_def
        login_window_def()
    elif ji==2:
        from option_window import option_window_def
        option_window_def()
    if ji==5:
        from database_options import database_option_def
        database_option_def()
