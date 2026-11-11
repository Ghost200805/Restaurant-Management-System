def option_window_def():
    import sys
    from qt_material import apply_stylesheet
    from PyQt5.QtCore import Qt,QSize
    from PyQt5.QtWidgets import (
        QApplication,
        QLabel,
        QLineEdit,
        QMainWindow,
        QPushButton,
        QVBoxLayout,
        QWidget,QGridLayout,QToolBar,QAction
    )
    global var66
    var66=0
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("options to go")

            
            
            bt_menu=QPushButton("MENU")
            bt_menu.setFixedSize(QSize(393,275))
            bt2_billing=QPushButton("BILLING")
            bt2_billing.setFixedSize(QSize(393,275))
            bt3_database=QPushButton("DATABASE")
            bt3_database.setFixedSize(QSize(393,275))
            bt4_logout=QPushButton("LOGOUT")
            bt4_logout.setFixedSize(QSize(393,275))
            
            
            layout0=QVBoxLayout()
            layout0.addWidget(QLabel('OPTION WINDOW',alignment=Qt.AlignCenter))

            layout1= QGridLayout()
            layout1.addWidget(bt_menu,0,0)
            layout1.addWidget(bt2_billing,0,1)
            layout1.addWidget(bt4_logout,1,1)
            layout1.addWidget(bt3_database,1,0)
            layout1.setContentsMargins(0,0,0,0)
            layout1.setSpacing(0)



            layout0.addLayout(layout1)
            
            widget = QWidget()
            widget.setLayout(layout0)
            self.setCentralWidget(widget)
            self.setMinimumSize(QSize(800,600))

            bt_menu.clicked.connect(self.menu)
            bt2_billing.clicked.connect(self.billing)
            bt3_database.clicked.connect(self.database)
            bt4_logout.clicked.connect(self.logout)

        def menu(self):
            global var66
            var66=3
            self.close()
        def billing(self):
            global var66
            var66=4
            self.close()
        def database(self):
            global var66
            var66=6
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
    elif ji==6:
        from  LWA import lWA_Def
        lWA_Def()

    elif ji==4:
        from  bill import bill_def
        bill_def()
    elif ji==3:
        from  menu import menu_def
        menu_def()

            


            