def bill_def():
    import sys
    import mysql.connector as sc
    from datetime import datetime
    import pandas as pd
    from qt_material import apply_stylesheet
    from PyQt5.QtCore import Qt,QSize
    from PyQt5.QtWidgets import (QApplication,QLabel,QLineEdit,QMainWindow,QPushButton,QVBoxLayout,QWidget,QDialogButtonBox,QDialog,QHBoxLayout,QComboBox,QGroupBox,QScrollArea,QFormLayout,QDoubleSpinBox,QSpinBox,QToolBar,QAction)
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
            message = QLabel("CUSTOMER DETAIL INCOMPLETE")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))

    class CustomDialog2(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("SUCCESS")
            QBtn = QDialogButtonBox.Ok 
            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)
            self.layout = QVBoxLayout()
            message = QLabel("ORDER PLACED")
            self.layout.addWidget(message,alignment=Qt.AlignCenter)
            self.layout.addWidget(self.buttonBox,alignment=Qt.AlignCenter)
            self.setLayout(self.layout)
            self.setMinimumSize(QSize(150,100))


    class MainWindow(QMainWindow):
        
        
        def __init__(self):
            super().__init__()

            toolbar = QToolBar()
            self.addToolBar(toolbar)
            button_action1 = QAction("Option Window", self)
            toolbar.addAction(button_action1)
            button_action2 = QAction("Logout Window", self)
            toolbar.addAction(button_action2)
            
            self.setWindowTitle("billing")
            layout_main=QHBoxLayout()
            layout_main_customer_detail_order=QVBoxLayout()
            layout_main_order_summery=QVBoxLayout()
            layout_quantity=QHBoxLayout()
            layout_remove=QHBoxLayout()
            self.remove_entry=QSpinBox()
            self.remove_entry.setMaximum(999999999)
            self.remove_entry.setMinimum(1)

            remove_button=QPushButton('REMOVE')
            
            
            self.customer_name_entry=QLineEdit()
            self.customer_phone_entry=QLineEdit()
            self.choice_main=QComboBox()
            self.choice_specific=QComboBox()
            add_button=QPushButton('ADD')
            self.groupbox=QGroupBox('ORDERS')
            add_button.setFixedSize(70,70)
            self.quantity_=QSpinBox()
            self.quantity_.setMaximum(999999999) 
            self.quantity_.setMinimum(1) 
            layout_quantity.addWidget(QLabel('Quantity',alignment=Qt.AlignRight | Qt.AlignBottom))
            layout_quantity.addWidget(self.quantity_)
            layout_remove.addWidget(QLabel('ENTER THE SERIAL NUMBER TO BE REMOVED'))
            layout_remove.addWidget(self.remove_entry)
            layout_remove.addWidget(remove_button)
            conferm_button=QPushButton('CONFIRM')

            
            self.label_show_data_of_selected_items=QLabel()
            
            layout_main_customer_detail_order.addWidget(QLabel('COSTUMER ORDER',alignment=Qt.AlignCenter))
            layout_main_customer_detail_order.addWidget(QLabel())
            layout_main_customer_detail_order.addWidget(QLabel('CUSTOMER NAME'))
        
            layout_main_customer_detail_order.addWidget(self.customer_name_entry)
        
            layout_main_customer_detail_order.addWidget(QLabel())
            layout_main_customer_detail_order.addWidget(QLabel('PHONE NUMBER'))
            
            layout_main_customer_detail_order.addWidget(self.customer_phone_entry)
            
            layout_main_customer_detail_order.addWidget(QLabel())
            layout_main_customer_detail_order.addWidget(QLabel('choose main'))
            layout_main_customer_detail_order.addWidget(self.choice_main)
            layout_main_customer_detail_order.addWidget(QLabel())
            layout_main_customer_detail_order.addWidget(QLabel('choose specific'))
            layout_main_customer_detail_order.addWidget(self.choice_specific)
            layout_main_customer_detail_order.addLayout(layout_quantity)
            layout_main_customer_detail_order.addWidget(QLabel())
            layout_main_customer_detail_order.addWidget(self.label_show_data_of_selected_items)
            layout_main_customer_detail_order.addWidget(QLabel())
            layout_main_customer_detail_order.addWidget(add_button)

            self.formlayout=QFormLayout()
            self.scrollarea =QScrollArea()

            self.scrollarea.setWidget(self.groupbox)
            self.scrollarea.setWidgetResizable(True)
            self.scrollarea.setFixedHeight(400)
        
            
            self.choice_specific_=['select']
            self.choice_specific.addItems(self.choice_specific_)

            

            self.choice_main_=['select']
            a="select name_food_type from food_type"
            cur.execute(a)
            res=cur.fetchall()
            for tables in res:
                x=str(tables)
                y=x.replace(")","")
                z=y.replace("'","")
                w=z.replace("(","")
                u=w.replace(",","")
                self.choice_main_.append(u)
            self.choice_main.addItems(self.choice_main_)
            

            
            self.choice_main.currentTextChanged.connect(self.main_choice)
            
            heading_ordersummery=QLabel('ORDER SUMMARY')
            

            layout_main_order_summery.addWidget(heading_ordersummery,alignment=Qt.AlignCenter)
            layout_main_order_summery.addWidget(self.scrollarea)
            layout_main_order_summery.addLayout(layout_remove)
            layout_main_order_summery.addWidget(conferm_button)


            self.setMinimumSize(QSize(1280,720))
            layout_main.addLayout(layout_main_customer_detail_order)
            layout_main.addLayout(layout_main_order_summery)

            widget=QWidget()
            widget.setLayout(layout_main)
            self.setCentralWidget(widget)
            
            d={}

            d['Dish']=[None]
            d['Price']=[None]
            d['Quantity']=[None]
            d['Amount']=[None]
            self.df=pd.DataFrame(d)
            add_button.clicked.connect(self.add)
            remove_button.clicked.connect(self.remove)
            conferm_button.clicked.connect(self.conferm)
            button_action1.triggered.connect(self.go_to_optio_window)
            button_action2.triggered.connect(self.logout)        
            

        def main_choice(self,i):
            self.choice_specific.clear()
            choicespecific_=['select']
            if i=='select':
            
                self.choice_specific.addItems(choicespecific_) 
            else: 
                a="select name from "+i+" "
                cur.execute(a)
                res=cur.fetchall()
                for tables in res:
                    x=str(tables)
                    y=x.replace(")","")
                    z=y.replace("'","")
                    w=z.replace("(","")
                    u=w.replace(",","")
                    choicespecific_.append(u)
                self.choice_specific.addItems(choicespecific_)
                self.choice_specific.currentTextChanged.connect(self.main_choice_specific)
                self.p=i
            
        def main_choice_specific(self,z):
            o="select name,mrp from "+self.p+" where name='"+z+"'"
            s=cur.execute(o)
            res=cur.fetchone()
            res=str(res)
            res1=res.replace("'","  ")
            res2=res1.replace("(","")
            res3=res2.replace(",","  ")
            resf=res3.replace(")","")
            self.label_show_data_of_selected_items.setText(resf)
            self.u=z
        def add(self):
            a=self.label_show_data_of_selected_items.text()
            if a=='None'or a=='':
                hakj=1
            else:   
                self.quantity=self.quantity_.value()
                o="select name from "+self.p+" where name='"+self.u+"'"
                s=cur.execute(o)
                res=cur.fetchone()
                res=str(res)
                res1=res.replace("'","  ")
                res2=res1.replace("(","")
                res3=res2.replace(",","  ")
                resf1=res3.replace(")","")
                o="select mrp from "+self.p+" where name='"+self.u+"'"
                s=cur.execute(o)
                res=cur.fetchone()
                res=str(res)
                res1=res.replace("'","  ")
                res2=res1.replace("(","")
                res3=res2.replace(",","  ")
                resf2=res3.replace(")","")

                self.amount=int(resf2)*int(self.quantity)


                self.df.loc[len(self.df.index)]=[resf1,resf2,self.quantity,self.amount]
            
                self.formlayout.addRow(QLabel(str(len(self.df.index)-1)+'    '+str(self.df.loc[len(self.df.index)-1,'Dish'])+'       '+str(self.df.loc[len(self.df.index)-1,'Price'])+'        '+str(self.df.loc[len(self.df.index)-1,'Quantity'])),QLabel('AMOUNT:'+str(self.amount)+"",alignment=Qt.AlignRight))
                self.groupbox.setLayout(self.formlayout) 

        def remove(self):
            om=self.remove_entry.text()
            om=int(om)

            if om in range(0,len(self.df.index)):
        
                self.df.drop(om,axis=0,inplace=True)
                self.df.reset_index(drop=True, inplace=True)
                for i in reversed(range(self.formlayout.count())): 
                    self.formlayout.itemAt(i).widget().setParent(None)
                for i in range(1,len(self.df.index)):
                    self.formlayout.addRow(QLabel(str(i)+'    '+str(self.df.loc[i,'Dish'])+'       '+str(self.df.loc[i,'Price'])+'        '+str(self.df.loc[i,'Quantity'])),QLabel("AMOUNT:"+str(self.df.loc[i,'Amount'])+"",alignment=Qt.AlignRight))
                    self.groupbox.setLayout(self.formlayout)
    
            
        def conferm(self):
            name=self.customer_name_entry.text()
            phno=self.customer_phone_entry.text()
            ti=datetime.today()
            tii=str(ti)
            z=tii.replace('-','')
            y=z.replace(':','')
            c=y.replace(' ','')
            bill = phno + c[0:len(c)-7]
            if name=='' or phno=='' :
                DLE=CustomDialog()
                DLE.exec()
            else:
                for i in range(1,len(self.df.index)):
                    ins="insert into orders values('"+bill+"','"+name+"','"+phno+"','"+str(self.df.loc[i,'Dish'])+"','"+str(self.df.loc[i,'Quantity'])+"','"+tii[:len(tii)-7]+"','"+str(self.df.loc[i,'Amount'])+"')"
                    cur.execute(ins)
                    con.commit()
                self.customer_name_entry.clear()
                self.customer_phone_entry.clear()
                self.quantity_.clear()
                for i in reversed(range(self.formlayout.count())): 
                    self.formlayout.itemAt(i).widget().setParent(None)
                DLE=CustomDialog2()
                DLE.exec()

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
    if ji==2:
        from option_window import option_window_def
        option_window_def()
    elif ji==1:
        from login_window import login_window_def
        login_window_def()
