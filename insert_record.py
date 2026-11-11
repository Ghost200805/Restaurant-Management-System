def insert_record_def():
    import sys
    from qt_material import apply_stylesheet
    from PyQt5.QtCore import Qt,QSize
    from PyQt5.QtWidgets import (QApplication,QLabel,QLineEdit,QMainWindow,QPushButton,QVBoxLayout,QWidget,QGridLayout,QHBoxLayout,QComboBox,QDialog,QDialogButtonBox,QSlider,QFormLayout,QScrollArea,QGroupBox,QToolBar,QAction)
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
            self.setWindowTitle("SUCCESS")
            QBtn = QDialogButtonBox.Ok 
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.layout = QVBoxLayout()
            message = QLabel("      DATA ADDED      ")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))

    class CustomDialog2(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Error")
            QBtn = QDialogButtonBox.Ok 
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.layout = QVBoxLayout()
            message = QLabel("      FIELD  EMPTY!       ")
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

            layout=QHBoxLayout()
            layoutleft=QVBoxLayout()
            layoutright=QVBoxLayout()
            self.table_name=QComboBox()
            self.ins_but=QPushButton('INSERT RECORD')
            layoutleft.addWidget(QLabel('INSERT',alignment=Qt.AlignCenter))
            layoutleft.addWidget(QLabel('NEW RECORD',alignment=Qt.AlignCenter))
            layoutleft.addWidget(QLabel('TABLE NAME'))
            layoutleft.addWidget(self.table_name)
            self.table_info=QLabel()
            self.warn=QLabel()
            layoutleft.addWidget(self.table_info)
            self.groupbox=QGroupBox('')

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
            self.table_name.addItems(self.table_name_entry_)
            self.tablename=''

            layoutleft.addWidget(self.ins_but)
            self.table_name.textActivated.connect(self.table)

            
            self.ins_but.clicked.connect(self.ins_rec)

            self.formlayout=QFormLayout()
            


            self.scrollarea =QScrollArea()

            self.scrollarea.setWidget(self.groupbox)
            self.scrollarea.setWidgetResizable(True)
            self.scrollarea.setFixedHeight(400)
            
            layoutright.addWidget(self.scrollarea)
            layoutleft.addWidget(self.warn)
            layout.addLayout(layoutleft)
            layout.addLayout(layoutright)
            widget=QWidget()

            widget.setLayout(layout)
            self.setCentralWidget(widget)   
            button_action.triggered.connect(self.go_to_optio_window_database)
            button_action2.triggered.connect(self.go_to_optio_window)
            button_action1.triggered.connect(self.addlogout)     
            button_action3.triggered.connect(self.logout) 
                
        
        def table(self,s):
            for i in reversed(range(self.formlayout.count())): 
                self.formlayout.itemAt(i).widget().setParent(None)
            self.tablename=s
            self.table_info.clear()   
            if self.tablename!='select':
                cur.execute("desc "+s+"")
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
                self.table_info.setText(z)
                labellist=[]
                self.buttonlist=[]
                cur.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'restaurant' AND table_name = '"+s+"'")
                re1=cur.fetchall()
    
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
                    labellist.append(QLabel(''+nt+''))
                    self.buttonlist.append(QLineEdit(''))
                    self.formlayout.addRow(labellist[i],self.buttonlist[i])
                self.groupbox.setLayout(self.formlayout)
                self.warn.setText('WARNING: ENTER CORRECT DATATYPE OF EACH FIELD')

        def ins_rec(self):
            z=''
            if self.tablename=='' or self.tablename=='select':
                dle=CustomDialog()
                dle.exec()
            else: 
                val=0
                for i in range(0,len(self.buttonlist)): 
                    a=(self.buttonlist[i].text())
                    if a==''or val!=0:
                        z=' '
                        val=val+1
                        dle=CustomDialog2()
                    elif val==0:
                        z=z+"'"+a+"'"+','
                        
                        dle=CustomDialog1()
                dle.exec()
            if val==0:

                cur.execute("insert into "+self.tablename+ " values("+z[:len(z)-1]+")")
                con.commit()
                
                    
                
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