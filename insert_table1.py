def insert_table1_def():
    import sys
    import pandas as pd
    from qt_material import apply_stylesheet
    from PyQt5.QtCore import Qt,QSize
    from PyQt5.QtWidgets import (QApplication,QLabel,QLineEdit,QMainWindow,QPushButton,QVBoxLayout,QWidget,QGridLayout,QHBoxLayout,QComboBox,QDialog,QDialogButtonBox,QAction,QToolBar,QGroupBox,QFormLayout,QScrollArea)
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
            message = QLabel("      Enter Table Type      ")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))


    class CustomDialog1(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("      TABLE CREATED      ")
            QBtn = QDialogButtonBox.Ok 
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.layout = QVBoxLayout()
            message = QLabel("\n\nTABLE CREATED SUCCESSFULLY!")
            m1=QLabel('\n\n NOTE-sno,name,mrp column will be added if you have selected tabble type as food')
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(m1,alignment=Qt.AlignLeft)
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
            message = QLabel("TABLE ALREADY PRESENT!")
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
            message = QLabel("      Table Name 'Table' Not Supported      ")
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
            layoutleft_butt=QGridLayout()

            self.setWindowTitle("insert table")

            self.table_name_entry=QLineEdit()
            self.type_entry=QComboBox()
            self.column_name_entry=QLineEdit()
            self.column_datatype_entry=QLineEdit()
            self.add_attribute_entry=QLineEdit()
            list=['select','administrative','food']
            self.type_entry.addItems(list)

            bt=QPushButton('ADD COLUMN')
            Bt2=QPushButton('CREATE TABLE')

            layout.addLayout(layoutleft)
            layout.addLayout(layoutright)          
            layoutleft.addWidget(QLabel('TABLE NAME'))
            layoutleft.addWidget(self.table_name_entry)
            layoutleft.addWidget(QLabel('TABLE TYPE'))
            layoutleft.addWidget(self.type_entry)
            layoutleft.addWidget(QLabel('COLUMN NAME'))
            layoutleft.addWidget(self.column_name_entry)
            layoutleft.addWidget(QLabel('DATA TYPE'))
            layoutleft.addWidget(self.column_datatype_entry)
            layoutleft.addWidget(QLabel('ADD ATTRIBUTE(IF MORE THAN ONE THEN ADD ENTER WITH COMAS(,)) '))
            layoutleft.addWidget(self.add_attribute_entry)
            layoutleft.addLayout(layoutleft_butt)
            layoutleft_butt.addWidget(bt,0,0)
            layoutleft_butt.addWidget(Bt2,0,1)

            bt.clicked.connect(self.add_columns)
            self.df=pd.DataFrame()
            self.df.loc[0,0]='name'
            self.df.loc[0,1]='datatype'
            self.df.loc[0,2]='attributes'
            self.number=1
            
            self.groupbox=QGroupBox('Table')
            self.formlayout=QFormLayout()
            self.scrollarea =QScrollArea()
            self.scrollarea.setWidget(self.groupbox)
            self.scrollarea.setWidgetResizable(True)
            self.scrollarea.setFixedHeight(400)
            layoutright.addWidget(self.scrollarea)
            btdis=QPushButton('DISCARD')
            layoutright.addWidget(btdis)
            Bt2.clicked.connect(self.create_table)
            
            button_action.triggered.connect(self.go_to_optio_window_database)
            button_action2.triggered.connect(self.go_to_optio_window)
            button_action1.triggered.connect(self.addlogout)     
            button_action3.triggered.connect(self.logout)
            btdis.clicked.connect(self.discard)
            self.formlayout.addRow(QLabel('NAME    DATATYPE    ATTRIBUTES'))
            self.formlayout.addRow(QLabel('')) 
            self.groupbox.setLayout(self.formlayout)

            
            
            widget=QWidget()
            widget.setLayout(layout)
            self.setCentralWidget(widget)
            self.typetext=''
            self.type_entry.textActivated.connect(self.type_entry_)
        
        def type_entry_(self,z):
            self.typetext=z
            

        def add_columns(self):
            column_entry=self.column_name_entry.text()
            column_datatype=self.column_datatype_entry.text()
            column_attributes=self.add_attribute_entry.text()
            self.df.loc[self.number,0]=column_entry
            self.df.loc[self.number,1]=column_datatype
            self.df.loc[self.number,2]=column_attributes
            self.number=self.number+1
            self.column_name_entry.clear()
            self.column_datatype_entry.clear()
            self.add_attribute_entry.clear()
            self.formlayout.addRow(QLabel(''+column_entry+'    '+column_datatype+'    '+column_attributes+'')) 
            self.groupbox.setLayout(self.formlayout)

        def create_table(self):
            table_name=self.table_name_entry.text()
            y=self.typetext
            if  y=='select'or y=='':
                dle=CustomDialog()
                dle.exec()
            else:
                l=[]
                a="show tables"
                cur.execute(a)
                res=cur.fetchall()
                for tables in res:
                    x=str(tables)
                    y=x.replace(")","")
                    z=y.replace("'","")
                    w=z.replace("(","")
                    u=w.replace(",","")
                    l.append(u)
                if table_name in l:
                    dle=CustomDialog2()
                    dle.exec()
                elif table_name=='Table'or table_name=='table'or table_name=='TABLE':
                    dle=CustomDialog3()
                    dle.exec()
                else:
                    if self.typetext=='food':
                        print("insert into food_type values('"+table_name+"')")
                        cur.execute("insert into food_type values('"+table_name+"')")
                        con.commit()
                        len1=self.df.index
                        self.df.loc[self.number,0:2]=['sno','int','']
                        self.df.loc[self.number+1,0:2]=['Name','varchar(89)','']
                        self.df.loc[self.number+2,0:2]=['mrp','int','']
                        
                    lent=len(self.df.index)
                    aa=''
                    for x in range(1,lent):
                        att=str(self.df.loc[x,2])
                        att1=att.replace(',',' ')
                        stri=str(self.df.loc[x,0])+' '+str(self.df.loc[x,1])+' '+att1+','
                        aa=aa+stri
                    aa1=aa[:len(aa)-1]
                    print("create table "+table_name+"("+aa1+")")
                    cur.execute("create table "+table_name+"("+aa1+")")
                    con.commit()   
                    self.table_name_entry.clear()
                    dle=CustomDialog1()
                    dle.exec()
                    for i in reversed(range(2,self.formlayout.count())): 
                        self.formlayout.itemAt(i).widget().setParent(None)
                        del self.df
                        self.df=pd.DataFrame()
                        self.df.loc[0,0]='name'
                        self.df.loc[0,1]='datatype'
                        self.df.loc[0,2]='attributes'
                        self.number=1
        def discard(self):
            del self.df
            self.df=pd.DataFrame()
            self.df.loc[0,0]='name'
            self.df.loc[0,1]='datatype'
            self.df.loc[0,2]='attributes'
            self.number=1
        
            for i in reversed(range(2,self.formlayout.count())): 
                self.formlayout.itemAt(i).widget().setParent(None)
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

