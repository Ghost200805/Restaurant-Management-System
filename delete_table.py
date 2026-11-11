def delete_table_def():
    import sys
    from qt_material import apply_stylesheet
    from PyQt5.QtCore import Qt,QSize
    from PyQt5.QtWidgets import (QApplication,QLabel,QLineEdit,QMainWindow,QPushButton,QVBoxLayout,QWidget,QGridLayout,QHBoxLayout,QComboBox,QDialog,QDialogButtonBox,QSlider,QScrollArea,QAction,QToolBar)
    import mysql.connector as sc
    con=sc.connect(host='localhost',user='root',password='shamit',database='restaurant',charset='utf8')
    cur=con.cursor()

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
            message = QLabel("Enter Table NAME")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))

    class CustomDialog1(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("TABLE CREATED")
            QBtn = QDialogButtonBox.Ok 
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.layout = QVBoxLayout()
            message = QLabel("TABLE DELETED SUCCESSFULLY!")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))



    class MainWindow(QMainWindow):
        
        
        
        def __init__(self):
            super().__init__()
            toolbar = QToolBar()
            self.addToolBar(toolbar)
            button_action = QAction("Option Window(Database)", self)
            toolbar.addAction(button_action)
            button_action1 = QAction("Admin Logout", self)
            toolbar.addAction(button_action1)
            button_action2 = QAction("Option Window", self)
            toolbar.addAction(button_action2)
            button_action3 = QAction("User Logout", self)
            toolbar.addAction(button_action3)
            
            
            layout=QVBoxLayout()
            self.table_name_entry=QComboBox()
            del_button=QPushButton('DELETE')
            del_button.setFixedSize(100,50)

            layout.addWidget(QLabel('DELETE TABLE'),alignment=Qt.AlignCenter)
            layout.addWidget(QLabel('TABLE NAME'))
            layout.addWidget(self.table_name_entry)
            
            layout.addWidget(QLabel())
            layout.addWidget(del_button,alignment=Qt.AlignCenter)
            
            self.table_name_entry_=['select']
            a="show tables"
            cur.execute(a)
            res=cur.fetchall()
            for tables in res:
                x=str(tables)
                y=x.replace(")","")
                z=y.replace("'","")
                w=z.replace("(","")
                u=w.replace(",","")
                self.table_name_entry_.append(u)
            self.table_name_entry_.remove('food_type')
            self.table_name_entry.addItems(self.table_name_entry_)
            self.tablename=''
            
            self.table_name_entry.textActivated.connect(self.table)

            del_button.clicked.connect(self.delete_table)
            button_action.triggered.connect(self.go_to_optio_window_database)
            button_action2.triggered.connect(self.go_to_optio_window)
            button_action1.triggered.connect(self.addlogout)     
            button_action3.triggered.connect(self.logout) 
            
            widget=QWidget()
            widget.setLayout(layout)
            self.setCentralWidget(widget)
           

        def table(self,s):
            self.tablename=s

        def delete_table(self):
            if self.tablename=='' or self.tablename=='select':
                DG1=CustomDialog()
                DG1.exec()
            else:
                l=[]
                a="select name_food_type from food_type"
                cur.execute(a)
                res=cur.fetchall()
                for tables in res:
                    x=str(tables)
                    y=x.replace(")","")
                    z=y.replace("'","")
                    w=z.replace("(","")
                    u=w.replace(",","")
                    l.append(u)
                
                if self.tablename in l:
                    cur.execute("delete from food_type where name_food_type='"+self.tablename+"'")
                    con.commit()
                cur.execute("drop table "+self.tablename+"")
                con.commit()
                self.table_name_entry.clear()
                DG2=CustomDialog1()
                DG2.exec()
                self.table_name_entry_=['select']
                a="show tables"
                cur.execute(a)
                res=cur.fetchall()
                for tables in res:
                    x=str(tables)
                    y=x.replace(")","")
                    z=y.replace("'","")
                    w=z.replace("(","")
                    u=w.replace(",","")
                    self.table_name_entry_.append(u)
                self.table_name_entry_.remove('food_type')
                self.table_name_entry.addItems(self.table_name_entry_)
                self.tablename=''
        
        def go_to_optio_window_database(self):
            global var66
            var66=5
            self.close()   
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
    elif ji==5:
        from database_options import database_option_def
        database_option_def()
    elif ji==6:
        from LWA import lWA_Def
        lWA_Def()

