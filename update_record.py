def update_record_def():
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
            message = QLabel("      SELECT Table!      ")
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
            message = QLabel("      FIELD EMPTY!      ")
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
            message = QLabel("       DATA UPDATED!      ")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))

    class CustomDialog3(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("ERROR")
            QBtn = QDialogButtonBox.Ok 
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.layout = QVBoxLayout()
            message = QLabel("      ENTER DATA OF WHICH DATA TO BE UPDATED!      ")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))
            
    class CustomDialog4(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("ERROR")
            QBtn = QDialogButtonBox.Ok 
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.layout = QVBoxLayout()
            message = QLabel("      RECORD NOT FOUND!      ")
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
            
            layoutmain=QHBoxLayout()
            layout=QVBoxLayout()
            layout0=QVBoxLayout()
            
            self.table_info1=QLabel("FIELD    TYPE    NULL    KEY    DEFAULT    EXTRAS \n ")
            qlastlayout=QHBoxLayout()
            layout.addWidget(QLabel('UPDATE TABLE DATA',alignment=Qt.AlignCenter))
            layout.addWidget(QLabel('TABLE NAME'))
            self.table_name=QComboBox()
            self.groupbox=QGroupBox('TABLE')
            self.groupbox2=QGroupBox('UPDATE DATA')
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
            self.update_button=QPushButton('UPDATE')
            self.update_button.clicked.connect(self.update_)
            
            self.warnlabel=QLabel()
            
            self.formlayout2=QFormLayout()
            


            self.scrollarea2=QScrollArea()

            self.scrollarea2.setWidget(self.groupbox2)
            self.scrollarea2.setWidgetResizable(True)
            self.scrollarea2.setMinimumHeight(400)
            
            layout0.addWidget(self.scrollarea2)
            
            
            
            
            self.scrollarea =QScrollArea()

            self.scrollarea.setWidget(self.groupbox)
            self.scrollarea.setWidgetResizable(True)
            self.scrollarea.setMinimumHeight(400)

            qlastlayout.addWidget(self.paraeter)
            qlastlayout.addWidget(self.parameter_entry)
            qlastlayout.addWidget(self.update_button)
            
            layout.addWidget(self.scrollarea)
            layout.addLayout(qlastlayout)
            layout.addWidget(self.warnlabel)
            layout0.addWidget(self.table_info1)
            layoutmain.addLayout(layout)
            layoutmain.addLayout(layout0)
            
            button_action.triggered.connect(self.go_to_optio_window_database)
            button_action2.triggered.connect(self.go_to_optio_window)
            button_action1.triggered.connect(self.addlogout)     
            button_action3.triggered.connect(self.logout) 
            

            #self.delete_button.clicked.connect(self.delete)
            self.del_=''
        
            widget=QWidget()

            widget.setLayout(layoutmain)
            self.setCentralWidget(widget)

        def table(self,tn):
            self.tablename=tn
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
                a=str(self.dre1[0]).replace('    ','') 
                self.paraeter.setText("Enter '"+a+"' To Of Which Data Has To Be Updated.  ")
                self.warnlabel.setText("Warning:If record in '"+a+"' contain capital letters or any special character then please mention it.\n         ENTER CORRECT DATATYPE OF EACH FIELD")


                for i in reversed(range(self.formlayout2.count())): 
                    self.formlayout2.itemAt(i).widget().setParent(None)
                self.labellist=[]
                self.buttonlist=[]
                
                for i in range(0,len(re1)):
                    j=str(re1[i])
                    k=j.replace(',','')
                    l=k.replace(')','')
                    m=l.replace('(','')
                    n=m.replace("'",'')
                    jt=str(re1[i])
                    kt=jt.replace(',','')
                    lt=kt.replace(')','')
                    mt=lt.replace('(','')
                    nt=mt.replace("'",'')                
                    self.labellist.append(QLabel(''+nt+''))
                    self.buttonlist.append(QLineEdit(''))
                    self.formlayout2.addRow(self.labellist[i],self.buttonlist[i])
                self.groupbox2.setLayout(self.formlayout2)
                
                self.table_info1.clear()   
                if self.tablename!='select':
                    cur.execute("desc "+tn+"")
                    res=cur.fetchall()
                    x="FIELD    TYPE    NULL    KEY    DEFAULT    EXTRAS \n "

                    z=str(x)
                    for i in res:
                        j=str(i)
                        k=j.replace('(','')
                        l=k.replace(')','')
                        m=l.replace("'",'')
                        n=m.replace(',','    ')
                        z=z+ '\n' +n
                    self.table_info1.setText(z)
        def update_(self):
            z=''
            a=self.parameter_entry.text()
            if self.tablename=='' or self.tablename=='select':
                dle=CustomDialog()
                dle.exec()
                val=86
            elif a=='':
                dle=CustomDialog3()
                dle.exec()
                val=43

            else: 
                val=0
                for i in range(0,len(self.buttonlist)): 
                    k=(self.buttonlist[i].text())
                    b=(self.labellist[i].text())
                    if k==''or val!=0:
                        z=' '
                        val=val+1
                        dle=CustomDialog1()
                    elif val==0:
                        z=z+b+'='+"'"+k+"'"+','
                        dle=CustomDialog2()
                        
                if val==0:
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
                    if a in l:
                        x=self.dre1[0]
                        cur.execute("update "+self.tablename+" set "+z[:len(z)-1]+" where "+x[0:len(x)-4]+"='"+a+"' ")
                        con.commit()
                    else:
                        dle=CustomDialog4()
                dle.exec()
            if val==0:
                for i in range(0,len(self.buttonlist)): 
                            self.buttonlist[i].clear()
        
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

