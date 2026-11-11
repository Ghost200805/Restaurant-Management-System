def database_option_def():
    import sys

    from PyQt5.QtCore import Qt,QSize
    from qt_material import apply_stylesheet
    from PyQt5.QtWidgets import (QApplication,QLabel,QLineEdit,QMainWindow,QPushButton,QVBoxLayout,QWidget,QGridLayout,QToolBar,QAction)
    global var66
    var66=0
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            toolbar = QToolBar()
            self.addToolBar(toolbar)
            button_action1 = QAction("Admin Logout", self)
            toolbar.addAction(button_action1)
            button_action2 = QAction("Option Window", self)
            toolbar.addAction(button_action2)
            button_action3 = QAction("User Logout", self)
            toolbar.addAction(button_action3)
            
            
            
            self.setWindowTitle("database(options)")
            layout=QVBoxLayout()
            but1=QPushButton('CREATE TABLE')
            
            but3=QPushButton('INSERT RECORD')
            but4=QPushButton('DELETE TABLE DATA')
            but5=QPushButton('DELETE TABLE')
            but6=QPushButton('UPDATE TABLE DATA')
            
            
            layout.addWidget(but1)
            
            layout.addWidget(but3)
            layout.addWidget(but4)
            layout.addWidget(but5)
            layout.addWidget(but6)
            
            button_action2.triggered.connect(self.go_to_optio_window)
            button_action1.triggered.connect(self.addlogout)     
            button_action3.triggered.connect(self.logout)    
            but1.clicked.connect(self.bt1)
            but3.clicked.connect(self.bt3)
            but4.clicked.connect(self.bt4)
            but5.clicked.connect(self.bt5)
            but6.clicked.connect(self.bt6)
        

            widget=QWidget()
            widget.setLayout(layout)
            self.setCentralWidget(widget)

        def go_to_optio_window(self):
            global var66
            var66=2
            self.close()
        def addlogout(self):
            global var66
            var66=6
            self.close()
        def logout(self):
            global var66
            var66=1
            self.close()

        def bt1(self):
            global var66
            var66=51
            self.close()
        def bt3(self):
            global var66
            var66=52
            self.close()
        def bt4(self):
            global var66
            var66=53
            self.close()
        def bt5(self):
            global var66
            var66=54
            self.close()
        def bt6(self):
            global var66
            var66=55
            self.close()







    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')

    window = MainWindow()
    window.show()

    app.exec()
    ji=var66  
    if ji==1:
        from  login_window import login_window_def
        login_window_def()
    elif ji==2:   
        from option_window import option_window_def
        option_window_def()
    elif ji==6:
        from LWA import lWA_Def
        lWA_Def()
    elif ji==51:
        from insert_table1 import insert_table1_def
        insert_table1_def()
    elif ji==52:
        from insert_record import insert_record_def
        insert_record_def()
    elif ji==53:
        from delete_table_data import delete_table_data_def
        delete_table_data_def()
    elif ji==54:
        from delete_table import delete_table_def
        delete_table_def()
    elif ji==55:
        from update_record import update_record_def
        update_record_def()