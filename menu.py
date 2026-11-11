def menu_def():
    import sys
    import importlib
    from qt_material import apply_stylesheet
    from PyQt5.QtCore import Qt,QSize
    from qt_material import apply_stylesheet
    from PyQt5.QtWidgets import (QApplication,QLabel,QLineEdit,QMainWindow,QPushButton,QVBoxLayout,QWidget,QGridLayout,QHBoxLayout,QComboBox,QDialog,QDialogButtonBox,QSlider,QFormLayout,QScrollArea,QGroupBox,QToolBar,QAction)
    import mysql.connector as sc
    con=sc.connect(host='localhost',user='root',password='shamit',database='restaurant',charset='utf8')
    cur=con.cursor()
    global var66
    var66=0
    class MainWindow(QMainWindow):
        
        
        
        def __init__(self):
            super().__init__()

            toolbar = QToolBar()
            self.addToolBar(toolbar)
            button_action1 = QAction("Option Window", self)
            toolbar.addAction(button_action1)
            button_action2 = QAction("User Logout", self)
            toolbar.addAction(button_action2)
            

            layout=QVBoxLayout()
            self.groupbox=QGroupBox('MENU')
            self.formlayout=QFormLayout()
            self.scrollarea =QScrollArea()

            self.scrollarea.setWidget(self.groupbox)
            self.scrollarea.setWidgetResizable(True)
            layout.addWidget(self.scrollarea)
            cur.execute('select name_food_type from food_type')
            ft=cur.fetchall()
            ftf=[]
            for i in range(0,len(ft)):
                a=str(ft[i])
                y=a.replace(")","")
                z=y.replace("'","")
                w=z.replace("(","")
                u=w.replace(",","")
                self.formlayout.addRow(QLabel(''+u+'',alignment=Qt.AlignCenter))
                self.groupbox.setLayout(self.formlayout)
                cur.execute('select name from '+u+'')
                ft1=cur.fetchall()
                cur.execute('select mrp from '+u+'')
                ft2=cur.fetchall()
                for i in range(1,len(ft1)):
                    a=str(ft1[i])
                    y=a.replace(")","")
                    z=y.replace("'","")
                    w=z.replace("(","")
                    u1=w.replace(",","") 
                    a=str(ft2[i])
                    y=a.replace(")","")
                    z=y.replace("'","")
                    w=z.replace("(","")
                    u2=w.replace(",","") 
                    self.formlayout.addRow(QLabel(''+str(i)+'    '+u1+'',alignment=Qt.AlignLeft),QLabel(u2,alignment=Qt.AlignRight))
                    self.groupbox.setLayout(self.formlayout) 

            button_action1.triggered.connect(self.go_to_optio_window)
            button_action2.triggered.connect(self.logout) 
            self.setMinimumSize(1080,600)


            widget=QWidget()

            widget.setLayout(layout)
            self.setCentralWidget(widget)

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