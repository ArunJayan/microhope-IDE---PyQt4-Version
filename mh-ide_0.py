#mh-ide.py
import sys ,os
from time import strftime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Microhope_Lib import Microhope_hardware
class Microhope(QMainWindow):
    def __init__(self,app,parent=None):
		QMainWindow.__init__(self,parent)
		self.app = app
		self.time_format = ["%d.%B.%Y,%H:%M"] 
		
		self.Dname = "" 	#stores device address here . 
 		self.Fname = "untitled" 	#current file name here . 
		self.isFileChanged = False	#initially this parameter set false . 
		self.isNewFile = True		#initially this parameter set True .
		self.line_num  = 0
		self.col_num = 0
		self.statusbar_msg = ("Line: %d | Column: %d\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFile :: %s"%(self.line_num,self.col_num,self.Fname))
		self.resize(800,600)
		self.setWindowTitle("MicroHOPE IDE")
		self.statusBar().showMessage(self.statusbar_msg)
		self.form_widget = Microhope_Form(self)
		self.setCentralWidget(self.form_widget)

		self.statusBar().showMessage(self.statusbar_msg)
		self.setStyleSheet("QMainWindow { background-color :rgb(250,254,249);}")
		
		self.initUI()
		#event assiging
		self.form_widget.code_entry.cursorPositionChanged.connect(self.CursorPositionshow)  
		self.form_widget.code_entry.textChanged.connect(self.TextChanged)
		self.show()
    def initToolbar(self):
		#new file
		self.new_action = QAction(QIcon("icons/document-new.png"),"New",self)
		self.new_action.setShortcut("Ctrl+N")
		self.new_action.setStatusTip("Create a new file.")
		self.new_action.triggered.connect(self.newf)
		#open file
		self.open_file = QAction(QIcon("icons/document-open.png"),"New",self)
		self.open_file.setShortcut("Ctrl+O")
		self.open_file.setStatusTip("Open existing programs")
		self.open_file.triggered.connect(self.openf)
		#save action
		self.save_action = QAction(QIcon("icons/document-save.png"),"Save",self)
		self.save_action.setShortcut("Ctrl+S")
		self.save_action.setStatusTip("Save the current program")
		self.save_action.triggered.connect(self.save)
		
		self.toolbar = self.addToolBar("Options")
		self.toolbar.addAction(self.new_action)
		self.toolbar.addAction(self.open_file)
		self.toolbar.addAction(self.save_action)
    def initUI(self):
		self.initToolbar()
		self.initMenubar()
		
    def initMenubar(self):
		menubar = self.menuBar()
		file = menubar.addMenu("File")
		file.addAction(self.new_action)
    def newf(self,e):
		if self.isFileChanged == True:
			reply = QMessageBox.question(self,"Question","Current File is not saved . \nDo you want to save it before closing ?",QMessageBox.Yes,QMessageBox.No,QMessageBox.Cancel) 
			if reply == QMessageBox.Yes:
				self.save()
				self.form_widget.code_entry.clear()
				self.date_time = strftime(self.time_format[0])
				self.update_process_notification("New File")
				self.isNewFile = False
				self.isFileChanged = False
				
			elif reply == QMessageBox.No:
				self.form_widget.code_entry.clear()
				self.date_time = strftime(self.time_format[0])
				self.update_process_notification("New File")
				self.isNewFile = False
				self.isFileChanged = False
			
		else:
					
			self.form_widget.code_entry.clear()
			self.date_time = strftime(self.time_format[0])
			self.update_process_notification("New File")
			self.isNewFile = False
			self.isFileChanged = False
	
    def openf(self):
		filename = QFileDialog.getOpenFileName(self, 'Open File')
		f = open(filename, 'r')
		filedata = f.read()
		self.form_widget.code_entry.setText(filedata)
		f.close()
		self.update_process_notification("Opened file"+filename)
		self.Dname = os.path.split(str(filename))[0]
		self.Fname = os.path.split(str(filename))[1]
		self.statusbar_msg = ("Line: %d | Column: %d\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFile :: %s"%(self.line_num,self.col_num,self.Dname+"/"+self.Fname))
		self.statusBar().showMessage(self.statusbar_msg)
		self.isNewFile = False
		self.isFileChanged = False
    def update_process_notification(self,msg):
		self.date_time = strftime(self.time_format[0])
		self.form_widget.display_.append(self.date_time+"  ::: "+msg)
    def CursorPositionshow(self):
		self.line_num = self.form_widget.code_entry.textCursor().blockNumber()
		self.col_num = self.form_widget.code_entry.textCursor().columnNumber()
		if self.isNewFile == True and self.Dname == "":
			self.statusbar_msg = ("Line: %d | Column: %d\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFile :: %s"%(self.line_num,self.col_num,"untitled"))
		else:
			self.statusbar_msg = ("Line: %d | Column: %d\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFile :: %s"%(self.line_num,self.col_num,self.Dname+"/"+self.Fname))
		self.statusBar().showMessage(self.statusbar_msg)
    def TextChanged(self):
		self.isFileChanged = True
		if self.isNewFile == True and self.isFileChanged == True:
			self.Fname = "untitled"
			self.statusBar().showMessage("Line: %d | Column: %d\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFile :: %s"%(self.line_num,self.col_num,"untitled**"))
		elif self.isNewFile != True and self.isFileChanged == True:
			self.statusBar().showMessage("Line: %d | Column: %d\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFile :: %s"%(self.line_num,self.col_num,self.Dname+"/"+self.Fname+"**"))
			
			
			

		
		
    def save(self):
		"""
		self.Fname = QFileDialog.getSaveFileName(self, 'Save File')
		f = open(self.Fname, 'w')
		filedata = self.form_widget.code_entry.toPlainText()
		f.write(filedata)
		f.close()"""
		
		if self.isNewFile == True: #if the file is new :: FileDialog.getSaveFile() will give the filename of newfile from user .
			self.filename = QFileDialog.getSaveFileName(self, 'Save File')
			f = open(self.filename, 'w')
			#print sample
			self.Dname , self.Fname = os.path.split(str(self.filename))
			filedata = self.form_widget.code_entry.toPlainText() #convert the texts of code_entry into plaintext
			f.write(filedata)
			f.close()
		else :
			f = open(self.Dname+"/"+self.Fname,"w")
			filedata = self.form_widget.code_entry.toPlainText()
			f.write(filedata)
			f.close()
		self.isNewFile = False
		self.isFileChanged = False
		self.statusBar().showMessage("Line: %d | Column: %d\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFile :: %s"%(self.line_num,self.col_num,self.Dname+"/"+self.Fname))
		self.update_process_notification("File "+self.Dname+"/"+self.Fname+" saved.")
		
		
		
		
		
class Microhope_Form(QWidget):
    def __init__(self, parent):        
        super(Microhope_Form, self).__init__(parent)
        layout 		=  QGridLayout(self)
        #layout.setHorizontalSpacing(0)
        #layout.setVerticalSpacing(0)
        hardware_label = QLabel()
        hardware_label.setStyleSheet("QLabel { background-color :rgb(250,254,249);color:green}") 
        hardware_label.resize(600,10)
        
        self.code_entry = QTextEdit(self)
        self.display_ = QTextEdit(self)
        self.display_.setStyleSheet("QTextEdit { background-color : rgb(0,0,0);color:green}") 
        self.display_.setSizePolicy(QSizePolicy.MinimumExpanding,QSizePolicy.Fixed)
        #hardware_label.setSizePolicy(QSizePolicy.MinimumExpanding,QSizePolicy.Fixed)
        self.code_entry.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        layout.addWidget(self.code_entry,0,0)
        layout.addWidget(hardware_label,1,0)
        layout.addWidget(self.display_,2,0)
        hardware_label.setText("/dev/ttyACM0")

		
if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	mh_ = Microhope(app)
	sys.exit(app.exec_())
	

