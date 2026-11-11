def delete_table_data_def():
    import sys
    from qt_material import apply_stylesheet
    from PyQt5.QtCore import Qt,QSize
    from PyQt5.QtWidgets import (QApplication,QLabel,QLineEdit,QMainWindow,QPushButton,QVBoxLayout,QWidget,QGridLayout,QHBoxLayout,QComboBox,QDialog,QDialogButtonBox,QSlider,QFormLayout,QScrollArea,QGroupBox,QAction,QToolBar)
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
            message = QLabel("      Enter Table!      ")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))
    class CustomDialog1(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("ERROR")
            QBtn = QDialogButtonBox.Ok 
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.layout = QVBoxLayout()
            message = QLabel("      Enter Record Field!      ")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))

    class CustomDialog2(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("ERROR")
            QBtn = QDialogButtonBox.Ok 
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.layout = QVBoxLayout()
            message = QLabel("      No Record Found     ")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))

    class CustomDialog3(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("SUCCESS")
            QBtn = QDialogButtonBox.Ok 
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.layout = QVBoxLayout()
            message = QLabel("      Record Deleted.\nReselect Table Name To See Updated Data     ")
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
            qlastlayout=QHBoxLayout()
            layout.addWidget(QLabel('DELETE TABLE DATA',alignment=Qt.AlignCenter))
            layout.addWidget(QLabel('TABLE NAME'))
            self.table_name=QComboBox()
            self.groupbox=QGroupBox('TABLE')
            layout.addWidget(self.table_name)

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
            
            self.table_name.addItems(self.table_name_entry_)
            self.tablename=''

            self.table_name.textActivated.connect(self.table)

            self.formlayout=QFormLayout()
            
            
            self.paraeter=QLabel()
            self.parameter_entry=QLineEdit()
            self.delete_button=QPushButton('DELETE')
            
            self.warnlabel=QLabel()
            self.scrollarea =QScrollArea()

            self.scrollarea.setWidget(self.groupbox)
            self.scrollarea.setWidgetResizable(True)
            self.scrollarea.setFixedHeight(400)

            qlastlayout.addWidget(self.paraeter)
            qlastlayout.addWidget(self.parameter_entry)
            qlastlayout.addWidget(self.delete_button)
            
            layout.addWidget(self.scrollarea)
            layout.addLayout(qlastlayout)
            layout.addWidget(self.warnlabel)

            self.delete_button.clicked.connect(self.delete)
            self.del_=''
        

            button_action.triggered.connect(self.go_to_optio_window_database)
            button_action2.triggered.connect(self.go_to_optio_window)
            button_action1.triggered.connect(self.addlogout)     
            button_action3.triggered.connect(self.logout) 
                
            widget=QWidget()

            widget.setLayout(layout)
            self.setCentralWidget(widget)

        def table(self,tn):
            for i in reversed(range(self.formlayout.count())): 
                self.formlayout.itemAt(i).widget().setParent(None)
            if tn!='select':
                self.tablename=tn
                self.dre1=[]
                cur.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'restaurant' AND table_name = '"+tn+"'")
                re1=cur.fetchall()

                a1="select count(*)from "+tn+""
                cur.execute(a1)
                f=cur.fetchone()    
                a=str(f).replace('(','')
                ab=a.replace(')','')
                abc=ab.replace(',','')
                abce=int(abc)
                o=''
                for i in range(0,len(re1)):
                    j=str(re1[i])
                    k=j.replace(',','    ')
                    l=k.replace(')','')
                    m=l.replace('(','')
                    n=m.replace("'",'')
                    self.dre1.append(n)
                    o=o+n
                w=QLabel(o)
                self.formlayout.addWidget(w)
            
                cur.execute("select * from "+tn+" ")
                for s in range(0,abce):
                    c=cur.fetchone()
                    d=str(c)
                    e=d.replace(',','    ')
                    f=e.replace(')','')
                    g=f.replace('(','')
                    h=g.replace("'",'')
                
                
                    self.formlayout.addRow(QLabel(''+h+''))
                self.groupbox.setLayout(self.formlayout) 
                a=self.dre1[0].replace('    ','') 
                self.paraeter.setText("Enter '"+a+"' To Be Deleted")
                self.warnlabel.setText("Warning:If record in '"+a+"' contain capital letters or any special character then please mention it.")
                

            
        def delete(self,z):
            if self.tablename=='' or self.tablename=='select':
                dle=CustomDialog()
                dle.exec()
            else:
                cur.execute("select "+self.dre1[0]+" from "+self.tablename+"")
                c=cur.fetchall()
                l=[]
                for x in c:
                    d=str(x)
                    e=d.replace(',','')
                    f=e.replace(')','')
                    g=f.replace('(','')
                    h=g.replace("'",'')
                    l.append(h)
                a=self.parameter_entry.text()
                if a=='':
                    dle=CustomDialog1()
                    dle.exec()
                elif a not in l:
                    dle=CustomDialog2()
                    dle.exec()
                elif a in l:
                    cur.execute("delete from "+self.tablename+" where "+self.dre1[0]+"='"+a+"'")
                    con.commit()
                    dle=CustomDialog3()
                    dle.exec()
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
    if ji==5:
        from database_options import database_option_def
        database_option_def()
    elif ji==6:
        from LWA import lWA_Def
        lWA_Def()
    elif ji==2:
        from option_window import option_window_def
        option_window_def()
    elif ji==1:
        from login_window import login_window_def
        login_window_def()
